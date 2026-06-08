
# ProAsiste Security FAQ

Answers to common security questions from prospects.

---

## Quick Reference

| Tier | Infrastructure | Security Level |
|------|----------------|----------------|
| **SILVER** | Google Workspace | Standard business security |
| **GOLD** | Google Workspace | Standard business security |
| **PLATINUM** | Google Cloud | Enhanced cloud security |
| **DIAMOND** | Google Cloud | Enhanced cloud security |

| Compliance Need | How ProAsiste Handles It | Status |
|-----------------|--------------------------|--------|
| GDPR compliance | Encryption, no model training, export/deletion on request; EU data residency on request | In progress (in-house) |
| HIPAA compliance | Control framework, audit controls, BAA path | In progress (in-house) |
| SOC 2 compliance | Control framework and audit evidence | In progress (in-house) |
| Role-based access (IAM) | Twin-level access today; granular IAM scoping | In progress (in-house) |

---

## Standard Security (Included by Tier)

### SILVER & GOLD Tiers: Google Workspace Security

> "SILVER and GOLD tiers use Google Workspace for data storage and security. Your data sits on the same enterprise-grade infrastructure that protects millions of Google Workspace users worldwide. It's the same infrastructure behind Gmail, Google Drive, and Google Docs."

**What's Included:**
- **Encryption in transit**: TLS 1.3 for all data transmission
- **Encryption at rest**: AES-256 encryption for stored data
- **Google Workspace infrastructure**: Proven, trusted platform
- **Data isolation**: Your twin's data is separate from other customers
- **Access control**: Token-based authentication
- **Automatic backups**: Google's redundant storage systems

**Best For:**
- Individual professionals
- Small businesses
- Teams without specific compliance requirements
- Companies already using Google Workspace

---

### PLATINUM & DIAMOND Tiers: Google Cloud Security

> "PLATINUM and DIAMOND tiers run on Google Cloud Platform for enhanced security capabilities. This provides additional controls, better scalability, and more sophisticated infrastructure options."

**What's Included (in addition to standard):**
- **Google Cloud Platform infrastructure**: Enterprise-grade cloud
- **Enhanced monitoring**: Cloud-native security monitoring
- **Scalability**: Enterprise-level performance
- **Advanced networking**: VPC, private connectivity options
- **Dedicated resources**: Isolated compute and storage

**Best For:**
- Larger teams and departments
- Organizations with heavier data processing needs
- Companies requiring enhanced cloud capabilities
- Businesses planning significant scale

### "Where is our data stored?"

> "Your data is stored on Google's infrastructure through Google Workspace. Google operates data centers worldwide with industry-leading physical and digital security. Your data never leaves Google's secure environment."

### "Can you access our data?"

> "We can access your data only for technical support purposes when you request assistance. We do not routinely access, review, or analyze customer data. Your data is never used to train AI models or shared with other customers."

### "What happens if we cancel?"

> "You own your data. You can export everything at any time in standard formats (JSON, Markdown, CSV). When you cancel, we delete your data from our systems within 30 days. You retain any exports you've made."

---

## Enterprise & Formal Compliance

### "We need GDPR/HIPAA/SOC 2 compliance"

> "We understand that enterprises and regulated industries have specific compliance requirements. ProAsiste's platform gives you the technical controls today: encryption, data isolation, no model training, export and deletion. The formal documentation, signed agreements, and audits are being built in-house and are currently in progress. Tell us your specific requirement and we'll share where it stands and the timeline."

**Formal compliance, in progress (in-house):**
- **GDPR compliance**: Data processing agreements, EU data residency, right to erasure
- **HIPAA compliance**: BAA agreements, PHI handling, audit controls
- **SOC 2 Type II**: Formal auditing, compliance reports, control frameworks
- **Role-based access control**: Google IAM integration, granular permissions
- **Advanced audit logging**: Detailed access logs, compliance reporting
- **Dedicated environments**: Isolated infrastructure for regulated data

### "When will formal compliance be ready?"

> "It's actively in progress. The technical controls behind these frameworks (encryption, data isolation, no model training, export and deletion) are in place today. The formal certifications, signed agreements, and audit documentation are being finalized in-house. Tell us which framework you need and we'll give you the current status and the expected timeline for your organization."

### "Why don't you handle compliance directly?"

> "We do, in-house. We focus on building the best possible twin for your business, and formal compliance is part of that work, not something we hand off. The technical controls are in place today; the specialized expertise, dedicated resources, and ongoing certification maintenance behind the formal documentation are being built in-house and are in progress. You get strong AI capabilities and a defined path to audit-ready security."

---

## Common Security Questions

### "Do you train AI models on our data?"

> "No. Your data is never used to train public AI models. Your ProAsiste learns from YOUR data to serve YOU. That knowledge stays within your twin and is never shared externally."

