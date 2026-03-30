# Lead Qualification: Tekion Corp
**URL:** https://tekion.com
**Date:** March 29, 2026
**Opportunity Quality Score: 79/100**
**Lead Grade: A — Sales Qualified Lead**
**BANT Score: 82/100 | MEDDIC Completeness: 83%**

---

## Qualification Snapshot

| Metric | Value |
|--------|-------|
| **Company** | Tekion Corp |
| **Industry** | Vertical SaaS — Automotive Retail Technology (DMS/Cloud Platform) |
| **Employees** | ~2,747 |
| **Revenue** | $273.5M (Sept 2025) |
| **Valuation** | $4B (Private) |
| **BANT Score** | 82/100 |
| **MEDDIC Completeness** | 83% |
| **Opportunity Quality Score** | 79/100 |
| **Lead Grade** | A — Sales Qualified Lead |
| **Urgency Level** | High |
| **Recommended Action** | Assign senior rep immediately. Multi-thread to Jacob Shulman (CFO), VP Engineering, and Principal Security Engineer. Lead with AI data infrastructure and compliance narrative. |

---

## BANT Scorecard

| Dimension | Score | Key Evidence | Confidence |
|-----------|-------|-------------|------------|
| **Budget** | 22/25 | $200M Dragoneer round (July 2024); $600M total raised; ex-JFrog IPO CFO hired; 60%+ ARC revenue growth in 2025 | High |
| **Authority** | 20/25 | Jacob Shulman (CFO), Jay Vijayan (CEO), Guru Sankararaman (COO) publicly identified; enterprise buying committee inferred from company scale | Medium |
| **Need** | 22/25 | ISO 27001, SOC2, GLBA, FTC Safeguards, CCPA, GDPR compliance obligations; multi-cloud (Azure + AWS) data sprawl; agentic AI platform requiring robust data foundation; active security hiring across 4+ roles | High |
| **Timeline** | 18/25 | NADA 2026 agentic AI launch (February 2026) driving immediate data infrastructure demands; ISO/IEC 42001 certification requires ongoing audit trails; IPO-readiness posture with ex-IPO CFO | Medium |
| **TOTAL** | **82/100** | | |

---

### Budget Analysis

**Score: 22/25 | Confidence: High**

Tekion presents one of the clearest budget signals available in pre-IPO SaaS: a company growing at 60%+ annually with $600M in cumulative funding and a CFO explicitly brought in from an IPO track. Key evidence:

- **$200M Dragoneer Investment (July 2024):** Late-stage growth capital from a tier-1 investor signals both availability of capital and investor pressure to build enterprise-grade infrastructure for scale and eventual liquidity event.
- **$273.5M Revenue (Sept 2025):** At this revenue scale and growth rate, annual IT infrastructure and security spend typically runs $5–15M+ for a well-funded SaaS company. Enterprise data management solutions are not discretionary at this stage.
- **Jacob Shulman, CFO (ex-JFrog):** Shulman guided JFrog through its 2020 NASDAQ IPO and scaled Mellanox from $48M to $1B+ revenue. His hiring signals an IPO-readiness build-out — public companies require substantially more rigorous data governance, audit trails, and security controls than private ones. This is a direct budget unlock signal.
- **60%+ ARC Revenue Growth (2025):** Rapid revenue growth creates proportional data volume expansion across thousands of dealership customers. Infrastructure spend must scale with data growth.
- **Enterprise Tech Stack:** Azure Kubernetes Service, Kafka, MongoDB, SageMaker, Azure ML, Vertex AI, Databricks — this is an organization already paying premium enterprise-tier cloud costs. An enterprise data management layer is a natural adjacency.
- **Active Expansion:** Automotive Partner Cloud 2.0 grew 40x since launch, and Tekion handles transaction, PII, and financial data across thousands of dealerships — indicating massive and growing data volumes requiring protection.

**What is still needed:** Confirmation of annual IT/security budget cycle (likely Q1 planning), and whether infrastructure decisions are centralized or distributed across engineering leads.

---

### Authority Analysis

**Score: 20/25 | Confidence: Medium**

Tekion's leadership team is publicly visible, but the precise buying committee configuration for enterprise infrastructure purchases requires a discovery call to fully map.

**Identified Decision-Makers:**

