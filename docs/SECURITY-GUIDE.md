# Safe Integration Guide

1. Review source code and installation scripts before execution.
2. Use an isolated environment, container or disposable virtual machine for unfamiliar tools.
3. Apply least privilege; do not run as administrator/root unless justified.
4. Store credentials in a secrets manager or environment variables; never commit tokens or private keys.
5. Only scan systems you own or have explicit permission to test.
6. Review package lockfiles, model/dataset sources, container images and external services.
7. Record the upstream URL, tag or commit SHA for source you redistribute.
8. Re-check license, attribution and trademark terms before bundling code or assets.

CHEEKU INFINITY fetches source without executing third-party setup scripts.
