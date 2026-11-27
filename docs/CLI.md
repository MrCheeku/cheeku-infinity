# CLI Reference

Install with Python 3.10+ and Git:

~~~bash
python -m pip install .
~~~

## list
~~~bash
cheeku-infinity list
cheeku-infinity list --kind skill
cheeku-infinity list --kind tool
cheeku-infinity list --kind application
cheeku-infinity list --domain research
cheeku-infinity list --json
~~~

## info
~~~bash
cheeku-infinity info firecrawl
~~~

## clone
~~~bash
cheeku-infinity clone superpowers
cheeku-infinity clone --all
cheeku-infinity clone superpowers --destination ./my-sources
~~~

Clones are shallow and placed inside the configured destination. The command never runs downloaded code. Existing Git checkouts are left untouched; a non-Git directory at the target path is never overwritten.

## update
~~~bash
cheeku-infinity update superpowers
cheeku-infinity update --all
~~~

Updates use fast-forward-only pulls. Local divergent changes are not force-overwritten.

## status
~~~bash
cheeku-infinity status
cheeku-infinity status --json
~~~

## audit
~~~bash
cheeku-infinity audit
~~~

Audit checks familiar license/notice filenames and local Git changes. It does not parse license terms or determine legal compatibility.

## doctor
~~~bash
cheeku-infinity doctor
~~~

Use cheeku-infinity --help for all options.