| Name | Title | Role in Purchase | Access Path |
|------|-------|-----------------|-------------|
| Jacob Shulman | CFO | Economic buyer for infrastructure spend | LinkedIn, press releases |
| Jay Vijayan | CEO/Founder | Vision authority; likely signs off on strategic vendor relationships | LinkedIn, conference appearances |
| Guru Sankararaman | COO | Operational oversight of platform reliability | LinkedIn |
| Rob Glenn | CRO | Revenue operations data stakeholder | LinkedIn |
| Ved Surtani | VP Engineering | Technical authority, likely leads evaluation | LinkedIn |

**Buying Process Inference:**

At ~2,747 employees and $4B valuation, Tekion sits at the boundary between mid-market and enterprise procurement complexity. Expect:
- Technical evaluation led by VP Engineering / Principal Security Engineer
- Financial sign-off by CFO (Jacob Shulman) for contracts above ~$500K
- Legal/compliance review for data handling agreements (they already have a DPA framework published)
- Possible vendor security questionnaire (they have an active Trust Portal at trust.tekion.com powered by Akitra)

**Authority Gap:** No publicly named CTO or VP of Infrastructure. The Principal Security Engineer job posting (open) suggests the security architecture function is still being built out — this is an opportunity to insert the conversation early.

**What is still needed:** Confirm reporting structure of VP Engineering; identify if there is a dedicated IT Procurement or Vendor Management function.

---

### Need Analysis

**Score: 22/25 | Confidence: High**

Tekion has multiple, compounding, validated needs that map directly to enterprise data management, backup/recovery, and data security solutions.

**Pain Point 1 — Multi-Cloud Data Sprawl (Severity: Critical)**
Tekion runs simultaneously on Azure (primary, AKS-based) and AWS (SageMaker for ML workloads), with additional ML infrastructure on Google's Vertex AI. Managing backup, recovery, and data governance across three cloud providers with a unified policy layer is a textbook enterprise data management problem. Their job posting for Principal Security Engineer explicitly calls for "security architectures and best practices for cloud environments (AWS, Azure, Google Cloud, etc.)" — confirming this is a live, unsolved challenge.

**Pain Point 2 — Compliance Obligation Stack (Severity: Critical)**
Tekion's compliance portfolio is extensive and growing:
- SOC 1 Type II + SOC 2 Type II (annual audits)
- ISO/IEC 27001:2022 (annual audits)
- ISO/IEC 27701:2019 (PII management)
- ISO/IEC 42001:2023 (AI governance — one of the first automotive platforms certified)
- GLBA / FTC Safeguards Rule
- CCPA / CPRA / GDPR

Each of these frameworks requires demonstrable data lineage, access controls, audit trails, and incident response capabilities. The "one audit trail" messaging in their NADA 2026 announcement signals this is a strategic priority — and a gap that enterprise data management directly addresses.

**Pain Point 3 — AI/ML Data Pipeline Integrity (Severity: High)**
The NADA 2026 agentic AI platform (Technician AI, Scheduler AI, T1) is built on "accurate, real-time data from across its end-to-end system." AI models are only as reliable as their training data and the backup/recovery infrastructure protecting that data. Any data corruption, loss, or unavailability directly degrades AI model performance — a mission-critical risk for a company positioning AI as its core differentiator.

**Pain Point 4 — Dealer Customer Data Protection (Severity: High)**
Tekion processes dealer transactions, OEM data, customer PII, vehicle inventory, and financial data across thousands of dealerships. A breach or data loss event at Tekion would affect not just Tekion but their entire dealer network — creating massive downstream liability. Ransomware resilience and immutable backup are directly relevant.

**Pain Point 5 — IPO-Readiness Data Governance (Severity: Medium-High)**
With an ex-IPO CFO at the helm, Tekion is almost certainly building the data governance infrastructure required for public company status, even if an IPO is not imminent. Public companies require materially stronger data audit, lineage, and recovery capabilities than private ones.

**What is still needed:** Confirm whether Tekion uses a current backup/recovery vendor (Veeam, Commvault, Zerto, etc.) and their satisfaction level. Assess data volume in TB/PB terms.

---

### Timeline Analysis

**Score: 18/25 | Confidence: Medium**

Multiple convergent trigger events suggest a 1–3 month initial engagement window, with a 3–6 month deal cycle likely.

