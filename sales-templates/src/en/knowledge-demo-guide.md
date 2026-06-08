
# Knowledge Sales Demo Guide

A comprehensive guide for sales teams to demonstrate, explain, and sell the Knowledge platform (ProAsiste for business, EduAsiste for education).

> **Applies to both brands.** The tabs and flow are identical across ProAsiste and EduAsiste — it's the same Knowledge platform. The examples below use **ProAsiste** (business) scenarios; for **EduAsiste** (education), swap the equivalents: invoices/contracts → worksheets/assignments, supplier/customer → student/parent, operations reports → progress summaries. Brand-specific email, competitive, security, and quick-reference assets live as separate EduAsiste pages on the index.

---

## Quick Reference

| Component | Purpose | Key Selling Point |
|-----------|---------|-------------------|
| **Chat Window** (left) | AI conversation interface | "Talk to your business knowledge" |
| **Import Tab** (default) | Document upload + extraction | "Drop a document, watch it become knowledge" |
| **View Tab** | Knowledge dashboard + Activity Map | "See how everything connects and moves" |
| **Task Tab** | Automated workflows | "Your AI apprentice handles routine work" |
| **Verify Tab** | Approval queue | "You stay in control of what enters your knowledge base" |
| **Obsidian** button | Markdown vault access | "Your knowledge is portable — never locked in" |
| **Neo4j** button | Graph database browser | "Power users can query the graph directly" |

---

## Tab Order: Import | View | Task | Verify

Import is the default tab on load — the first thing a user sees is the document upload zone.

---

## Import Tab (Document Intelligence)

### What It Is
Drag-and-drop document processor that extracts entities, relationships, and events from uploaded files, connecting them to your Knowledge graph.

### Supported Formats
- PDF, DOCX, DOC, TXT, MD (up to 25MB)
- Google Docs and Google Sheets via URL import
- CSV, XLSX spreadsheets

