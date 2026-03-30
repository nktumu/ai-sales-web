"""
AI Sales Team — FastAPI Web Application
All 14 sales commands available via REST API with SSE streaming.
"""

import asyncio
import json
import os
import secrets
import sys
import time
from pathlib import Path
from typing import AsyncGenerator, Dict, Optional, Union

import anthropic
import httpx
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

# ---------------------------------------------------------------------------
# Configuration (all overridable via environment variables)
# ---------------------------------------------------------------------------
ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-6")
ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "SalesTeam#2024!")
SESSION_TTL: int = int(os.getenv("SESSION_TTL_HOURS", "8")) * 3600

AVAILABLE_MODELS = [
    "claude-sonnet-4-6",
    "claude-opus-4-6",
    "claude-haiku-4-5-20251001",
    "claude-3-7-sonnet-20250219",
    "claude-3-5-sonnet-20241022",
]

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"
SCRIPTS_DIR = BASE_DIR.parent / "scripts"
TMP_DIR = Path("/tmp/ai_sales_team")
TMP_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# In-memory stores
# ---------------------------------------------------------------------------
sessions: Dict[str, dict] = {}          # token -> {username, expires, model}
analyses: Dict[str, dict] = {}          # username -> {command -> markdown}

# ---------------------------------------------------------------------------
# FastAPI app
# ---------------------------------------------------------------------------
app = FastAPI(title="AI Sales Team", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Auth helpers
# ---------------------------------------------------------------------------

def create_session(username: str, model: str) -> str:
    token = secrets.token_hex(32)
    sessions[token] = {
        "username": username,
        "model": model,
        "expires": time.time() + SESSION_TTL,
    }
    return token


def get_session(request: Request) -> Optional[dict]:
    token = request.cookies.get("st")
    if not token or token not in sessions:
        return None
    s = sessions[token]
    if time.time() > s["expires"]:
        sessions.pop(token, None)
        return None
    return s


def require_session(request: Request) -> dict:
    s = get_session(request)
    if not s:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return s


# ---------------------------------------------------------------------------
# Claude API helpers
# ---------------------------------------------------------------------------

def get_client(api_key: str = "") -> anthropic.AsyncAnthropic:
    key = api_key or ANTHROPIC_API_KEY
    if not key:
        raise HTTPException(status_code=500, detail="ANTHROPIC_API_KEY not configured")
    return anthropic.AsyncAnthropic(api_key=key)


async def fetch_url_text(url: str, timeout: int = 15) -> str:
    """Fetch a URL and return plain text content (best-effort)."""
    try:
        async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
            headers = {"User-Agent": "Mozilla/5.0 (compatible; SalesBot/1.0)"}
            r = await client.get(url, headers=headers)
            soup = BeautifulSoup(r.text, "html.parser")
            # Remove script/style tags
            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()
            text = soup.get_text(separator="\n", strip=True)
            # Trim to ~6000 chars to stay within context
            return text[:6000]
    except Exception as e:
        return f"[Could not fetch {url}: {e}]"


async def stream_claude(
    system: str,
    user_msg: str,
    model: str,
    max_tokens: int = 8192,
) -> AsyncGenerator[str, None]:
    """Stream Claude response as text chunks, with web search tool enabled."""
    client = get_client()
    tools = [{"type": "web_search_20250305", "name": "web_search"}]

    messages = [{"role": "user", "content": user_msg}]

    # Agentic loop — handles both direct replies and tool-use rounds
    while True:
        try:
            response = await client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system,
                messages=messages,
                tools=tools,
            )
        except anthropic.BadRequestError:
            # Fallback: retry without web search tool
            response = await client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system,
                messages=messages,
            )

        # Yield any text blocks
        for block in response.content:
            if hasattr(block, "text") and block.text:
                yield block.text

        if response.stop_reason == "end_turn":
            break

        if response.stop_reason == "tool_use":
            # Append assistant message and provide tool results
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": "Tool executed server-side.",
                    })
            if tool_results:
                messages.append({"role": "user", "content": tool_results})
            else:
                break
        else:
            break


async def call_claude(
    system: str,
    user_msg: str,
    model: str,
    max_tokens: int = 8192,
) -> str:
    """Non-streaming Claude call. Returns full text response."""
    chunks = []
    async for chunk in stream_claude(system, user_msg, model, max_tokens):
        chunks.append(chunk)
    return "".join(chunks)


# ---------------------------------------------------------------------------
# SSE helpers
# ---------------------------------------------------------------------------

def sse(event: str, data: Union[str, dict]) -> str:
    payload = data if isinstance(data, str) else json.dumps(data)
    return f"event: {event}\ndata: {payload}\n\n"


async def simple_stream(
    system: str,
    user_msg: str,
    model: str,
    command: str,
    username: str,
) -> AsyncGenerator[str, None]:
    """Generic SSE generator: streams Claude output, saves to analyses store."""
    yield sse("status", f"Running {command} analysis...")
    full_text = []
    try:
        async for chunk in stream_claude(system, user_msg, model):
            full_text.append(chunk)
            yield sse("chunk", chunk)
    except Exception as e:
        yield sse("error", str(e))
        return

    result = "".join(full_text)
    # Persist to analysis store
    if username not in analyses:
        analyses[username] = {}
    analyses[username][command] = result

    yield sse("done", {"command": command, "length": len(result)})


