# Zeppelin AI Resume Screener

![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Fellowship](https://img.shields.io/badge/Zeppelin-AI%20Fellowship-purple)

**AI-powered Resume Parser & Feedback Engine**

*Developed as part of the Zeppelin AI & Generative AI Fellowship.*

> **Week 1 — Repository Setup • Git Workflow • Team Collaboration**

---

## Overview

The **Zeppelin AI Resume Screener** is an AI-powered application designed to streamline the recruitment process by parsing resumes, comparing candidate profiles with job descriptions, and generating intelligent feedback using Large Language Models (LLMs).

This repository currently represents the **Week 1** project setup, focusing on repository initialization, team collaboration, Git workflow, and project planning. Core application features will be implemented throughout the upcoming weeks of the fellowship.

### Project Goal

Build an intelligent resume screening platform capable of:

- Parsing resume documents
- Extracting candidate information
- Matching resumes against job descriptions
- Generating AI-powered resume feedback

---

## Repository Workflow

This repository follows the Git workflow defined by the Zeppelin AI & Generative AI Fellowship.

| Branch | Purpose |
| :------ | :------ |
| `main` | Stable production branch (protected) |
| `dev` | Integration branch |
| `feature/frontend-foundation` | Frontend foundation and UI layout branch |
| `feature/ai-engine` | AI engine and LLM integration branch |
| `feature/pdf-utility` | PDF utility and document processing branch |
| `feature/backend-setup` | Backend setup and core API framework branch |

### Current Feature Branches

| Member | Branch |
| :------ | :----- |
| **Suraiba Idrees** *(Team Lead)* | `feature/frontend-foundation` |
| Maryam Imran Shah | `feature/ai-engine` |
| Aniqa Qamar | `feature/pdf-utility` |
| Saboor Khalil | `feature/backend-setup` |

---

## Tech Stack

This project follows the official technology roadmap of the **Zeppelin AI & Generative AI Fellowship**.

### Week 1 Setup

- Git
- GitHub
- Python Virtual Environment (`.venv`)

### Planned Core Stack

#### Frontend

- Next.js

#### Backend

- Python FastAPI

#### Vector Database

- Qdrant *(Required)*
- Pinecone *(Alternative)*

#### Large Language Models (LLMs)

- OpenAI
- Anthropic Claude
- Google Gemini

#### AI Development Tools

- GitHub Copilot
- Cursor
- Claude Code
- Windsurf
- v0 / Bolt

> **Note:** Week 1 focuses on repository setup, Git workflow, collaboration, and project planning. The technologies listed above will be integrated progressively throughout the fellowship according to the official roadmap.

---

## Getting Started

Clone the repository.

```bash
git clone <repository-url>
```

Navigate to the project directory.

```bash
cd zeppelin-ai-resume-screener
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Development Guidelines

- Create a new `feature/feature-name` branch before starting development.
- Commit changes frequently using meaningful commit messages.
- Submit completed work through Pull Requests targeting the `dev` branch.
- Do not push directly to the `main` branch.
- Pull the latest changes from `dev` before beginning new work.

### Example Commit Messages

```text
feat: implement resume upload
feat: add AI engine skeleton
feat: add frontend foundation
fix: resolve PDF parsing issue
docs: update README
```

---

## Current Development

Development tasks are managed through GitHub Issues.

### Active Tasks

- Backend project setup
- AI engine initialization
- PDF utility foundation
- Frontend foundation

Additional issues and milestones will be introduced as the project progresses.

---

## Project Team

| Role | Member |
| :--- | :----- |
| **Team Lead** | Suraiba Idrees |
| **Member** | Maryam Imran Shah |
| **Member** | Aniqa Qamar |
| **Member** | Saboor Khalil |

---

## Project Status

**Current Milestone**

✅ **Week 1 — Repository Setup & Git Workflow**

Future milestones will include backend development, AI integration, document parsing, vector databases, deployment, and application refinement according to the fellowship roadmap.

---

## License

This project is licensed under the **MIT License**.
