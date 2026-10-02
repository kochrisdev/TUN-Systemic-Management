# TUN Systemic Management

**Direct human and machine intelligence with purpose, bounded delegation, and evidence.**

TUN Systemic Management is a proposed management discipline for organizations in which people and AI systems both recommend, coordinate, and act. It connects organizational outcomes to explicit mandates, accountable decisions, resource limits, and reviews of what actually happened.

**Current status: draft specification with an experimental local pilot.** The repository includes a management model, templates, a specialized JSON Schema profile, and a Python/SQLite initiative-review pilot. The pilot uses fixture identities and synthetic evidence. There is no production identity integration, external provider, dashboard, or validated organizational adoption.

## The management question

An AI initiative can deliver every planned feature and still fail to help its users. An agent can complete an authorized action while its mandate has become obsolete. A management report can sound certain even when the underlying outcome is unresolved.

Management needs an account of what is worth pursuing, who can decide, what has been delegated, what evidence supports the results, and when to change direction.

```text
SENSE → FRAME → DECIDE → DELEGATE → OBSERVE → ADAPT
   ↑                                          │
   └──────────────────────────────────────────┘
```

## One family, three responsibilities

| Project | Central question |
|---|---|
| [TUN Systemic Design](https://github.com/kochrisdev/TUN-Systemic-Design) | How do people understand and control AI behavior? |
| [TUN Systemic Engineering](https://github.com/kochrisdev/TUN-Systemic-Engineering) | How are actions authorized, executed, verified, and recovered? |
| **TUN Systemic Management** | How do organizations choose outcomes, delegate authority, allocate resources, and adapt from evidence? |

Management supplies purpose and mandates. Engineering enforces current authority at the action boundary and supplies evidence of effects. Design makes those relationships understandable and controllable. They are cooperating responsibilities, not a mandatory sequence of separate software services.

## Start here

| Read | Use it to |
|---|---|
| [Introduction](docs/INTRODUCTION.md) | Understand the problem through a concrete example |
| [Getting started](docs/GETTING-STARTED.md) | Apply the draft to one bounded initiative |
| [Run the local pilot](docs/PILOT.md) | Exercise version-bound decisions, shared reservations, evidence review, and restart |
| [Pilot validation](docs/PILOT-VALIDATION-2026-10-02.md) | Inspect the named local run and its limitations |
| [Concept note](docs/CONCEPT-NOTE-v0.1.md) | Understand the proposed scope and approach |
| [Manifesto](docs/MANIFESTO-v0.1.md) | Read the twelve guiding commitments |
| [Management model](docs/MANAGEMENT-MODEL-v0.1.md) | Follow the management loop across organizational levels |
| [Specification](docs/SPECIFICATION-v0.1.md) | Inspect twelve proposed behavioral requirements |
| [AI support initiative](examples/ai-support-initiative.md) | Walk through a fictional mandate, evidence review, and decision |
| [Documentation index](docs/README.md) | Find the complete reference and templates |

## Try the local pilot

Use Python 3.11 or later in a virtual environment. From the repository root, after activating that environment:

```sh
python -m pip install -r requirements-pilot.txt
python -m reference.tsm_pilot.demo
python -m unittest discover -s tests -v
```

The demo creates a temporary fixture database, approves a mandate, reserves part of a shared budget, reviews insufficient-quality observations, pauses new reservations, and reopens the store. It preserves an unknown-effect fixture alongside the outcome assessment. It never calls a model or provider, and a reservation is not an execution grant. See the [pilot guide](docs/PILOT.md) for Windows setup and retaining the database.

Next: connect one bounded engineering operation and then a human review interface. The Markdown worked examples remain fictional narratives, separate from the executable fixture scenario.

## Project

[Scope and non-claims](docs/SCOPE.md) · [Status and roadmap](docs/STATUS-AND-ROADMAP.md) · [Contributing](CONTRIBUTING.md) · [Governance](GOVERNANCE.md) · [Changelog](CHANGELOG.md) · [MIT license](LICENSE)

Maintained by Christopher Tun (`@kochrisdev`). This initial documentation was developed with AI assistance.

**Purpose. Bounded delegation. Evidence-led adaptation.**
