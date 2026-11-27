# Architecture

## Current release: source manager

1. Catalogue: IDs, names, upstream URLs, default branches, broad project type and setup notes.
2. CLI: list, filter, inspect, clone, update, status, audit and doctor commands.
3. Local source area: each project is cloned into sources/<id>/ and retains its own Git history.
4. Documentation and tests: usage, safety, contribution and licensing guidance.

## Data flow

~~~text
User command
    |
    v
CHEEKU INFINITY CLI
    |
    +--> Catalogue lookup
    |
    +--> Git clone / fast-forward pull
    |
    +--> Local Git status and notice-file audit
    |
    v
sources/<project-id>/
    |
    v
Upstream project instructions and runtime
~~~

The CLI does not proxy, rewrite or merge upstream repositories. It does not start services, execute install scripts or grant agent permissions.

## Future integration design

Future opt-in adapters should use explicit configuration, least-privilege credentials, separate processes/services, inspectable logs, cancellation and confirmation for destructive actions. A catalogue entry does not mean that an integration is implemented.