**Trigger Event 1 — NADA 2026 Agentic AI Launch (February 2026, 7 weeks ago)**
The public launch of Tekion's agentic AI platform is the most significant near-term trigger. Agentic AI creates immediate, substantial new data infrastructure requirements: training data storage, model artifact backup, inference data pipelines, audit trails for AI decisions (required by ISO/IEC 42001), and recovery SLAs for AI-dependent workflows. This event is recent enough that budget allocation conversations are likely happening now.

**Trigger Event 2 — Jacob Shulman CFO Appointment (January 2024, 15 months ago)**
While not brand new, Shulman has had enough time to assess the infrastructure landscape and is now in the build-out phase. CFOs from IPO backgrounds typically complete their "what needs to be enterprise-grade" audit in the first 12 months and begin procurement in months 12-24. This positions Q1-Q2 2026 as a natural buying window.

**Trigger Event 3 — ISO/IEC 42001 Certification (Active)**
Tekion is already certified. Maintaining this certification requires continuous monitoring, audit trails, and data governance tooling — creating an ongoing procurement need, not a one-time event.

**Trigger Event 4 — Active Security Hiring (Confirmed March 2026)**
Four active security engineering roles (IT Security Ops Engineer, Security Engineer I, Senior Security Engineer, Principal Security Engineer) indicate a team being built to manage expanding infrastructure. New security hires typically trigger tooling evaluations within 30–90 days of starting.

**Inhibitor — No IPO Imminent:**
CEO Jay Vijayan has publicly stated no IPO timeline. This removes one urgency accelerant but does not eliminate the need — operational scale alone justifies enterprise data infrastructure investment.

**Estimated Deal Timeline:** Discovery call in April 2026 → POC in May-June 2026 → Contract Q3 2026.

**What is still needed:** Identify budget cycle (calendar year or fiscal year Q1); determine if there is an active RFP or vendor evaluation in progress.

---

## MEDDIC Assessment

| Element | Finding | Evidence | Confidence |
|---------|---------|----------|------------|
| **Metrics** | Compliance audit pass rates, RTO/RPO SLAs, data breach cost avoidance, AI model uptime | ISO/IEC 42001 cert, SOC2 Type II, NADA 2026 AI launch | Medium |
| **Economic Buyer** | Jacob Shulman (CFO) — primary; Jay Vijayan (CEO) for strategic decisions | BusinessWire CFO announcement, Crunchbase | High |
| **Decision Criteria** | Compliance coverage, multi-cloud support, audit trail capability, AI data pipeline support | Trust Portal, job postings, NADA 2026 messaging | Medium |
| **Decision Process** | Technical eval (VP Eng) → Security review → CFO sign-off → Legal/DPA review | Company scale, Trust Portal, published DPA | Medium |
| **Identify Pain** | Multi-cloud data sprawl, AI data integrity, compliance stack, dealer PII protection | Job postings, compliance page, NADA 2026 press release | High |
| **Champion** | Principal Security Engineer (role being filled) or VP Engineering (Ved Surtani) | Active job listings, LinkedIn | Low-Medium |

**MEDDIC Completeness: 5/6 elements at Medium+ confidence = 83%**

---

### Metrics Deep Dive

Tekion's primary success metrics for a data management solution would center on:

1. **Compliance Audit Pass Rate** — Must maintain SOC2 Type II, ISO 27001, ISO 27701, and ISO 42001 certifications annually. Any finding related to data backup, recovery, or access controls is a material risk to certification. Evidence: active Trust Portal at trust.tekion.com.

2. **Recovery Time Objective (RTO) / Recovery Point Objective (RPO)** — Tekion's agentic AI platform is a real-time operational system for dealerships. Downtime directly costs dealer revenue. RTO of minutes/hours, not days, is likely the threshold.

3. **Data Breach Cost Avoidance** — Handling PII across thousands of dealerships creates massive breach liability under GLBA, CCPA, and GDPR. A single incident at scale could generate hundreds of millions in fines and remediation costs.

4. **AI Model Integrity** — As an AI-native platform, data corruption affecting training pipelines or inference data would directly degrade product quality — a competitive and reputational risk.

5. **Audit Trail Completeness** — ISO/IEC 42001 (AI governance) and SOC2 both require demonstrable, complete audit trails. The ability to show regulators and customers exactly who accessed what data when is a core buying criterion.