# ---------------------------------------------------------------------------
# Auth routes
# ---------------------------------------------------------------------------

@app.post("/api/login")
async def login(request: Request):
    body = await request.json()
    username = body.get("username", "").strip()
    password = body.get("password", "")
    model = body.get("model", CLAUDE_MODEL)

    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if model not in AVAILABLE_MODELS:
        model = CLAUDE_MODEL

    token = create_session(username, model)
    resp = JSONResponse({"ok": True, "username": username, "model": model})
    resp.set_cookie("st", token, httponly=True, samesite="lax", max_age=SESSION_TTL)
    return resp


@app.post("/api/logout")
async def logout(request: Request):
    token = request.cookies.get("st")
    sessions.pop(token, None)
    resp = JSONResponse({"ok": True})
    resp.delete_cookie("st")
    return resp


@app.get("/api/me")
async def me(request: Request):
    s = require_session(request)
    return {"username": s["username"], "model": s["model"]}


@app.get("/api/models")
async def models():
    return {"models": AVAILABLE_MODELS, "default": CLAUDE_MODEL}


@app.patch("/api/model")
async def set_model(request: Request):
    s = require_session(request)
    body = await request.json()
    model = body.get("model", "")
    if model not in AVAILABLE_MODELS:
        raise HTTPException(status_code=400, detail="Unknown model")
    token = request.cookies.get("st")
    if token in sessions:
        sessions[token]["model"] = model
    return {"ok": True, "model": model}


# ---------------------------------------------------------------------------
# Import prompts
# ---------------------------------------------------------------------------
from prompts import PROMPTS, build_user_message  # noqa: E402 — after app creation


# ---------------------------------------------------------------------------
# Generic single-agent SSE endpoint
# ---------------------------------------------------------------------------

SINGLE_AGENT_COMMANDS = [
    "quick", "research", "qualify", "contacts", "outreach",
    "followup", "prep", "proposal", "objections", "icp", "competitors",
]


