# Contributing

Thanks for considering a contribution to CHEEKU INFINITY.

## What belongs here?
- Accurate catalogue metadata and setup notes.
- Improvements to the original CLI, tests and documentation.
- Optional adapters that preserve upstream ownership and licensing.
- Reproducible installation checks and compatibility notes.

## Development setup

~~~bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest -q
~~~

On Windows PowerShell, activate with .venv\Scripts\Activate.ps1.

## Guidelines
1. Open an issue before major changes or adding new upstream projects.
2. Use canonical upstream URLs and clearly label project types.
3. Do not copy third-party source unless its license permits it and notices are preserved.
4. Never commit credentials, tokens, private URLs or user data.
5. Keep tests deterministic and offline.

## Pull request checklist
- [ ] Change has a clear purpose and documentation.
- [ ] Tests pass locally.
- [ ] No secrets or private data added.
- [ ] Third-party licenses and attribution are respected.
- [ ] Catalogue and README updated where needed.

Original contributions submitted to this repository are offered under the MIT license in LICENSE unless otherwise stated and accepted by the maintainers.
