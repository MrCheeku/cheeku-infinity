# Integration Roadmap

## v0.2 — Source manager (current)
- Catalogue of 16 upstream projects.
- CLI for listing, inspection, clone, update, status, audit and environment checks.
- Upstream projects remain separate checkouts with their own licenses and install procedures.

## v0.3 — Verified setup recipes
- Test upstream projects on documented operating systems.
- Record release versions, prerequisites, setup commands and limitations.
- Add configuration templates with placeholders only.
- Add preflight checks without automatically running unreviewed scripts.

## v0.4 — Optional agent adapters
- Add opt-in adapters for supported agent hosts.
- Keep skills, MCP servers, APIs and applications clearly separated.
- Require explicit configuration for credentials and tool permissions.
- Add isolated integration tests.

## v1.0 — Tested workflows
- Compose verified tools into documented workflows.
- Make steps inspectable, logged and cancellable.
- Require confirmation for destructive or sensitive actions.
- Consider a dashboard only after workflows are reliable.

A source clone is not an integration. Do not label a tool integrated until setup, adapter, permissions and tests are verified.