**How our solution impacts these metrics:** Immutable backup eliminates RPO risk; automated compliance reporting reduces audit prep time; unified multi-cloud data management consolidates sprawl; data classification and access governance supports audit trail completeness.

---

### Economic Buyer Profile

**Primary: Jacob Shulman, CFO**
- Background: JFrog (IPO 2020, NASDAQ), Mellanox Technologies ($48M → $1B+ revenue)
- Buying lens: Infrastructure investments that reduce risk, support compliance, and build the foundation for scale/public-company readiness
- Communication style: Finance-first; will require ROI modeling, risk quantification (cost of breach vs. cost of solution), and TCO analysis
- Access: LinkedIn (active profile), press/conference appearances
- Trigger language: "data risk," "audit readiness," "compliance cost reduction," "infrastructure for scale"

**Secondary: Jay Vijayan, CEO/Founder**
- Background: Former Tesla CIO; deep technical conviction; built Tekion on the premise that legacy systems fail modern automotive retail
- Buying lens: Strategic alignment with "AI You Can Trust" positioning; will care whether the solution reinforces or undermines their trust narrative
- Trigger language: "data integrity for AI," "trusted data foundation," "enabling responsible AI"

**Tertiary: VP Engineering (Ved Surtani) / Principal Security Engineer (role open)**
- Technical champions who will lead the evaluation
- Likely gatekeepers before CFO/CEO engagement

---

### Decision Criteria Assessment

Based on Tekion's tech stack, compliance posture, and public messaging, their evaluation criteria in ranked order:

1. **Multi-cloud coverage (Azure + AWS + GCP)** — Non-negotiable given their three-cloud footprint. Any solution must provide unified management across all three. [Evidence: Azure primary, AWS SageMaker, Vertex AI on GCP; Principal Security Engineer JD]

2. **Compliance automation and audit trail** — SOC2, ISO 27001/27701/42001, GLBA, CCPA/GDPR reporting must be automatable, not manual. [Evidence: Trust Portal, published compliance page]

3. **Scalability at dealership data volumes** — Millions of transactions, PII records, and vehicle data across thousands of dealers. The solution must handle petabyte-scale. [Evidence: APC 2.0 grew 40x, 60%+ ARC revenue growth]

4. **AI/ML workload support** — Protection and governance of ML training datasets, model artifacts, and inference pipelines. [Evidence: SageMaker, Databricks, Azure ML, Vertex AI in stack]

5. **API-first / Kubernetes-native integration** — Tekion runs on AKS. Solutions requiring agents on bare metal or VM-only architectures will face friction. [Evidence: Microsoft Azure customer story, AKS usage]

6. **Zero-trust security model** — Existing MFA requirements, role-based access, and data segregation posture indicate a zero-trust-aligned security philosophy. [Evidence: Trust Portal, compliance descriptions]

7. **Vendor security questionnaire / DPA compatibility** — Tekion already has a published DPA and requires vendors to meet their security standards as a condition of partnership. [Evidence: tekion.com/legal/privacy/dpa]

---

### Decision Process Map

**Estimated Process for a $500K–$2M+ Enterprise Data Infrastructure Deal:**

```
Stage 1: Technical Discovery (2–4 weeks)
  → Initiated by VP Engineering or Principal Security Engineer
  → Proof of concept scoping, architecture review
  → Security questionnaire submission (trust.tekion.com vendor portal)

Stage 2: Security & Compliance Review (2–4 weeks)
  → Trust team reviews SOC2 report, ISO certifications, penetration test results
  → Legal reviews DPA and data processing terms
  → InfoSec validates multi-cloud architecture

Stage 3: POC / Technical Validation (4–8 weeks)
  → Hands-on testing against Tekion's Azure/AWS environment
  → Validation of compliance reporting outputs
  → Performance benchmarking at scale

Stage 4: Business Case & CFO Review (2–3 weeks)
  → VP Engineering / security team presents recommendation
  → CFO (Shulman) reviews TCO, ROI, risk reduction analysis
  → Contract negotiation with legal

Stage 5: Contract & Onboarding (2–4 weeks)
  → MSA, DPA, and SLA finalization
  → Phased deployment plan

Estimated Total Cycle: 3–6 months from first contact
Estimated Deal Size: $500K–$2M ARR (based on company scale and data volume)
```

