# 🚀 FIR Intelligence and Crime Pattern Detector

> ⚠️ **Replace everything in `[ ]` brackets with your actual content before submission.**

---

## 👥 Team

| Field | Value |
|---|---|
| **Team Name** | [Kasukabe_Defense_Group] |
| **Track** | [Intelligence, Prediction & Pattern Detection] |
| **Team Lead** | [Shreyanshi Dixit] — [shreyanshid07@gmail.com] |
| **Members** | [Flora], [Jeeshu Dutta], [Srishti Nidhi Dangwar] |

---

## 🎯 Problem Statement

> In 2–3 sentences: What problem does your project solve? Who experiences this problem?

[UP Police's CCTNS system holds 3+ crore digitized FIRs but has no NLP layer. Serial offenders such as the Jamtara gang evaded detection for years because inter-district FIR connections were never surfaced, and pattern analysis is entirely manual.

Objective: Build a Bob-powered NLP intelligence tool that ingests batches of FIR data and:

Categorizes each FIR by crime type
Extracts named entities (accused, location, MO, victim profile)
Detects repeat-offender signatures across FIRs
Generates a station-level crime trend summary with a flagged repeat-offender list]

---

## 💡 Solution

> In 2–3 sentences: What did you build? How does it solve the problem above?

[Our Bob-powered tool ingests FIRs from JSON and Excel files, validates them, and uses NLP to classify crimes, extract entities, and generate summaries and keywords. Records are stored in SQL and vector databases, enabling repeat-offender detection, cross-district FIR linking, and pattern analysis, all surfaced through a dashboard and an Ask AI assistant.]

---

## ✨ Key Features

- **Feature 1:** [Multi-source FIR ingestion from JSON and Excel files, converted into one standard structure with automated validation]
- **Feature 2:** [Bob-powered NLP that classifies crime type, extracts entities (accused, victim, location, phones, vehicles) and generates a summary and top 10 keywords for every FIR.]
- **Feature 3:** [Repeat-offender detection and cross-district FIR linking, with fuzzy name matching and a reason and confidence score for each link.]
- **Feature 4:** [Crime pattern analysis with a station-level trend summary and automatic alerts for offender matches and crime spikes.]
- **Feature 5:** [Ask AI assistant that answers plain-language questions using context retrieved from both the SQL and vector databases, citing FIR numbers.]

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Languages** | [e.g., Python, TypeScript] |
| **Frameworks** | [e.g., FastAPI, React] |
| **IBM Technologies** | [e.g., watsonx.ai, IBM Bob, IBM Cloud] |
| **Databases** | [e.g., PostgreSQL, Redis] |
| **Other** | [e.g., Docker, GitHub Actions] |

---

## 📁 Repository Structure

```
├── src/                  # All source code
├── docs/                 # Written documentation
│   ├── problem-statement.md
│   ├── solution-overview.md
│   ├── architecture.md
│   └── setup-guide.md
├── demo/                 # Demo artifacts
│   ├── screenshots/      # App screenshots
│   └── demo-video-link.txt  # Link to demo video
├── presentation/         # Slide deck
└── submission.yaml       # Structured submission metadata
```

---

## ⚡ How to Run

> **Copy these exact steps from your [`docs/setup-guide.md`](docs/setup-guide.md)**

```bash
# 1. Clone the repo
git clone https://github.com/[your-repo].git
cd [your-repo]

# 2. Install dependencies
[your install command here]

# 3. Configure environment
cp .env.example .env
# Edit .env with your values

# 4. Run the project
[your run command here]
```

---

## 🖥️ Demo

| Artifact | Link |
|---|---|
| 📹 Demo Video | [See demo/demo-video-link.txt](demo/demo-video-link.txt) |
| 🌐 Live Demo | [See demo/live-demo-url.txt](demo/live-demo-url.txt) |
| 🖼️ Screenshots | [See demo/screenshots/](demo/screenshots/) |
| 📊 Presentation | [See presentation/slides.pdf](presentation/) |

---

## ⚠️ Known Limitations

> Be honest — judges appreciate transparency over overclaiming.

- [Limitation 1: e.g., "Authentication is mocked — not production-ready"]
- [Limitation 2: e.g., "Only tested on Chrome"]
- [Limitation 3: e.g., "Feature X is scaffolded but not fully implemented"]

---

## 🏅 What We're Most Proud Of

[Tell the judges what part of your submission is strongest and worth paying close attention to.]

---
