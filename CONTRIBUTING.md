# Contributing

Useful contributions include a concrete management scenario, an ambiguous authority boundary, a clearer record definition, or evidence from a bounded adoption. Explain the problem and expected behavior. Identify assumptions and include contrary evidence when relevant.

## Documentation changes

Keep the [documentation index](docs/README.md) current. Preserve the difference between proposed behavior and implemented or validated behavior. If a requirement changes, update the corresponding guidance, [conformance matrix](docs/CONFORMANCE-MATRIX.md), scenarios, and threat analysis.

Use relative links for repository files and pin companion source revisions when making compatibility claims. Keep examples clearly marked as fictional. Do not add private customer, personnel, or operational information to examples or issue reports.

Run the dependency-free documentation check with Python 3.10 or later:

```sh
python scripts/check_docs.py
git diff --check
```

The checker validates local Markdown file targets, duplicate requirement definitions, requirement references, and coverage in the conformance table. It does not fetch external URLs, validate link fragments, execute scenarios, or assess conformance. Review those meanings separately.

## Reporting an implementation or assessment

Identify the specification source revision, product or workflow, environment, applicable requirements, actual procedures and results, responsible reviewer, and limitations. A passing schema check is not evidence that authority or effects are enforced. Preserve failed and incomplete results alongside successful ones.

See [Governance](GOVERNANCE.md) for project decision ownership and licensing.