---

### Pain Point Analysis

| Pain Point | Evidence | Severity | Our Solution Relevance | Confidence |
|------------|---------|----------|----------------------|------------|
| Multi-cloud data sprawl (Azure + AWS + GCP) | Principal Security Engineer JD, tech stack | Critical | Unified multi-cloud data management | High |
| Compliance audit trail maintenance | SOC2 Type II, ISO 27001/27701/42001, GLBA, CCPA | Critical | Automated compliance reporting, immutable audit logs | High |
| AI/ML data integrity and protection | NADA 2026 agentic AI launch, Databricks/SageMaker stack | High | ML workload backup, data lineage | High |
| Dealer PII and financial data breach risk | GLBA, CCPA, thousands of dealers in platform | High | Ransomware resilience, immutable backup, encryption at rest/transit | High |
| IPO-readiness data governance | CFO Shulman from JFrog IPO; "no timeline" but infrastructure building | Medium-High | Data governance framework, audit readiness | Medium |
| Rapid data growth outpacing current tooling | 60%+ revenue growth, APC 2.0 40x growth, 348% 4-year growth | Medium | Scalable backup/recovery, auto-tiering | Medium |

---

### Champion Strategy

**Target 1: Principal Security Engineer (role currently open — highest potential)**
- This person will be hired specifically to solve the security architecture challenges identified in the job description: cloud security across AWS/Azure/GCP, IAM frameworks, DevSecOps
- A newly hired Principal Security Engineer at a $4B company with major compliance obligations will immediately evaluate the tooling landscape
- **Approach:** Connect with the candidate on LinkedIn before they start, or identify the person once hired. Offer to do a technical architecture briefing as part of their onboarding. Frame it as helping them succeed in their new role.

**Target 2: Ved Surtani, VP Engineering**
- Engineering leader overseeing the platform that all this data runs on
- Has direct budget influence over infrastructure tooling
- **Approach:** LinkedIn outreach referencing the NADA 2026 AI platform launch; lead with AI data infrastructure narrative ("ensuring your agentic AI platform has the trusted data foundation it needs")

**Target 3: IT Security Ops Engineer (role open)**
- Day-to-day operator who will live in the tooling
- Strong technical champion if engaged early; can pull through the deal from below
- **Approach:** Engage after hire through community events, webinars, or direct outreach with a technical POV on multi-cloud security operations

---

## Buying Signals Detected

| # | Signal | Source | Strength | Relevance |
|---|--------|--------|----------|-----------|
| 1 | NADA 2026 agentic AI platform launch (February 2026) | BusinessWire, Yahoo Finance | Strong | AI platform requires robust data infrastructure, audit trails, and backup for ML pipelines |
| 2 | ISO/IEC 42001 AI governance certification (first in automotive retail) | NADA 2026 press release | Strong | Ongoing certification requires continuous data governance and audit capability |
| 3 | 4 active security engineering job openings simultaneously | tekion.com/careers | Strong | Active security team build-out = tooling evaluation imminent |
| 4 | Jacob Shulman (ex-JFrog IPO CFO) hired as CFO | BusinessWire, Nasdaq press release | Strong | IPO-track CFO signals infrastructure maturity investment; familiar with enterprise data governance requirements |
| 5 | $200M Dragoneer investment (July 2024) | Crunchbase, press | Strong | Capital available; investor pressure to build enterprise-grade infrastructure |
| 6 | SOC2 Type II + ISO 27001 + GLBA + CCPA/GDPR compliance obligations | Trust Portal, compliance page | Strong | Each framework creates explicit, auditable data management requirements |
| 7 | Multi-cloud footprint: Azure + AWS + GCP simultaneously | Microsoft customer story, job postings | Strong | Unified data management across 3 clouds is a known, expensive operational gap |
| 8 | 60%+ ARC revenue growth in 2025 | NADA 2026 keynote announcement | Moderate | Rapid growth = rapid data volume growth = scaling data infrastructure needs |
| 9 | Automotive Partner Cloud 2.0 grew 40x since launch | Tekion blog | Moderate | Partner ecosystem data sprawl; integration points multiply backup/recovery complexity |
| 10 | "One platform, one security model, one audit trail" messaging | NADA 2026 press release | Moderate | Public acknowledgment that unified audit trail is a strategic priority — implying gaps exist today |
| 11 | Published Data Processing Agreement on website | tekion.com/legal/privacy/dpa | Moderate | Mature vendor security program in place; they know how to buy and vet data vendors |