@app.post("/api/{command}")
async def run_command(command: str, request: Request):
    if command not in SINGLE_AGENT_COMMANDS + ["prospect", "report", "report-pdf"]:
        raise HTTPException(status_code=404, detail=f"Unknown command: {command}")

    s = require_session(request)
    body = await request.json()
    model = s["model"]
    username = s["username"]

    # ----- /api/report — compile from stored analyses -----
    if command == "report":
        stored = analyses.get(username, {})

        async def report_stream():
            yield sse("status", "Compiling pipeline report from stored analyses...")
            system = PROMPTS["report"]["system"]
            context = "\n\n---\n\n".join(
                f"## {cmd.upper()}\n{text}" for cmd, text in stored.items()
            ) or "No analyses found. Run /prospect or other commands first."
            user_msg = f"Compile a pipeline report from these analyses:\n\n{context}"
            full = []
            async for chunk in stream_claude(system, user_msg, model):
                full.append(chunk)
                yield sse("chunk", chunk)
            analyses.setdefault(username, {})["report"] = "".join(full)
            yield sse("done", {"command": "report"})

        return StreamingResponse(report_stream(), media_type="text/event-stream")

    # ----- /api/report-pdf — generate PDF from stored report -----
    if command == "report-pdf":
        stored = analyses.get(username, {})
        report_md = stored.get("report", "")

        async def pdf_stream():
            yield sse("status", "Generating PDF report...")
            if not report_md:
                yield sse("error", "No pipeline report found. Run /report first.")
                return

            # Build JSON for the PDF script
            import subprocess, sys
            prospect_data = stored.get("prospect", "")
            score = 74  # default; could parse from prospect_data

            pdf_input = {
                "title": "Sales Pipeline Report",
                "date": time.strftime("%Y-%m-%d"),
                "overall_pipeline_score": score,
                "health_rating": "Good",
                "total_prospects": 1 if prospect_data else 0,
                "prospects": [],
                "top_prospects": [],
                "action_items": {"quick_wins": [], "this_week": [], "this_month": []},
                "pipeline_health": {
                    "total_prospects": 1 if prospect_data else 0,
                    "average_score": score,
                    "a_grade_count": 0, "a_grade_pct": 0,
                    "b_grade_count": 1, "b_grade_pct": 100,
                    "c_grade_count": 0, "c_grade_pct": 0,
                    "d_grade_count": 0, "d_grade_pct": 0,
                    "highest_score": score, "lowest_score": score,
                    "health_rating": "Good",
                },
                "score_distribution": {
                    "A+": {"count": 0, "pct": 0, "prospects": []},
                    "A": {"count": 0, "pct": 0, "prospects": []},
                    "B": {"count": 1, "pct": 100, "prospects": ["Latest Prospect"]},
                    "C": {"count": 0, "pct": 0, "prospects": []},
                    "D": {"count": 0, "pct": 0, "prospects": []},
                },
                "weekly_focus": [],
                "methodology": {
                    "company_fit_weight": 25,
                    "contact_access_weight": 20,
                    "opportunity_quality_weight": 20,
                    "competitive_position_weight": 15,
                    "outreach_readiness_weight": 20,
                },
            }

            json_path = TMP_DIR / f"pdf_input_{username}.json"
            pdf_path = TMP_DIR / f"SALES-REPORT-{time.strftime('%Y-%m-%d')}-{username}.pdf"
            json_path.write_text(json.dumps(pdf_input))

            script = str(SCRIPTS_DIR / "generate_pdf_report.py")
            proc = subprocess.run(
                [sys.executable, script, str(json_path), str(pdf_path)],
                capture_output=True, text=True,
            )
            json_path.unlink(missing_ok=True)

            if proc.returncode != 0:
                yield sse("error", f"PDF generation failed: {proc.stderr[:300]}")
                return

            filename = pdf_path.name
            yield sse("pdf_ready", {"filename": filename, "url": f"/api/download/{filename}"})
            yield sse("done", {"command": "report-pdf"})

        return StreamingResponse(pdf_stream(), media_type="text/event-stream")

    # ----- /api/prospect — 5 parallel agents -----
    if command == "prospect":
        url = body.get("url", "").strip()
        if not url:
            raise HTTPException(status_code=400, detail="url is required")

        async def prospect_stream():
            yield sse("status", "Fetching company homepage...")
            page_content = await fetch_url_text(url)

            yield sse("status", "Launching 5 parallel analysis agents...")

            agent_names = [
                ("company",      "Company Research & Firmographics"),
                ("contacts",     "Decision Maker Intelligence"),
                ("opportunity",  "Opportunity & BANT Qualification"),
                ("competitive",  "Competitive Positioning"),
                ("strategy",     "Outreach Strategy & Messaging"),
            ]

            context = f"Target URL: {url}\n\nHomepage content:\n{page_content}"

            async def run_agent(key: str, label: str) -> tuple[str, str]:
                p = PROMPTS.get(f"prospect_{key}", PROMPTS["research"])
                result = await call_claude(p["system"], context, model, max_tokens=6000)
                return key, result

            tasks = [run_agent(k, label) for k, label in agent_names]
            agent_results: dict[str, str] = {}

            completed = 0
            for coro in asyncio.as_completed(tasks):
                key, result = await coro
                agent_results[key] = result
                completed += 1
                label = next(l for k, l in agent_names if k == key)
                yield sse("agent_done", {"label": label, "index": completed, "total": 5})

            yield sse("status", "Calculating Prospect Score and generating report...")

            # Build synthesis prompt
            synthesis_system = PROMPTS["prospect_synthesis"]["system"]
            synthesis_user = (
                f"URL: {url}\n\n"
                f"## Company Research\n{agent_results.get('company', '')}\n\n"
                f"## Contact Intelligence\n{agent_results.get('contacts', '')}\n\n"
                f"## Opportunity Assessment\n{agent_results.get('opportunity', '')}\n\n"
                f"## Competitive Analysis\n{agent_results.get('competitive', '')}\n\n"
                f"## Outreach Strategy\n{agent_results.get('strategy', '')}"
            )

            full = []
            async for chunk in stream_claude(synthesis_system, synthesis_user, model, max_tokens=8192):
                full.append(chunk)
                yield sse("chunk", chunk)

            result_text = "".join(full)
            analyses.setdefault(username, {})["prospect"] = result_text
            yield sse("done", {"command": "prospect"})

        return StreamingResponse(prospect_stream(), media_type="text/event-stream")

    # ----- All other single-agent commands -----
    if command not in PROMPTS:
        raise HTTPException(status_code=404, detail=f"No prompt found for {command}")

    prompt_cfg = PROMPTS[command]
    user_msg = build_user_message(command, body, analyses.get(username, {}))

    async def gen():
        async for chunk in simple_stream(prompt_cfg["system"], user_msg, model, command, username):
            yield chunk

    return StreamingResponse(gen(), media_type="text/event-stream")


# ---------------------------------------------------------------------------
# PDF download
# ---------------------------------------------------------------------------

@app.get("/api/download/{filename}")
async def download_pdf(filename: str, request: Request):
    require_session(request)
    # Security: only allow known PDF filenames from TMP_DIR
    safe_name = Path(filename).name
    path = TMP_DIR / safe_name
    if not path.exists() or not safe_name.endswith(".pdf"):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path, filename=safe_name, media_type="application/pdf")


# ---------------------------------------------------------------------------
# Stored analyses
# ---------------------------------------------------------------------------

@app.get("/api/analyses")
async def get_analyses(request: Request):
    s = require_session(request)
    return {"analyses": list(analyses.get(s["username"], {}).keys())}


@app.delete("/api/analyses")
async def clear_analyses(request: Request):
    s = require_session(request)
    analyses.pop(s["username"], None)
    return {"ok": True}


# ---------------------------------------------------------------------------
# Static files — must be LAST
# ---------------------------------------------------------------------------
app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="static")
