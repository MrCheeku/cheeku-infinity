"""Curated upstream project metadata.

This catalogue stores pointers and descriptions, not copies of upstream code.
Upstream projects retain their own releases, maintainers and license terms.
"""

PROJECTS = [
    {
        "id": "claude-bughunter", "name": "Claude-BugHunter",
        "repository": "elementalsouls/Claude-BugHunter",
        "url": "https://github.com/elementalsouls/Claude-BugHunter",
        "branch": "main", "kind": "skill", "domain": "Cybersecurity",
        "description": "Security-focused agent skills and workflows for authorized vulnerability assessment.",
        "setup": "Read the upstream README; install into a compatible agent environment. Test only systems you own or are authorized to assess."
    },
    {
        "id": "superpowers", "name": "Superpowers",
        "repository": "obra/superpowers",
        "url": "https://github.com/obra/superpowers",
        "branch": "main", "kind": "skill", "domain": "Software Engineering",
        "description": "A software-development skills framework for planning, TDD, debugging, code review and agent workflows.",
        "setup": "Follow the upstream installation instructions for a supported coding-agent environment."
    },
    {
        "id": "cli-anything", "name": "CLI-Anything",
        "repository": "HKUDS/CLI-Anything",
        "url": "https://github.com/HKUDS/CLI-Anything",
        "branch": "main", "kind": "tool", "domain": "Developer Tools",
        "description": "A framework for creating command-line interfaces that allow agents to operate supported software.",
        "setup": "Follow upstream setup instructions. Generated CLIs and target applications may require additional dependencies."
    },
    {
        "id": "minimind", "name": "MiniMind",
        "repository": "jingyaogong/minimind",
        "url": "https://github.com/jingyaogong/minimind",
        "branch": "master", "kind": "tool", "domain": "AI & Machine Learning",
        "description": "An educational codebase for training and experimenting with small language models.",
        "setup": "Review Python, PyTorch, dataset and hardware requirements in the upstream README before training."
    },
    {
        "id": "cursor-plugins", "name": "Cursor Plugins",
        "repository": "cursor/plugins",
        "url": "https://github.com/cursor/plugins",
        "branch": "main", "kind": "skill", "domain": "AI Coding Agents",
        "description": "Plugins and reusable integrations for the Cursor coding-agent environment.",
        "setup": "Use Cursor's supported plugin import/install flow and consult upstream instructions."
    },
    {
        "id": "firecrawl", "name": "Firecrawl",
        "repository": "firecrawl/firecrawl",
        "url": "https://github.com/firecrawl/firecrawl",
        "branch": "main", "kind": "tool", "domain": "Research & Web Data",
        "description": "A web-data platform and API for crawling, scraping, searching and extracting website content.",
        "setup": "Review upstream deployment instructions, environment variables, resource requirements and service configuration."
    },
    {
        "id": "nginx", "name": "NGINX",
        "repository": "nginx/nginx",
        "url": "https://github.com/nginx/nginx",
        "branch": "master", "kind": "tool", "domain": "Infrastructure & Networking",
        "description": "Web server and reverse-proxy software for HTTP serving, proxying and traffic distribution.",
        "setup": "For normal use, prefer trusted OS packages; see upstream documentation for configuration and source builds."
    },
    {
        "id": "openvino", "name": "OpenVINO",
        "repository": "openvinotoolkit/openvino",
        "url": "https://github.com/openvinotoolkit/openvino",
        "branch": "master", "kind": "tool", "domain": "AI & Machine Learning",
        "description": "An AI inference and optimization toolkit for supported hardware and deployment environments.",
        "setup": "Choose a current installation method and hardware target from upstream documentation."
    },
    {
        "id": "diagram-design", "name": "Diagram Design",
        "repository": "cathrynlavery/diagram-design",
        "url": "https://github.com/cathrynlavery/diagram-design",
        "branch": "main", "kind": "skill", "domain": "Design & Documentation",
        "description": "Agent-oriented instructions for producing structured technical and visual diagrams.",
        "setup": "Follow the upstream skill setup for a compatible agent host."
    },
    {
        "id": "last30days-skill", "name": "Last30Days Skill",
        "repository": "mvanhorn/last30days-skill",
        "url": "https://github.com/mvanhorn/last30days-skill",
        "branch": "main", "kind": "skill", "domain": "Research & Web Intelligence",
        "description": "An agent skill for researching recent online discussions, trends and sources.",
        "setup": "Follow upstream instructions; some sources may require accounts, credentials or API access."
    },
    {
        "id": "stitch-skills", "name": "Stitch Skills",
        "repository": "google-labs-code/stitch-skills",
        "url": "https://github.com/google-labs-code/stitch-skills",
        "branch": "main", "kind": "skill", "domain": "Design & Documentation",
        "description": "Agent skills and workflows for UI/UX design with the Google Stitch toolchain.",
        "setup": "Check upstream requirements for Stitch MCP and compatible agent environments."
    },
    {
        "id": "app-store-compliance", "name": "App Store Compliance",
        "repository": "mjmirza/app-store-compliance",
        "url": "https://github.com/mjmirza/app-store-compliance",
        "branch": "main", "kind": "skill", "domain": "App Security & Compliance",
        "description": "A compliance playbook and related checks for preparing applications for store submission.",
        "setup": "Use as a review aid, not legal advice. Verify current store policies and applicable laws."
    },
    {
        "id": "opensre", "name": "OpenSRE",
        "repository": "Tracer-Cloud/opensre",
        "url": "https://github.com/Tracer-Cloud/opensre",
        "branch": "main", "kind": "tool", "domain": "DevOps & Reliability",
        "description": "An AI-assisted CLI for investigating CI/CD and software delivery reliability issues.",
        "setup": "Check upstream maturity, provider support, permissions and installation requirements before production use."
    },
    {
        "id": "affine", "name": "AFFiNE",
        "repository": "toeverything/AFFiNE",
        "url": "https://github.com/toeverything/AFFiNE",
        "branch": "canary", "kind": "application", "domain": "Productivity",
        "description": "A productivity and knowledge workspace combining documents, notes and visual canvases.",
        "setup": "For everyday use, prefer an official release or hosted option. The source repository is a large application codebase."
    },
    {
        "id": "ghost-downloader-3", "name": "Ghost Downloader 3",
        "repository": "XiaoYouChR/Ghost-Downloader-3",
        "url": "https://github.com/XiaoYouChR/Ghost-Downloader-3",
        "branch": "main", "kind": "application", "domain": "Productivity",
        "description": "A desktop download manager; supported platforms and protocols depend on the current release.",
        "setup": "Use official release assets where available and verify supported platforms in the upstream README."
    },
    {
        "id": "autoclip", "name": "AutoClip",
        "repository": "zhouxiaoka/autoclip",
        "url": "https://github.com/zhouxiaoka/autoclip",
        "branch": "main", "kind": "application", "domain": "Media & Video",
        "description": "An AI-assisted video clipping application intended to turn longer videos into short-form clips.",
        "setup": "Check upstream requirements for models, media tools, GPU support and API credentials."
    }
]

PROJECT_BY_ID = {project["id"]: project for project in PROJECTS}

if len(PROJECT_BY_ID) != len(PROJECTS):
    raise RuntimeError("Project IDs must be unique.")
