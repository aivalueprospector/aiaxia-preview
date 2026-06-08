# EduAsiste Security FAQ

> _EduAsiste education-market variant of the ProAsiste security FAQ (product-research #16). Authored 2026-06-08._

Answers to the security and privacy questions that parents, schools, and tutors ask before trusting EduAsiste with student data. The focus here is your child's data, and the rules that protect children's records.

---

## Quick Reference

| Tier | Infrastructure | Security Level |
|------|----------------|----------------|
| **SILVER** | Google Workspace | Standard education security |
| **GOLD** | Google Workspace | Standard education security |
| **PLATINUM** | Google Cloud | Enhanced cloud security |
| **DIAMOND** | Google Cloud | Enhanced cloud security |

| Privacy / Compliance Need | How EduAsiste Handles It | Status |
|---------------------------|--------------------------|--------|
| FERPA (US student education records) | Per-learner data isolation, encryption, export/deletion on request | Technical controls today; formal documentation in progress (in-house) |
| COPPA (US children under 13) | Parental/school consent posture, no profiling, no model training on student data | Technical controls today; formal documentation in progress (in-house) |
| GDPR / data residency (EU & LATAM schools) | Encryption, no model training, export-on-request; regional residency on request | In progress (in-house) |
| HIPAA / SOC 2 (orgs that also need them) | Control framework and audit evidence | In progress (in-house) |
| Role-based access (school/district IAM) | Per-workspace access today; district IAM scoping | In progress (in-house) |

> **Plain-language note for parents:** "Standard security" already encrypts everything, keeps your child's data separate from every other learner's, and never feeds it to AI training. The formal audit paperwork and signed agreements that a district's lawyers ask for are being built in-house and are in progress. That's not something a single family normally needs.

---

## Standard Security (Included)

> "Learning data is stored on Google's enterprise-grade infrastructure, the same platform that protects millions of students and teachers worldwide through Google for Education, Gmail, Google Drive, and Google Docs. Larger school and multi-school deployments run on Google Cloud for added scale and monitoring."

**What's Included:**
- **Encryption in transit**: TLS 1.3 for all data moving between your child and the platform
- **Encryption at rest**: AES-256 encryption for stored learning data
- **Google infrastructure**: the proven platform schools already trust
- **Data isolation per learner**: each child's workspace is separate from every other learner's
- **Access control**: token-based authentication
- **Automatic backups**: Google's redundant storage systems

For larger deployments (departments, whole schools, multi-school networks), EduAsiste runs on Google Cloud Platform, adding cloud-native monitoring, VPC and private-connectivity options, and dedicated, isolated compute and storage.

### "Where is our child's data stored?"

> "Learning data is stored on Google's infrastructure through Google Workspace, or Google Cloud for larger deployments. Google operates data centers worldwide with industry-leading physical and digital security, and your child's data never leaves that secure environment. For schools that must keep data in a specific country or region (EU, or LATAM under laws like Chile's Ley 21.719), regional data residency is available on request."

### "Can EduAsiste staff read my child's work?"

> "We access learning data only when a parent, school, or tutor asks us for technical support. We do not routinely read, review, or analyze your child's work. It is never used to train AI models and never shared with other families, students, or schools."

### "What happens if we cancel?"

> "You own your data. You can export everything at any time in standard formats (JSON, Markdown, CSV). When you cancel, we delete the data from our systems within 30 days, and you keep any exports you've made. For family-owned accounts, the data belongs to the family and is portable: it goes with you."

---

## Education Privacy & Compliance

### "Is my child's data used to train AI models?"

> "No. Your child's learning data is never used to train public AI models. Eduardo learns from THEIR work to help THEM. That knowledge stays inside their own private workspace, isolated from every other learner, and is never shared externally. Data isolation per learner is the foundation of how the platform is built."

### "Can other students see my child's work?"

> "No. Each learner has their own private workspace, isolated from one another. In a school (Org) setup, the people who can see a learner's workspace are exactly the assigned teacher/mentor and the learner. No other students. One child cannot browse, read, or stumble into another child's work."

### "What about COPPA / children under 13?"

> "COPPA governs the online collection of personal information from US children under 13, and it requires verifiable parental (or, in the school context, school) consent. EduAsiste's posture:
> - A child under 13 is onboarded by a parent or by the school acting on the parent's behalf, not by self-signup.
> - We collect only what the learning experience needs; there is no advertising and no behavioral profiling of children.
> - A child's data is never sold, never used for ad targeting, and never used to train AI models.
> - The parent is the account owner and can always see what data exists and what their child is doing. Formal COPPA documentation and signed agreements are being built in-house and are in progress."

### "Are you FERPA compliant?"

> "FERPA governs US student education records and gives parents (and eligible students) rights over those records. EduAsiste is built to help a school meet its FERPA obligations rather than to replace them:
> - **Data isolation** keeps each student's records separate.
> - **Encryption** (TLS 1.3 in transit, AES-256 at rest) protects records in motion and at rest.
> - **Export and deletion on request** support a parent's right to access and a school's right to control records.
> - In a school (Org) deployment, the school is the data controller and EduAsiste acts as a service provider under the school's direction. Formal FERPA audit documentation and a signed agreement are being built in-house and are in progress. We do not overstate certifications we don't hold. We give you the controls today and the paperwork path as it's finalized."

### "What about GDPR or data residency (EU / LATAM schools)?"

> "For schools governed by GDPR (EU) or GDPR-aligned laws (for example, Chile's Ley 21.719 (LPDP), which takes effect 1 December 2026 and adds special protections for minors' data), the formal frameworks (Data Processing Agreements, regional data residency in the EU or LATAM, right-to-erasure handling, and the audit trail your data-protection officer needs) are being built in-house and are in progress. EduAsiste's standard controls (encryption, no model training on student data, export-on-request, deletion within a billing cycle) already align with the spirit of these laws."

### "Who can see what my child does?"

> "You do. As the account owner, a parent (or the assigned teacher in a school) can read every conversation and see every attempt your child makes. A learner's workspace is private to them and to the people explicitly linked to it, the assigned teacher/mentor and the parent. No other students, and nothing about your child's activity is hidden from you."

### "Does the school own the data, or does the parent?"

> "It depends on how the account is set up, and we keep this explicit so there's no confusion:
> - **Family account**: the data belongs to the family. It's portable, so when you leave, you take it with you.
> - **School (Org) account**: the institution is the data controller, and the data stays with the school the way student records normally do. The parent still has access and transparency rights. Whichever model applies, the access rules are explicit, with no hidden permissions."

---

## Enterprise & Formal Compliance

### "We need a signed FERPA/COPPA agreement, or GDPR/HIPAA/SOC 2 documentation"

> "We understand that districts, multi-school networks, and institutions handling sensitive student data need formal, signed compliance frameworks. EduAsiste's platform gives you the technical controls today: encryption, per-learner isolation, no model training, export and deletion. The formal documentation, signed agreements, and audits are being built in-house and are currently in progress. Tell us your specific requirement and we'll share where it stands and the timeline for your school or district."

**Formal compliance, in progress (in-house):**
- **FERPA / COPPA documentation**: signed agreements, student-data-privacy controls, audit evidence
- **GDPR**: Data Processing Agreements, EU/LATAM data residency, right to erasure, minors-data controls (incl. Ley 21.719 alignment)
- **HIPAA**: BAA agreements and audit controls (for orgs that also handle health data, e.g. school health programs)
- **SOC 2 Type II**: formal auditing, compliance reports, control frameworks
- **Role-based access control**: district/school permission structures
- **Advanced audit logging**: detailed access logs, compliance reporting
- **Dedicated environments**: isolated infrastructure for regulated student records

### "When will formal compliance be ready?"

> "It's actively in progress. The technical controls behind these frameworks (encryption, per-learner isolation, no model training, export and deletion) are in place today. The formal certifications, signed agreements, and audit documentation are being finalized in-house. Tell us which framework you need and we'll give you the current status and the expected timeline for your school or district."

---

## Common Security Questions

### "What about the AI provider behind Eduardo?"

> "When your child's Eduardo works through a problem, it sends the relevant conversation context to the AI provider (Anthropic's Claude). However:
> - Only the current conversation context is sent, not your child's entire learning history.
> - Anthropic does not train on API data (per their data usage policy).
> - We use enterprise API tiers with additional data protections.
> - For schools with maximum-security or residency needs, we can configure dedicated/private AI endpoints."

### "What if there's a data breach?"

> "Google has industry-leading breach detection and response. In the unlikely event of a breach affecting your child's data, you would be notified according to Google's policies and any applicable laws. Formal incident-response procedures, breach-notification SLAs, and regulatory breach-reporting (GDPR's 72-hour notification, FERPA and state student-privacy breach rules) are part of the in-house compliance program currently in progress."

### "Can a teacher see only their own students?"

> "Yes. A teacher/mentor sees the workspaces of the learners assigned to them and the shared space. They cannot see other students' private workspaces or other classes. Granular, district-wide role-based access (where different staff see different scopes within the same system) is part of the in-house roadmap and is in progress."

### "Do you have a security certification?"

> "We inherit Google Workspace's certifications, which include SOC 1/2/3, ISO 27001, and more. See Google's compliance page for the full list. For education specifically, our standard posture gives you the technical controls behind FERPA and COPPA today. Our own formal certifications (SOC 2 Type II) and the signed FERPA/COPPA/GDPR/HIPAA documentation are being built in-house and are in progress; we can share current status for your audit."

---

## Security Conversation Flow

### Step 1: Understand Their Needs

Ask: "What are your main concerns about your child's data, or your students' data?"

Listen for:
- General "is my kid's data safe?" worry → Standard offering + full visibility for the parent
- "Other kids can't see my child's work, right?" → Per-learner isolation
- "Is it used to train AI?" → No, data isolation, never trains models
- Specific framework mentions (FERPA, COPPA, GDPR, Ley 21.719) → Standard controls today + formal docs in progress (in-house)
- District / multi-school role-based access or audit needs → In-house roadmap, in progress; share current status and timeline

### Step 2: Position Appropriately

**For Parents / Tutors / Small Schools:**
> "The standard platform encrypts everything, keeps your child's data isolated from every other learner, never trains AI on it, and gives you, the account owner, full visibility into everything your child does. That covers what almost every family and small school needs."

**For Schools / Districts with Formal Requirements:**
> "For FERPA, COPPA, GDPR, or data-residency requirements that need signed agreements and audit evidence, those frameworks are being built in-house and are in progress. Tell me the specific requirement and I'll get you the current status and timeline..."

### Step 3: Handle Formal Requirements (if needed)

If a formal framework is required:
1. Acknowledge their requirements are valid and important (student data deserves it)
2. Be clear about what's available today (technical controls) vs in progress (formal docs/certifications)
3. Capture the specific framework and deadline they need
4. Get them a current status and expected timeline from the team
5. Emphasize this gives them best-in-class learning now, with audit-ready data protection on a defined path

---

## Objection Handling

### "Why should we trust a startup with our children's data?"

> "You're not trusting us with the data infrastructure. You're trusting Google. We built EduAsiste on Google Workspace specifically because we knew parents and schools would (rightly) worry about children's data. Your child's data sits on the same infrastructure that schools and Fortune 500 companies trust with their most sensitive records. On top of that, you're the account owner, with full visibility into everything your child does, so nothing happens in the dark."

### "Our school's IT / data-protection officer will never approve this."

> "Good. They should be careful with student data. Here's what usually helps:
> 1. We can provide Google Workspace's security documentation
> 2. For FERPA, COPPA, GDPR, or residency needs, we can share where our formal documentation stands and the timeline
> 3. We're happy to do a technical call with your IT or DPO
> 4. We can start with a small, non-sensitive pilot to build confidence"

### "We need everything to stay in our country / on our own servers."

> "True on-premise isn't something we offer directly. The platform is cloud-native. But regional data residency (EU or LATAM) and private-cloud options can be configured to meet many such requirements while you still use EduAsiste. For schools under laws like Chile's Ley 21.719, that's exactly the path. Would it help to explore that?"

### "We need formal compliance now, not 'in progress.'"

> "Fair, and we won't pretend otherwise. The technical controls (encryption, per-learner isolation, no model training, export and deletion) are in place today. The formal certifications and signed agreements are being finalized in-house. If you have a hard deadline, tell us the framework and the date, and we'll give you an honest status and timeline so you can decide. For most families and small schools, the standard Google Workspace security plus full parent visibility is already more than enough."

---

## Security Summary Table

| Question | Answer |
|----------|--------|
| Where is the data stored? | Google Workspace, or Google Cloud for larger deployments |
| Is the data encrypted? | Yes (TLS 1.3 in transit + AES-256 at rest) |
| Used to train AI? | Never |
| Can other students see it? | No, isolated per learner |
| FERPA? | Technical controls today; formal documentation in progress (in-house) |
| COPPA (under 13)? | Parent/school consent, no profiling; formal documentation in progress (in-house) |
| GDPR / residency? | Aligned controls today; DPAs and EU/LATAM residency in progress (in-house) |
| Who can view my child's work? | The account owner (parent) and the assigned teacher; private to the learner otherwise |
| Role-based access? | Workspace-level today (teacher sees own learners); district IAM in progress |
| Audit logging? | Basic today; comprehensive logging in progress (in-house) |
| Cost | Standard security included |