---

## Red Flags

| # | Red Flag | Source | Severity | Mitigation |
|---|---------|--------|----------|------------|
| 1 | No confirmed IPO timeline — CEO explicitly says "no rush" | Automotive News interview | Medium | IPO is not required for the need to exist; compliance and operational scale alone justify the investment. Reframe to operational risk, not IPO prep. |
| 2 | Primary cloud is Azure — Microsoft has native backup/security products (Azure Backup, Microsoft Defender) | Microsoft customer story | Medium | Azure-native tools lack multi-cloud coverage (AWS/GCP), do not provide true immutability, and cannot cover the full data estate. Lead with multi-cloud gap. |
| 3 | Company may already have incumbent backup/recovery vendor (unknown) | No public data found | Medium | Qualify early: "What does your current backup and recovery architecture look like for your multi-cloud environment?" Frame displacement as a risk reduction upgrade. |
| 4 | IT Security Ops role based in Bangalore — offshore team may have different tooling authority | Tekion careers page | Low | Ensure US-based leadership (VP Engineering, CFO) is the primary engagement point. Bangalore team is likely implementation, not purchase authority. |
| 5 | Complex enterprise procurement likely — DPA, security questionnaire, legal review | Trust Portal, published DPA | Low | Prepare SOC2 Type II report, ISO certificates, penetration test summary, and completed DPA before first meeting. Reduce friction by anticipating their vendor vetting process. |
| 6 | Jay Vijayan is a technical founder who built the platform from the ground up — may have strong "build vs. buy" instinct | Background research | Low | Lead with the cost of building vs. buying. Quantify the engineering time required to replicate immutable backup, multi-cloud data governance, and compliance automation in-house. |

---

## Opportunity Quality Score: 79/100

| Component | Raw Score | Weight | Weighted Score |
|-----------|-----------|--------|---------------|
| BANT Score | 82/100 | 50% | 41.0 |
| MEDDIC Completeness | 83/100 | 30% | 24.9 |
| Urgency Modifier | 65/100 | 20% | 13.0 |
| **TOTAL** | | **100%** | **78.9 → 79/100** |

**Urgency Modifier Rationale (65/100):** NADA 2026 AI launch is a strong recent trigger event (7 weeks ago), and active security hiring creates a 30–90 day tooling evaluation window. Score capped at 65 (not 80+) because no confirmed active RFP and CEO has signaled no imminent IPO — removing one major urgency amplifier.

---

## Recommended Approach

**Lead Grade: A — Sales Qualified Lead**

**Strategy:**

Tekion is a high-conviction target with compounding urgency signals. The NADA 2026 agentic AI platform launch is the single best entry point: their public positioning of "AI You Can Trust" built on "one platform, one security model, one audit trail" is an explicit acknowledgment that data integrity and governance are mission-critical. Your opening message should not be about backup software — it should be about protecting the data foundation that their agentic AI platform depends on.

The multi-thread approach is essential here. Jacob Shulman (CFO) is the economic buyer and speaks the language of risk reduction, compliance cost, and IPO-readiness infrastructure. Jay Vijayan (CEO) is the visionary who will care that your solution enables — not constrains — their AI ambitions. The Principal Security Engineer role, once filled, will be the technical champion and day-to-day evaluator. Engage all three tracks simultaneously.

The timing is favorable: the agentic AI launch creates a fresh, specific business justification for data infrastructure investment. Their ISO/IEC 42001 AI governance certification creates an ongoing audit obligation that needs tooling support. And four simultaneous security hires signal a team being built to evaluate exactly the category of solutions you offer. Move now — this window is 30–90 days wide before the security team is fully staffed and potentially attached to incumbents.

**Deal Size Estimate:** $750K–$2M ARR, depending on scope (backup/recovery only vs. full data management and governance platform). Multi-year contract likely given compliance and AI platform dependencies.

---

## Next Steps

