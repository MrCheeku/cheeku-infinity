<div align="center">

# ∞ CHEEKU INFINITY

### Beyond Tools. Beyond Limits.

**One curated collection. Sixteen powerful open-source projects.**

[![CI](https://github.com/MrCheeku/cheeku-infinity/actions/workflows/ci.yml/badge.svg)](https://github.com/MrCheeku/cheeku-infinity/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-2ea44f.svg)](LICENSE)
[![Projects](https://img.shields.io/badge/Projects-16-7656D6)](catalog.json)
[![Engineered by](https://img.shields.io/badge/Engineered%20by-Mr.Cheeku-111827)](https://github.com/MrCheeku)

**Discover · Fetch · Inspect · Update**

</div>

---

## About

**CHEEKU INFINITY** is an open-source collection and command-line source manager created under the **Mr.Cheeku** brand. It brings 16 independently maintained projects into one organized catalogue, covering AI, software engineering, cybersecurity, research, design, infrastructure, productivity and media.

Use one CLI to discover projects, inspect what they do, download their source code, check local status and update your local copies.

> **The idea:** One organized entry point to a world of useful developer tools and AI capabilities.

### Why use it?

- **One catalogue:** Browse all 16 projects from one place.
- **Simple discovery:** Filter projects by type or engineering domain.
- **On-demand downloads:** Clone only the projects you need.
- **Source-aware updates:** Pull changes from original upstream repositories.
- **Local visibility:** See what is downloaded and whether your copy has local changes.
- **License awareness:** Locate common license and notice files before reuse.
- **Open development:** Automated tests, CI and contribution guidance.

## The collection

| Type | Count | Meaning |
|---|---:|---|
| Agent skills, plugins and playbooks | 7 | Extend compatible AI-agent environments |
| Developer tools, frameworks and services | 6 | Provide reusable software capabilities |
| Applications | 3 | User-facing software projects |
| **Total** | **16** | **Across 8 engineering domains** |

### AI & Machine Learning

| Project | What it brings |
|---|---|
| [MiniMind](https://github.com/jingyaogong/minimind) | Learn and experiment with small language-model training |
| [OpenVINO](https://github.com/openvinotoolkit/openvino) | Optimize and deploy AI inference on supported hardware |

### Software Engineering & AI Coding

| Project | What it brings |
|---|---|
| [Superpowers](https://github.com/obra/superpowers) | Planning, TDD, debugging and software-development agent workflows |
| [CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Create command-line interfaces for agent-controllable software |
| [Cursor Plugins](https://github.com/cursor/plugins) | Extend the Cursor coding-agent environment with plugins |

### Cybersecurity & Compliance

| Project | What it brings |
|---|---|
| [Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | Security-focused agent skills for authorized vulnerability assessment |
| [App Store Compliance](https://github.com/mjmirza/app-store-compliance) | App-store compliance guidance and checks |

### Research & Web Intelligence

| Project | What it brings |
|---|---|
| [Firecrawl](https://github.com/firecrawl/firecrawl) | Crawl, scrape, search and extract website content |
| [Last30Days Skill](https://github.com/mvanhorn/last30days-skill) | Research recent online discussions and trends |

### Design & Documentation

| Project | What it brings |
|---|---|
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) | Agent guidance for technical and visual diagrams |
| [Stitch Skills](https://github.com/google-labs-code/stitch-skills) | UI/UX design workflows using Google Stitch |

### DevOps & Infrastructure

| Project | What it brings |
|---|---|
| [NGINX](https://github.com/nginx/nginx) | Web serving, reverse proxying and traffic distribution |
| [OpenSRE](https://github.com/Tracer-Cloud/opensre) | AI-assisted CI/CD and reliability troubleshooting |

### Productivity

| Project | What it brings |
|---|---|
| [AFFiNE](https://github.com/toeverything/AFFiNE) | Documents, notes and visual knowledge workspace |
| [Ghost Downloader 3](https://github.com/XiaoYouChR/Ghost-Downloader-3) | Desktop download management |

### Media & Video

| Project | What it brings |
|---|---|
| [AutoClip](https://github.com/zhouxiaoka/autoclip) | AI-assisted long-to-short video clipping |

See the [detailed catalogue](docs/CATALOG.md) and [project type guide](docs/PROJECT-TYPES.md).

---

## How it works

CHEEKU INFINITY keeps its own management code separate from the 16 upstream projects.

~~~mermaid
flowchart TD
    U["You"] --> CLI["CHEEKU INFINITY CLI"]
    CLI --> CAT["16-project catalogue"]
    CLI --> GIT["Git source manager"]
    GIT --> SRC["Local sources directory"]
    SRC --> A["AI skills and plugins"]
    SRC --> T["Developer tools and services"]
    SRC --> AP["Applications"]
~~~

When you request a project, CHEEKU INFINITY fetches it from its original GitHub repository. Each project keeps its own source code, Git history, setup instructions and license.

## Quick start

### Requirements

- Python **3.10 or newer**
- [Git](https://git-scm.com/downloads)
- Internet connection for downloading upstream projects

### 1. Clone CHEEKU INFINITY

~~~bash
git clone https://github.com/MrCheeku/cheeku-infinity.git
cd cheeku-infinity
~~~

### 2. Install the CLI

**Windows PowerShell**

~~~powershell
py -m pip install .
~~~

**Linux / macOS**

~~~bash
python3 -m pip install .
~~~

For development and tests, install the optional development tools:

~~~bash
python -m pip install -e ".[dev]"
~~~

### 3. Explore

~~~bash
cheeku-infinity --version
cheeku-infinity list
cheeku-infinity info superpowers
~~~

### 4. Download a project

~~~bash
cheeku-infinity clone superpowers
~~~

The source is placed in the local sources/superpowers/ directory. Read that project's own README and follow its official installation instructions.

To fetch the complete collection:

~~~bash
cheeku-infinity clone --all
~~~

> Cloning all 16 projects can use significant disk space and bandwidth. The clone command downloads source code only; it does not execute third-party installation scripts.

## CLI command reference

| Command | Purpose |
|---|---|
| cheeku-infinity list | List all 16 projects |
| cheeku-infinity list --kind skill | Show agent skills and plugins |
| cheeku-infinity list --kind tool | Show developer tools |
| cheeku-infinity list --kind application | Show applications |
| cheeku-infinity list --domain research | Filter by domain |
| cheeku-infinity list --json | Export catalogue data as JSON |
| cheeku-infinity info PROJECT_ID | Inspect one project's details |
| cheeku-infinity clone PROJECT_ID | Download one upstream project |
| cheeku-infinity clone --all | Download all 16 projects |
| cheeku-infinity update PROJECT_ID | Update one cloned project |
| cheeku-infinity update --all | Update projects already cloned locally |
| cheeku-infinity status | Show local clone and modification status |
| cheeku-infinity audit | Check common license and notice filenames |
| cheeku-infinity doctor | Check basic environment requirements |

Use the command-line help for further options.

## What works today?

| Capability | Status |
|---|---|
| Browse and filter the 16-project catalogue | Implemented |
| Inspect project descriptions and source links | Implemented |
| Clone one or all upstream repositories | Implemented |
| Update already-cloned repositories | Implemented |
| View clone state and local modifications | Implemented |
| Check common license and notice filenames | Implemented |
| Check Python and Git prerequisites | Implemented |
| Automatically install every upstream project | Not implemented |
| Launch all applications through one command | Not implemented |
| Unified AI runtime and multi-agent orchestration | Planned |
| Integrated dashboard | Planned |
| Cross-project automated workflows | Planned |

**Transparency matters:** This release is a working source manager and curated collection, not a claim that 16 separate software projects have already been merged into one application.

## Project structure

~~~text
cheeku-infinity/
├── cheeku_infinity/
│   ├── __init__.py
│   ├── catalog.py
│   └── cli.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CATALOG.md
│   ├── CLI.md
│   ├── INTEGRATION-ROADMAP.md
│   ├── PROJECT-TYPES.md
│   └── SECURITY-GUIDE.md
├── tests/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── catalog.json
├── pyproject.toml
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── README.md
~~~

## Roadmap

- [x] **v0.1** — Initial repository bootstrap.
- [x] **v0.2** — Project catalogue, CLI, source cloning, updates, status, audit, docs and CI.
- [ ] **v0.3** — Verified installation recipes and dependency preflight checks.
- [ ] **v0.4** — Optional adapters for compatible AI-agent environments.
- [ ] **v0.5** — Tested, permission-controlled workflows connecting selected tools.
- [ ] **v1.0** — Mature integrations, with a dashboard considered after the workflows are reliable.

Track development through [GitHub Issues](https://github.com/MrCheeku/cheeku-infinity/issues).

## License & third-party ownership

CHEEKU INFINITY's original catalogue, CLI code and documentation are licensed under the [MIT License](LICENSE), unless a file says otherwise.

The 16 referenced projects are **not relicensed by this repository**. They remain the property of their respective maintainers and retain their own licenses, notices, dependencies, assets and trademarks. Always review the current upstream license before modifying, bundling, redistributing or using a project commercially.

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). CHEEKU INFINITY is an independent collection and is not affiliated with or endorsed by the upstream projects.

## Security

- Only test systems you own or are explicitly authorized to assess.
- Review third-party code and installation scripts before executing them.
- Use isolated environments and least-privilege accounts.
- Never commit API keys, passwords, tokens or private data.
- Treat downloaded source and AI-generated output as untrusted until reviewed.

Read [SECURITY.md](SECURITY.md) and the [Security Guide](docs/SECURITY-GUIDE.md).

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md), preserve upstream attribution and license requirements, and include tests for code changes.

## Maintainer

**Mr.Cheeku** · [GitHub Profile](https://github.com/MrCheeku)

---

<div align="center">

### ∞ CHEEKU INFINITY

**Beyond Tools. Beyond Limits.**

*Engineered by Mr.Cheeku*

</div>
