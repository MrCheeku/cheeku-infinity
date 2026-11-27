# Understanding Project Types

## Skill
A skill, plugin or playbook extends a compatible AI-agent environment. It is usually not a standalone desktop app. It may require a coding agent, MCP server, API credentials or a particular install directory.

Included: Claude-BugHunter, Superpowers, Cursor Plugins, Diagram Design, Last30Days Skill, Stitch Skills and App Store Compliance.

## Tool
A library, framework, server, command-line utility or model-training codebase. It can be run or integrated, but needs its own setup and dependencies.

Included: CLI-Anything, MiniMind, Firecrawl, NGINX, OpenVINO and OpenSRE.

## Application
A user-facing software project. It may have desktop, web or other interfaces, but releases and supported operating systems are determined by upstream maintainers.

Included: AFFiNE, Ghost Downloader 3 and AutoClip.

## Why source fetching is separate
These projects use different runtimes, dependencies, platforms and licenses. CHEEKU INFINITY fetches source into sources/ only when asked. It does not install every dependency, start every service or execute third-party setup scripts automatically.
