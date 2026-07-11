# Zeppelin AI Resume Screener

**AI-powered Resume Parser & Feedback Engine**

*Developed as part of the Zeppelin AI & Generative AI Fellowship.*

## Overview

The **Zeppelin AI Resume Screener** is being developed to streamline the initial recruitment process by parsing resumes, comparing candidate profiles with job descriptions, and generating intelligent feedback using Generative AI.

This repository currently reflects the **Week 1** project setup, focusing on repository initialization, team collaboration, Git workflow, and development planning. Core application features will be implemented in the upcoming weeks of the fellowship.

## Repository Workflow

This project follows the Git branching strategy defined for the fellowship.

| Branch | Purpose |
| :------ | :------ |
| `main` | Stable production branch (protected – no direct pushes) |
| `dev` | Development integration branch |
| `feature/<feature-name>` | Individual feature development |

### Current Feature Branches

| Member | Branch |
| :------ | :----- |
| Suraiba Idrees | `feature/frontend-foundation` |
| Maryam Imran Shah | `feature/ai-engine` |
| Aniqa Qamar | *Pending* |
| Saboor Khalil | *Pending* |

## Getting Started

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd zeppelin-ai-resume-screener
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

## Development Guidelines

- Create a new `feature/*` branch before starting any task.
- Commit changes frequently using meaningful commit messages.
- Submit completed work through Pull Requests to the `dev` branch.
- Do not push directly to the `main` branch.
- Pull the latest changes from `dev` before starting new work.

Example commit messages:

```text
feat: implement resume upload
fix: resolve PDF parsing issue
docs: update project README
```

## Current Development

Development tasks are managed through GitHub Issues and implemented on individual feature branches.

### Active Issues

- Backend project setup
- AI engine initialization
- Core data extraction logic
- Frontend foundation and project setup

Additional issues will be created as new milestones are introduced throughout the fellowship.

## Project Team

| Role | Member |
| :--- | :----- |
| **Team Lead** | Suraiba Idrees |
| **Member** | Maryam Imran Shah |
| **Member** | Aniqa Qamar |
| **Member** | Saboor Khalil |

## Project Status

**Current Phase:** Week 1 — Repository Setup & Git Workflow

This repository will be updated incrementally as new project milestones and features are completed during the fellowship.

## License

This project is licensed under the MIT License.