### How to Demo
1. Show the Import tab (it's the default on load)
2. Drag a sample invoice or contract onto the upload zone
3. Show the extraction progress — entities being identified
4. Switch to View tab to see the new Knowledge Notes appear in the Activity Map
5. Ask a question about the document in chat: *"What are the key terms in that contract?"*

### How to Explain
> "Drop any document here, and Knowledge reads it, understands it, and connects it to everything else it knows about your business. That supplier contract you just uploaded? It now links to your previous orders, your risk assessments, and your compliance requirements."

### How to Sell
- **Pain Point**: "How many important documents are sitting in folders, never to be found again?"
- **Solution**: "Every document becomes searchable, connected, and actionable. Knowledge doesn't just store files — it understands them."
- **ROI Hook**: "When you need to find that one clause in a contract from 18 months ago, do you want to spend an hour searching or 10 seconds asking?"

---

## View Tab (Knowledge Dashboard)

### What It Is
The knowledge intelligence dashboard with six sub-views. The default landing is the **Activity Map**.

### Sub-Views

| Button | Purpose |
|--------|---------|
| **Activity Map** | Default — recent events, hot entities, attention items, manual creation |
| **Source Files** | Browse uploaded documents with detail modals |
| **Knowledge Notes** | Browse entity nodes with search, type filter, click-to-edit |
| **KaiLinks** | Browse relationships between entities |
| **KaiEvents** | Browse timestamped micro-events (actor-verb-object) |

### Activity Map (Default Landing)

The Activity Map is the first thing users see when they click View. It shows:

- **+ KaiNote / + KaiLink / + KaiEvent** — manual creation buttons with modal forms
- **Recent Activity** — last 10 KaiEvents showing who did what to whom
- **Hot Entities** — top 8 most-connected Knowledge Notes (clickable chips)
- **Needs Attention** — orphan entities (no connections) and stale entities (14+ days without updates)

### How to Demo
1. Click View tab — Activity Map loads by default
2. Point out Recent Activity: *"These are the latest events extracted from your documents"*
3. Click a Hot Entity chip to open its detail card
4. Show the Needs Attention section: *"Knowledge tells you what needs work"*
5. Click **+ KaiNote** to manually create an entity
6. Click **+ KaiLink** to connect two entities
7. Switch to Knowledge Notes to browse the full entity list
8. Show KaiEvents filtered by verb
9. Resize the sidebar by dragging the left edge

### How to Explain
> "The Activity Map is your knowledge command center. At a glance, you see what's happening, what's important, and what needs attention. It's like a living dashboard of your institutional knowledge."

### How to Sell
- **Pain Point**: "Do you know which parts of your business knowledge are getting stale or disconnected?"
- **Solution**: "Knowledge actively monitors your knowledge graph and surfaces orphans, gaps, and stale data."
- **ROI Hook**: "What if you could prevent knowledge decay before it costs you a deal or a compliance issue?"

---

## Task Tab (AI Apprentice)

### What It Is
An AI-powered task automation system. Users define templates for recurring workflows, and Knowledge executes them.

### How to Demo
1. Show the list of available task templates
2. Click on a task to see its details and parameters
3. Approve a task for execution
4. Show the completed output — reports, spreadsheets, analysis
5. Point out the report download button for generated XLSX/DOCX files

### How to Explain
> "Think of it as training an apprentice. You define the process once — 'Every Monday, pull supplier data, compare to last week, flag anomalies, and write a summary.' Then Knowledge does it automatically, exactly how you taught it."

### How to Sell
- **Pain Point**: "How many hours does your team spend on repetitive reports and data compilation?"
- **Solution**: "Define the task once. Your AI apprentice handles it from then on."
- **ROI Hook**: "If a weekly report takes 3 hours to compile, that's 150+ hours per year. Knowledge does it in minutes."

---

## Verify Tab (Quality Control)

### What It Is
A two-way approval queue that keeps humans in the loop.

### Two Directions
| Direction | Purpose |
|-----------|---------|
| **Incoming** | Review AI-extracted Knowledge Notes before they're committed to the graph |
| **Outgoing** | Review AI-recommended cut candidates (stale, orphan, low-quality) |

### How to Demo
1. Show the incoming queue with pending Knowledge Notes
2. Click to review an entity — show the detail card
3. Approve or reject with one click
4. Switch to Outgoing to show cut candidates
5. Explain the Cut/Retain actions

### How to Explain
> "Knowledge is powerful, but you're always in control. Every piece of knowledge passes through your approval before it enters the graph. And when data gets stale, Knowledge recommends pruning — but you decide what stays and what goes."

### How to Sell
- **Pain Point**: "How do you ensure AI-generated insights are accurate?"
- **Solution**: "Built-in human oversight. Nothing enters your knowledge base without your approval."
- **ROI Hook**: "Compliance teams love this — full audit trail of what was approved, rejected, and by whom."

---

## Demo Flow Checklist (20 minutes)

### Opening (2 minutes)
- [ ] Introduce Knowledge: "Your AI-powered knowledge brain"
- [ ] Show the clean interface — chat left, tabs right
- [ ] Note: Import tab is default — designed for action

### Import Demo (3 minutes)
- [ ] Drag a sample document onto the upload zone
- [ ] Show extraction progress
- [ ] Point out entity count growing

### Chat Demo (3 minutes)
- [ ] Ask a business question about the uploaded document
- [ ] Show source citations in the response
- [ ] Demonstrate follow-up context awareness

### View Tab Demo (5 minutes)
- [ ] Show Activity Map (default landing)
- [ ] Point out Recent Activity, Hot Entities, Needs Attention
- [ ] Click + KaiNote to manually create an entity
- [ ] Browse Knowledge Notes list — click to see detail card
- [ ] Show KaiEvents — filter by verb
- [ ] Resize sidebar by dragging the handle

### Task Tab Demo (3 minutes)
- [ ] Show available task templates
- [ ] Explain the apprentice concept
- [ ] Show a completed task output / report download

### Verify Tab Demo (2 minutes)
- [ ] Show incoming approval queue
- [ ] Approve one KaiNote
- [ ] Mention outgoing cut candidates

### Closing (2 minutes)
- [ ] Summarize: knowledge capture, automation, intelligence, control
- [ ] Address security/privacy: "Your data stays yours — PRO twins push to your own GDrive"
- [ ] Discuss tier options and pricing

---

## Objection Handling

### "We already have a knowledge management system"
> "Great! Knowledge goes beyond storage. It reads your documents, extracts entities, discovers relationships, and builds a living knowledge graph. Your current system stores files — Knowledge understands them."

### "Our data is sensitive"
> "Your Knowledge runs in a dedicated environment. PRO twins push data to your own Google Drive — you own it completely. ORG twins obfuscate PII on shared drives. Your data never trains public AI models."

### "We don't have time to set this up"
> "The initial setup takes about 30 minutes. After that, every document you upload, every conversation you have — it all builds automatically. The system learns from normal use."

### "How is this different from ChatGPT?"
> "ChatGPT knows the internet. Knowledge knows YOUR business. It's trained on your documents, your processes, your data. When you ask about 'our supplier terms,' it gives you YOUR supplier terms, not generic advice."

### "Why not just use Obsidian/Notion/Confluence?"
> "Knowledge actually includes Obsidian — your Knowledge Notes sync to an Obsidian vault you can edit offline. But Knowledge adds the AI layer: automatic extraction, relationship discovery, event tracking, and an AI apprentice that acts on your knowledge. It's Obsidian + Neo4j + AI, working together."

### "What about ROI?"
> "Let's calculate it right now. How many hours per week does your team spend searching for information? Compiling reports? Answering the same questions? Most clients see 5-10 hours per employee per week in productivity gains."

---

## Tier Overview for Sales

All features are visible at every tier. Tiers differ by scale limits only.

| Tier | Monthly | Annual | Users | Doc Extractions | Task Executions | Trial |
|------|---------|--------|-------|-----------------|-----------------|-------|
| **Individual** | $29/mo | $289/yr ($24/mo) | 1 | 3/day | 5/day | 30 days |
| **Team** | $49/mo | $489/yr ($41/mo) | Up to 5 | 10/day | 15/day | 14 days |
| **Discipline** | $79/mo | $787/yr ($66/mo) | Up to 15 | 30/day | 50/day | 7 days |
| **Institution** | $99/mo | $987/yr ($82/mo) | Up to 50 | Unlimited | Unlimited | 3 days |

**Additional seats**: $19/mo ($190/yr) per seat. Mentor seat is always free.

**Trial cascade**: 54-day total experience (Individual 30d → Team 14d → Discipline 7d → Institution 3d). After trial, returns to Individual.

---

## Terminology Cheat Sheet

| Say This | Not This | Why |
|----------|----------|-----|
| Knowledge | Kaigraph, K-Graph | Current product name |
| Knowledge Notes | K-Notes, entities, nodes | Customer-facing term for entity files |
| KaiLinks | K-Links, relationships, rels | Customer-facing term for connections |
| KaiEvents | Events, micro-events | Customer-facing term for timestamped interactions |
| Individual / Team / Discipline / Institution | SILVER / GOLD / PLATINUM / DIAMOND | Display names vs internal codes |
| Import / View / Task / Verify | Load / Build / Update / Archive | Current tab names |
| Activity Map | Chord diagram, dashboard | Default View landing |

---

## Quick Pitch (30 seconds)

> "Knowledge captures everything your business knows — every document, every conversation, every process — and makes it instantly accessible through AI. Drop a document, watch it become connected knowledge. Ask a question, get an answer with sources. Define a task, let your AI apprentice handle it. It's like giving every employee access to your company's complete institutional knowledge, plus an AI assistant who's read all of it."

---

## Domains & Resources

| Resource | ProAsiste (Business) | EduAsiste (Education) |
|----------|-------------------|-------------------|
| Web UI | proasiste.com | eduasiste.org |
| Demo | proasiste.com/chat/ctwin/ | eduasiste.org/chat/ltwin/ |
| Company | AIVP (avaluei.com) | AIAXIA (aiaxia.org) |

