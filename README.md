<div align="center">

# ∞ CHEEKU INFINITY

### Beyond Tools. Beyond Limits.

**A curated collection of AI skills, developer tools, infrastructure and creative applications.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-2ea44f.svg)](LICENSE)
[![Projects](https://img.shields.io/badge/Curated%20projects-16-7656D6)](catalog.json)
[![Maintained by](https://img.shields.io/badge/Maintained%20by-Mr.Cheeku-111827)](https://github.com/MrCheeku)

**Engineered by Mr.Cheeku**

</div>

---

## What is CHEEKU INFINITY?

CHEEKU INFINITY is an open-source, Mr.Cheeku-branded catalogue and source manager for 16 independently maintained projects covering AI agents, software engineering, cybersecurity, web research, design, infrastructure, productivity and media creation.

It gives you one command-line interface to discover projects, inspect their purpose, clone upstream source, update local checkouts, view local status and audit common license/notice files.

**Important:** CHEEKU INFINITY is not yet one merged AI application, autonomous agent team or desktop suite. Each upstream project has its own runtime, dependencies, license and setup. This repository keeps the projects modular and fetches each from its original source when requested.

## The collection

| Domain | Projects |
|---|---|
| AI & Machine Learning | MiniMind, OpenVINO |
| Software Engineering & Agent Workflows | Superpowers, CLI-Anything, Cursor Plugins |
| Cybersecurity & Compliance | Claude-BugHunter, App Store Compliance |
| Research & Web Intelligence | Firecrawl, Last30Days Skill |
| Design & Documentation | Diagram Design, Stitch Skills |
| DevOps & Infrastructure | NGINX, OpenSRE |
| Productivity | AFFiNE, Ghost Downloader 3 |
| Media & Video | AutoClip |

Project types: **7 skills/plugins/playbooks**, **6 tools/frameworks/services**, and **3 applications**. See docs/CATALOG.md and docs/PROJECT-TYPES.md.

## Quick start

### Requirements
- Python 3.10+
- Git installed and available on PATH
- Internet access to fetch upstream repositories

### 1. Clone this repository

~~~bash
git clone https://github.com/MrCheeku/cheeku-infinity.git
cd cheeku-infinity
~~~

### 2. Install the CLI

~~~bash
python -m pip install .
~~~

For development, install editable mode with test dependencies:

~~~bash
python -m pip install -e ".[dev]"
~~~

Windows users can use py instead of python if required.

### 3. Discover the collection

~~~bash
cheeku-infinity list
cheeku-infinity list --kind skill
cheeku-infinity list --domain research
cheeku-infinity info superpowers
~~~

### 4. Fetch projects

~~~bash
cheeku-infinity clone superpowers
cheeku-infinity clone firecrawl
~~~

Clone all 16 projects (this may use significant disk space and bandwidth):

~~~bash
cheeku-infinity clone --all
~~~

Upstream source is stored under sources/project-id/. Clone only downloads source: it does not execute install scripts or grant downloaded software access to your computer.

### 5. Maintain your local collection

~~~bash
cheeku-infinity status
cheeku-infinity audit
cheeku-infinity update superpowers
cheeku-infinity update --all
cheeku-infinity doctor
~~~

See docs/CLI.md for the complete reference.

## What it does and does not do

**Available now:** catalogue browsing, project filtering, project details, shallow source cloning, fast-forward-only updates, local Git status, a basic license/notice filename audit and prerequisite checks.

**Not implemented yet:** automatic installation of every upstream project, one-command launching of every application, a unified AI runtime, agent-to-agent orchestration, an integrated dashboard or automated cross-project workflows. These are future roadmap items, not current features.

## Repository layout

~~~text
cheeku-infinity/
├── cheeku_infinity/       # Python CLI and catalogue
├── docs/                  # Catalogue, usage, architecture and safety docs
├── tests/                 # Offline automated tests
├── .github/workflows/     # Continuous integration
├── catalog.json           # Machine-readable catalogue
├── sources/               # Created locally when projects are cloned
├── LICENSE                # MIT for original CHEEKU INFINITY material
└── THIRD_PARTY_NOTICES.md # Upstream ownership and license boundaries
~~~

## License and ownership

The root MIT license applies only to original CHEEKU INFINITY code and documentation, unless an individual file states otherwise. It does not relicense any listed third-party project.

Every upstream repository remains owned by its original maintainers and retains its own license, copyright notices, trademarks, assets and dependencies. Read the current upstream license before modifying, bundling, redistributing or using an upstream project commercially. See THIRD_PARTY_NOTICES.md.

CHEEKU INFINITY is an independent collection and is not affiliated with or endorsed by the upstream projects.

## Security

- Only test systems you own or are explicitly authorized to assess.
- Review third-party code and install scripts before executing them.
- Use least-privilege accounts and isolated environments.
- Never commit API keys, passwords, tokens or private data.
- Treat downloaded repositories and AI output as untrusted until reviewed.

Read SECURITY.md and docs/SECURITY-GUIDE.md.

## Roadmap

- [x] Curated catalogue of 16 upstream projects.
- [x] CLI for list, info, clone, update, status, audit and doctor.
- [x] Upstream source and license boundaries documented.
- [x] Tests, CI and open-source contribution standards.
- [ ] Verify release-specific installation recipes for every project and OS.
- [ ] Add opt-in adapters for compatible AI agent hosts.
- [ ] Add tested, permission-controlled workflows connecting selected tools.
- [ ] Consider a dashboard only after integrations are reliable.

## Contributing

Contributions are welcome. Read CONTRIBUTING.md and preserve upstream attribution and license requirements.

## Maintainer

**Mr.Cheeku** · https://github.com/MrCheeku

<div align="center">

**CHEEKU INFINITY** · *Beyond Tools. Beyond Limits.*

</div>
