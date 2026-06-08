# EduAsiste Security FAQ

> _EduAsiste education-market variant of the ProAsiste security FAQ (product-research #16). Authored 2026-06-08._

Answers to the security and privacy questions that parents, schools, and tutors ask before trusting EduAsiste with student data. EduAsiste runs on the same **Knowledge** platform as ProAsiste — the difference here is the audience: your child's data, and the rules that protect children's records.

---

## Quick Reference

| Tier | Infrastructure | Security Level |
|------|----------------|----------------|
| **SILVER** | Google Workspace | Standard education security |
| **GOLD** | Google Workspace | Standard education security |
| **PLATINUM** | Google Cloud | Enhanced cloud security |
| **DIAMOND** | Google Cloud | Enhanced cloud security |

| Privacy / Compliance Need | Solution | Provider |
|---------------------------|----------|----------|
| FERPA (US student education records) | How-we-help framework + data isolation/encryption | EduAsiste standard; formal documentation via KloudStax |
| COPPA (US children under 13) | Parental-consent posture + no model training on student data | EduAsiste standard; formal documentation via KloudStax |
| GDPR / data residency (EU & LATAM schools) | KloudStax partnership | KloudStax (separate contract) |
| HIPAA / SOC 2 (orgs that also need them) | KloudStax partnership | KloudStax (separate contract) |
| Role-based access (school/district IAM) | KloudStax partnership | KloudStax (separate contract) |

> **Plain-language note for parents:** "Standard security" already encrypts everything, keeps your child's data separate from every other learner's, and never feeds it to AI training. The KloudStax column is for schools and districts that need a signed contract and formal audit paperwork to satisfy their lawyers — not something a single family normally needs.

---

## Standard Security (Included by Tier)

### SILVER & GOLD Tiers: Google Workspace Security

> "SILVER and GOLD tiers store learning data on Google Workspace — the same enterprise-grade infrastructure that protects millions of students and teachers worldwide through Google for Education, Gmail, Google Drive, and Google Docs."

**What's Included:**
- **Encryption in transit**: TLS 1.3 for all data moving between your child and the platform
- **Encryption at rest**: AES-256 encryption for stored learning data
- **Google Workspace infrastructure**: the proven platform schools already trust
- **Data isolation per learner**: each child's twin is separate from every other learner's twin
- **Access control**: token-based authentication
- **Automatic backups**: Google's redundant storage systems

**Best For:**
- Individual families and homeschoolers
- Tutors working with a handful of students
- Small schools without a formal data-protection officer
- Families and schools already using Google for Education

---

### PLATINUM & DIAMOND Tiers: Google Cloud Security

> "PLATINUM and DIAMOND tiers run on Google Cloud Platform for enhanced security and scale — the right fit for a department, a whole school, or a multi-school sostenedor handling many students' records."

**What's Included (in addition to standard):**
- **Google Cloud Platform infrastructure**: enterprise-grade cloud
- **Enhanced monitoring**: cloud-native security monitoring
- **Scalability**: handles whole-school and multi-school cohorts
- **Advanced networking**: VPC, private connectivity options
- **Dedicated resources**: isolated compute and storage

**Best For:**
- Departments and whole schools
- Tutoring centers and learning networks with many students
- Institutions with heavier reporting and data-processing needs
- Schools planning to scale across grades or campuses

### "Where is our child's data stored?"

> "Learning data is stored on Google's infrastructure through Google Workspace (or Google Cloud on higher tiers). Google operates data centers worldwide with industry-leading physical and digital security, and your child's data never leaves that secure environment. For schools that must keep data in a specific country or region (EU, or LATAM under laws like Chile's Ley 21.719), KloudStax can configure regional data residency."

### "Can EduAsiste staff read my child's work?"

> "We access learning data only when a parent, school, or tutor asks us for technical support. We do not routinely read, review, or analyze your child's work. It is never used to train AI models and never shared with other families, students, or schools."

### "What happens if we cancel?"

> "You own your data. You can export everything at any time in standard formats (JSON, Markdown, CSV). When you cancel, we delete the data from our systems within 30 days, and you keep any exports you've made. For PRO (family-owned) learner twins, the data belongs to the family and is portable — it goes with you."

---

## Education Privacy & Compliance

### "Is my child's data used to train AI models?"

> "No. Your child's learning data is never used to train public AI models. Their EduAsiste twin learns from THEIR work to help THEM — that knowledge stays inside their own twin, isolated from every other learner, and is never shared externally. Data isolation per learner is the foundation of how the platform is built."

### "Can other students see my child's work?"

> "No. Each learner has their own twin, and twins are isolated from one another. In a school (Org) setup, the people who can see a learner's workspace are exactly the assigned teacher/mentor and the learner — never other students. One child cannot browse, read, or stumble into another child's work."

### "What about COPPA / children under 13?"

> "COPPA governs the online collection of personal information from US children under 13, and it requires verifiable parental (or, in the school context, school) consent. EduAsiste's posture:
> - A child under 13 is onboarded by a parent or by the school acting on the parent's behalf — never self-signup.
> - We collect only what the learning experience needs; there is no advertising and no behavioral profiling of children.
> - A child's data is never sold, never used for ad targeting, and never used to train AI models.
> - The transparency model (below) means a child and their parent can always see what data exists and who has looked at it.
> For schools that need formal COPPA documentation and a signed agreement, KloudStax provides it."

### "Are you FERPA compliant?"

> "FERPA governs US student education records and gives parents (and eligible students) rights over those records. EduAsiste is built to help a school meet its FERPA obligations rather than to replace them:
> - **Data isolation** keeps each student's records separate.
> - **Encryption** (TLS 1.3 in transit, AES-256 at rest) protects records in motion and at rest.
> - **Export and deletion on request** support a parent's right to access and a school's right to control records.
> - In a school (Org) deployment, the school is the data controller and EduAsiste acts as a service provider under the school's direction.
> For a signed agreement and formal FERPA audit documentation, we work with KloudStax. We do not overstate certifications we don't hold — we give you the controls and the paperwork path to satisfy your obligations."

### "What about GDPR or data residency (EU / LATAM schools)?"

> "For schools governed by GDPR (EU) or GDPR-aligned laws — for example Chile's Ley 21.719 (LPDP), which takes effect 1 December 2026 and adds special protections for minors' data — we partner with KloudStax. They provide Data Processing Agreements, regional data residency (EU or LATAM), right-to-erasure handling, and the audit trail your data-protection officer needs. EduAsiste's standard controls (encryption, no model training on student data, export-on-request, deletion within a billing cycle) already align with the spirit of these laws; KloudStax provides the formal, signed framework."

### "Who can see what my child does? (Transparency)"

> "This is the heart of EduAsiste, and it's a real differentiator: **full transparency, built in.** Every time a parent or teacher looks at a child's data, the child can see that it happened. There is no secret surveillance — trust is the product. Your child always knows who has viewed their learning, and you always know what data exists. We don't believe in watching kids from behind a one-way mirror."

### "Does the school own the data, or does the parent?"

> "It depends on how the twin is set up, and we keep this explicit so there's no confusion:
> - **Family (PRO) learner twin** — the data belongs to the family. It's portable: when you leave, you take it with you.
> - **School (Org) learner twin** — the institution is the data controller, and the data stays with the school the way student records normally do. The parent still has access and transparency rights, and the child can still see who views their work.
> Whichever model applies, the access rules are visible to everyone involved — no hidden permissions."

---

## Enterprise & Formal Compliance (KloudStax Partnership)

### "We need a signed FERPA/COPPA agreement, or GDPR/HIPAA/SOC 2 documentation"

> "We understand that districts, multi-school sostenedores, and institutions handling sensitive student data need formal, signed compliance frameworks. EduAsiste's standard platform gives you the technical controls — encryption, per-learner isolation, no model training, export and deletion. For the formal documentation, signed agreements, and audits, we've partnered with KloudStax. Compliance is their core expertise, not ours. They provide the controls and paperwork your school's lawyers and data-protection officer need."

**What KloudStax Provides:**
- **FERPA / COPPA documentation**: signed agreements, student-data-privacy controls, audit evidence
- **GDPR compliance**: Data Processing Agreements, EU/LATAM data residency, right to erasure, minors-data controls (incl. Ley 21.719 alignment)
- **HIPAA compliance**: BAA agreements, audit controls (for orgs that also handle health data, e.g. school health programs)
- **SOC 2 Type II**: formal auditing, compliance reports, control frameworks
- **Role-based access control**: Google IAM integration, district/school permission structures
- **Advanced audit logging**: detailed access logs, compliance reporting
- **Dedicated environments**: isolated infrastructure for regulated student records

**How It Works:**
1. Tell us your privacy / compliance requirements (FERPA, COPPA, GDPR, residency, etc.)
2. We work with KloudStax to create a quick-turn proposal
3. You receive an addendum to your EduAsiste contract covering the additional services
4. KloudStax provisions and manages your compliant environment
5. EduAsiste runs on that KloudStax-managed infrastructure

**Pricing:**
- KloudStax services are added as a contract addendum
- Pricing based on your specific requirements
- Quick turnaround — no lengthy separate procurement process

### "Why don't you handle formal compliance directly?"

> "We believe in doing what we do best — building the best possible learning twin for each child. Formal education-privacy compliance requires specialized expertise, dedicated resources, and ongoing certification maintenance. Rather than do that poorly ourselves, we've partnered with KloudStax, who does it excellently. You get best-in-class learning AND best-in-class, audit-ready data protection."

### "Can we talk to KloudStax?"

> "Absolutely. We've set up a quick-turn proposal process with KloudStax. We can get you an addendum to your EduAsiste contract that meets any additional privacy, residency, or infrastructure needs your school or district has — no lengthy separate procurement process."

---

## Common Security Questions

### "What about the AI provider behind the twin?"

> "When your child's EduAsiste twin works through a problem, it sends the relevant conversation context to the AI provider (Anthropic's Claude). However:
> - Only the current conversation context is sent — not your child's entire learning history.
> - Anthropic does not train on API data (per their data usage policy).
> - We use enterprise API tiers with additional data protections.
> - For schools with maximum-security or residency needs, KloudStax can configure dedicated/private AI endpoints."

### "What if there's a data breach?"

**Standard (Google Workspace / Google Cloud):**
> "Google has industry-leading breach detection and response. In the unlikely event of a breach affecting your child's data, you would be notified according to Google's policies and any applicable laws."

**Enterprise (KloudStax):**
> "KloudStax provides formal incident-response procedures, breach-notification SLAs, and compliance with specific regulatory breach-reporting rules (GDPR's 72-hour notification, FERPA/state student-privacy breach rules, etc.)."

### "Can a teacher see only their own students?"

**Standard:**
> "Our standard offering provides twin-level access. A teacher/mentor sees the workspaces of the learners assigned to them and the shared space — never other students' private workspaces, and never other classes."

**Enterprise (KloudStax):**
> "For granular, district-wide role-based access — where different staff see different scopes within the same system — KloudStax can implement Google IAM integration with custom permission structures."

### "Do you have a security certification?"

**Standard:**
> "We inherit Google Workspace's certifications, which include SOC 1/2/3, ISO 27001, and more. See Google's compliance page for the full list. For education specifically, our standard posture gives you the technical controls behind FERPA and COPPA, not a standalone certificate."

**Enterprise:**
> "KloudStax maintains their own SOC 2 Type II certification and can provide compliance documentation for FERPA, COPPA, GDPR, HIPAA, and other frameworks as needed for your school's audits."

---

## Security Conversation Flow

### Step 1: Understand Their Needs

Ask: "What are your main concerns about your child's — or your students' — data?"

Listen for:
- General "is my kid's data safe?" worry → Standard offering + transparency story
- "Other kids can't see my child's work, right?" → Per-learner isolation
- "Is it used to train AI?" → No, data isolation, never trains models
- Specific framework mentions (FERPA, COPPA, GDPR, Ley 21.719) → Standard controls + KloudStax for formal docs
- District / multi-school role-based access or audit needs → KloudStax

### Step 2: Position Appropriately

**For Parents / Tutors / Small Schools:**
> "Good news — the standard platform encrypts everything, keeps your child's data isolated from every other learner, never trains AI on it, and shows your child every time someone looks at their work. That covers what almost every family and small school needs."

**For Schools / Districts with Formal Requirements:**
> "For FERPA, COPPA, GDPR, or data-residency requirements that need signed agreements and audit evidence, we work with our partner KloudStax. Let me explain how that partnership works..."

### Step 3: Handle the Handoff (if needed)

If KloudStax is needed:
1. Acknowledge their requirements are valid and important — student data deserves it
2. Explain the partnership model
3. Offer to make an introduction
4. Clarify that KloudStax pricing is separate
5. Emphasize this gives them best-in-class for both learning AND data protection

---

## Objection Handling

### "Why should we trust a startup with our children's data?"

> "You're not trusting us with the data infrastructure — you're trusting Google. We built EduAsiste on Google Workspace specifically because we knew parents and schools would (rightly) worry about children's data. Your child's data sits on the same infrastructure that schools and Fortune 500 companies trust with their most sensitive records. On top of that, our transparency model means nothing happens to your child's data in the dark — they see every view."

### "Our school's IT / data-protection officer will never approve this."

> "Good — they should be careful with student data. Here's what usually helps:
> 1. We can provide Google Workspace's security documentation
> 2. For FERPA, COPPA, GDPR, or residency needs, KloudStax can provide formal, signed documentation
> 3. We're happy to do a technical call with your IT or DPO
> 4. We can start with a small, non-sensitive pilot to build confidence"

### "We need everything to stay in our country / on our own servers."

> "True on-premise isn't something we offer directly — the platform is cloud-native. But KloudStax can configure regional data residency (EU or LATAM) and private-cloud options that may meet your requirement while you still use EduAsiste. For schools under laws like Chile's Ley 21.719, that's exactly the path. Would it help to explore that with them?"

### "KloudStax adds too much cost / complexity for us."

> "For most families and small schools, the standard Google Workspace security plus our transparency model is more than enough. KloudStax is really for institutions with specific regulatory mandates — districts, multi-school sostenedores, EU/LATAM data residency, formal audit requirements. If you don't have those mandates, you likely don't need KloudStax."

---

## Security Summary Table

| Question | Standard Answer | Enterprise Answer |
|----------|-----------------|-------------------|
| Where is the data stored? | Google Workspace / Google Cloud | KloudStax-managed environment |
| Is the data encrypted? | Yes (TLS 1.3 + AES-256) | Yes + additional controls |
| Used to train AI? | Never | Never |
| Can other students see it? | No — isolated per learner | No — isolated per learner |
| FERPA? | Technical controls to help you comply | Full signed docs (KloudStax) |
| COPPA (under 13)? | Parent/school consent, no profiling | Full signed docs (KloudStax) |
| GDPR / residency? | Aligned controls | Full + EU/LATAM residency (KloudStax) |
| Who can view my child's work? | Assigned teacher + parent — child sees every view | Same + district IAM scoping (KloudStax) |
| Role-based access? | Twin-level (teacher sees own learners) | Full IAM (KloudStax) |
| Audit logging? | Basic | Comprehensive (KloudStax) |
| Cost | Included | Separate KloudStax contract |

---

## KloudStax Contact

For formal education-privacy and compliance inquiries:
- **Partner**: KloudStax
- **Services**: FERPA / COPPA documentation, GDPR, data residency (EU/LATAM), HIPAA, SOC 2, IAM, dedicated environments
- **Engagement**: Direct contract with KloudStax (addendum to your EduAsiste contract)
- **Introduction**: Contact your EduAsiste sales rep for a warm introduction