1. **Connect with Jacob Shulman (CFO) on LinkedIn this week** — Reference the NADA 2026 AI platform launch. Lead with: "Congratulations on the agentic AI launch at NADA — as Tekion becomes the data backbone for thousands of dealerships, what does your data resilience and governance infrastructure look like across your Azure/AWS/GCP environment?" Do not pitch. Open a conversation.

2. **Monitor the Principal Security Engineer hire** — Set up a LinkedIn alert for new Tekion Principal Security Engineer hires. The moment this person starts, they are the highest-priority champion prospect. Reach out within their first 30 days with a technical briefing offer.

3. **Prepare a Tekion-specific ROI brief before outreach** — Calculate: (a) estimated cost of a breach affecting thousands of dealerships under GLBA/CCPA, (b) annual audit prep time savings with automated compliance reporting, (c) engineering hours saved vs. building multi-cloud data governance in-house. CFO Shulman will want numbers.

4. **Request a technical architecture briefing with VP Engineering (Ved Surtani)** — Frame it as: "We're seeing companies running agentic AI on AKS + SageMaker + Vertex AI face a specific set of data protection challenges — we'd like to share what we're seeing and hear what your architecture looks like." Peer-to-peer, no pitch.

5. **Submit vendor security documentation proactively** — Tekion has a formal Trust Portal and vendor DPA process. Before or during the first meeting, send your SOC2 Type II report, ISO 27001 certificate, and a pre-completed DPA. This signals you understand their process and reduces procurement friction by weeks.

---

*Generated by AI Sales Team — `/sales qualify` | Data sourced March 29, 2026*

---

## Sources

- [Tekion Trust Portal — Compliance](https://tekion.com/trust-portal/compliance)
- [Tekion Trust Portal — Privacy](https://tekion.com/trust-portal/privacy)
- [Tekion at NADA 2026](https://tekion.com/nada2026)
- [Tekion Sets New Standard for Agentic AI at NADA 2026 — BusinessWire](https://www.businesswire.com/news/home/20260205479848/en/Tekion-the-AI-Native-Platform-Sets-a-New-Standard-for-Agentic-AI-in-Automotive-Retail-at-NADA-2026)
- [Tekion Agentic AI Gambit — WebProNews](https://www.webpronews.com/tekions-agentic-ai-gambit-how-one-company-aims-to-rewire-the-entire-automotive-retail-experience/)
- [Tekion NADA 2026 Recap Blog](https://tekion.com/blog/nada-2026-recap-momentum-community-and-the-ai-native-future)
- [Tekion Appoints Jacob Shulman CFO and Rob Glenn CRO — BusinessWire](https://www.businesswire.com/news/home/20240102305605/en/Tekion-Appoints-New-Chief-Financial-Officer-and-Chief-Revenue-Officer)
- [Jacob Shulman CFO — Nasdaq Press Release](https://www.nasdaq.com/press-release/tekion-appoints-new-chief-financial-officer-and-chief-revenue-officer-2024-01-02)
- [Jacob Shulman — Crunchbase](https://www.crunchbase.com/person/jacob-shulman)
- [Tekion CEO Jay Vijayan: No Timeline for IPO — Automotive News](https://www.autonews.com/retail/an-tekion-cautious-about-ipo/)
- [Tekion IPO — Forge Global](https://forgeglobal.com/tekion_ipo/)
- [Tekion 2026 Company Profile — PitchBook](https://pitchbook.com/profiles/company/171103-78)
- [IT Security Ops Engineer — Tekion Careers](https://tekion.com/job-openings/job/7100031003)
- [Principal Security Engineer — Tekion Careers](https://tekion.com/job-openings/job/6304484003)
- [Tekion Builds ARC with Azure — Microsoft Customer Stories](https://www.microsoft.com/en/customers/story/21405-tekion-corp-azure)
- [Automotive Partner Cloud 2.0 Grows 40x — Tekion Blog](https://tekion.com/blog/a-new-era-of-dealer-controlled-tech-automotive-partner-cloud-2-grows-40x-since-launch)
- [Tekion Privacy Policy (Sept 2025)](https://tekion.com/legal/privacy/privacy-policy/revisions/09-05-2025)
- [Tekion Data Processing Agreement](https://tekion.com/legal/privacy/dpa)
- [Tekion GLBA/Safeguards Guidance](https://tekion.com/resources/guidance-for-dealerships-on-ftc-safegaurds-glba)