### "What about the AI provider (Claude/OpenAI)?"

> "When your ProAsiste processes queries, it sends prompts to the AI provider (Anthropic's Claude). However:
> - Only the current conversation context is sent, not your entire knowledge base
> - Anthropic does not train on API data (per their data usage policy)
> - We use enterprise API tiers with additional data protections
> - For maximum security needs, we can configure dedicated/private AI endpoints"

### "What if there's a data breach?"

> "Google has industry-leading breach detection and response. In the unlikely event of a breach affecting your data, you would be notified according to Google's policies and any applicable laws. Formal incident-response procedures, breach-notification SLAs, and compliance with specific regulatory breach-reporting requirements (GDPR's 72-hour notification, HIPAA breach rules, etc.) are part of the in-house compliance program currently in progress."

### "Can employees access only what they should?"

> "Our standard offering provides twin-level access control. Either someone has access to the twin or they don't. For Org-twins, we support mentor oversight of user workspaces. Granular role-based access control (where different users see different data within the same system, via Google IAM integration with custom permission structures) is part of the in-house roadmap and is in progress."

### "Do you have a security certification?"

> "We inherit Google Workspace's certifications, which include SOC 1/2/3, ISO 27001, and more. See Google's compliance page for the full list. Our own formal certifications (SOC 2 Type II) and compliance documentation for GDPR, HIPAA, and other frameworks are being built in-house and are in progress; we can share current status for your audit."

---

## Security Conversation Flow

### Step 1: Understand Their Needs

Ask: "What are your main security concerns or requirements?"

Listen for:
- General data protection concerns → Standard offering
- Specific compliance mentions (GDPR, HIPAA, SOC 2) → Standard controls today + formal docs in progress (in-house)
- Role-based access needs → In-house roadmap, in progress
- Audit/documentation requirements → In-house roadmap, in progress; share current status and timeline

### Step 2: Position Appropriately

**For Standard Needs:**
> "Our standard platform runs on Google Workspace's security infrastructure, which provides enterprise-grade protection out of the box. This includes encryption, access controls, and Google's world-class security operations."

**For Enterprise Needs:**
> "For GDPR, HIPAA, SOC 2, or role-based access requirements that need signed agreements and audit evidence, those formal frameworks are being built in-house and are in progress. Tell me the specific requirement and I'll get you the current status and timeline..."

### Step 3: Handle Formal Requirements (if needed)

If a formal framework is required:
1. Acknowledge their requirements are valid and important
2. Be clear about what's available today (technical controls) vs in progress (formal docs/certifications)
3. Capture the specific framework and deadline they need
4. Get them a current status and expected timeline from the team
5. Emphasize this gives them best-in-class AI now, with audit-ready security on a defined path

---

## Objection Handling

### "Why should we trust a startup with our data?"

> "You're not trusting us with your data infrastructure. You're trusting Google. We built ProAsiste on Google Workspace specifically because we knew security would be a concern. Your data sits on the same infrastructure that Fortune 500 companies trust with their most sensitive information."

### "Our IT team will never approve this."

> "I understand IT teams are cautious, and they should be. Here's what usually helps:
> 1. We can provide Google Workspace's security documentation
> 2. For specific compliance needs, we can share where our formal documentation stands and the timeline
> 3. We're happy to do a technical call with your IT team
> 4. We can start with a non-sensitive pilot to build confidence"

### "We need everything on-premise."

> "True on-premise deployment isn't something we offer directly. Our platform is cloud-native. However, regional data residency and private-cloud options can be configured to meet many such requirements while you still use ProAsiste. Would it be helpful to explore that?"

### "We need formal compliance now, not 'in progress.'"

> "Fair, and we won't pretend otherwise. The technical controls (encryption, data isolation, no model training, export and deletion) are in place today. The formal certifications and signed agreements are being finalized in-house. If you have a hard deadline, tell us the framework and the date, and we'll give you an honest status and timeline so you can decide. For most customers, the standard Google Workspace security is already more than sufficient; formal frameworks are really for organizations with specific regulatory mandates: healthcare, finance, government contractors, EU data residency, etc."

---

## Security Summary Table

| Question | Answer |
|----------|--------|
| Where is data stored? | Google Workspace, or Google Cloud for larger deployments |
| Is data encrypted? | Yes (TLS 1.3 in transit + AES-256 at rest) |
| GDPR compliant? | Aligned controls today; DPAs and EU residency in progress (in-house) |
| HIPAA compliant? | Technical controls today; BAA and audit docs in progress (in-house) |
| SOC 2 certified? | Inherited from Google today; own SOC 2 Type II in progress (in-house) |
| Role-based access? | Twin-level today; full IAM in progress (in-house) |
| Audit logging? | Basic today; comprehensive logging in progress (in-house) |
| Cost | Standard security included |

