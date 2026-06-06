# Changelog

All notable changes to this project will be documented in this file.

This project follows a draft-oriented development process.
Versions marked as `draft` are conceptual and may change before stabilization.

---

## [v0.5.0-draft] - 2026-06-06

### Added

* Added `docs/v0.5-structural-diff.md`.

  * Defines the structural transition from Royalty OS v0.4 to v0.5.
  * Introduces v0.5 as a shift from value relationship infrastructure to personal representative infrastructure.
  * Defines the Personal AI Agent Royalty Layer.
  * Clarifies that v0.5 does not automatically determine ownership, calculate compensation, execute payments, or enforce legal claims.
  * Adds the core distinction:

    * `v0.4 = relationship infrastructure`
    * `v0.5 = representative infrastructure`

* Added `docs/personal-ai-agent-royalty-os.md`.

  * Defines the Personal AI Agent Royalty OS as the core document of v0.5.
  * Explains why personal AI agents are needed in AI-era value circulation.
  * Defines the personal AI agent as a representative interface.
  * Clarifies that the personal AI agent is not:

    * a value owner
    * a judge
    * a payment executor
    * a legal enforcement engine
  * Defines roles including:

    * Trace Manager
    * Usage Detection Assistant
    * Value Event Preparer
    * Attribution Route Assistant
    * Claim Route Assistant
    * Return Route Assistant
    * Representative Event Logger
  * Adds privacy, governance, boundary, and non-goal sections.

* Added `specs/royalty-os-v0.5-draft.yaml`.

  * Provides the initial conceptual specification for Royalty OS v0.5.
  * Defines the title: `Personal AI Agent Royalty OS`.
  * Defines the subtitle: `Agent-Mediated Value Routing Architecture`.
  * Adds core layers:

    * Human Intelligence Layer
    * Personal AI Agent Layer
    * Trace Management Layer
    * Agent-Mediated Usage Detection Layer
    * Value Event Layer
    * Value Graph Layer
    * Policy and Governance Review Layer
    * Human-Reviewed Value Return Layer
  * Adds core components:

    * Personal AI Agent
    * Personal Trace Fingerprint
    * Agent-Mediated Usage Detection
    * Attribution Route
    * Claim Route
    * Human-Reviewed Value Return
    * Representative Event Log
  * Adds boundary definitions for non-automatic ownership, compensation, payment, and enforcement.
  * Adds planned schemas and examples for later stages.

* Added `schemas/personal-agent.schema.json`.

  * Validates Personal AI Agent records.
  * Defines allowed and prohibited roles for a personal AI agent.
  * Adds review, boundary, privacy, governance, and representative event log policies.
  * Ensures that personal AI agents cannot act as automatic owners, judges, payment executors, legal enforcers, or infringement accusers.

* Added `examples/personal-agent.example.yaml`.

  * Provides a sample personal AI agent record.
  * Demonstrates a representative agent that can assist with trace management, usage detection, attribution routing, claim route preparation, and human-reviewed return preparation.
  * Preserves strict boundaries against automatic ownership, compensation, payment, and enforcement.

* Added `schemas/trace-fingerprint.schema.json`.

  * Validates Personal Trace Fingerprint records.
  * Defines intellectual trace elements such as:

    * writing patterns
    * question structures
    * prompt patterns
    * conceptual frameworks
    * terminology
    * theory structures
    * model output patterns
  * Clarifies that a trace fingerprint is a reviewable structure, not automatic proof of ownership, infringement, compensation, or claim validity.

* Added `examples/trace-fingerprint.example.yaml`.

  * Provides a sample personal trace fingerprint.
  * Demonstrates how a creator's question structures, conceptual frameworks, terminology, and boundary principles may be recorded.
  * Preserves human review and minimal disclosure.

* Added `schemas/usage-detection-event.schema.json`.

  * Validates Agent-Mediated Usage Detection Event records.
  * Defines how possible usage of a personal trace may be recorded.
  * Supports usage types such as:

    * reference
    * summary
    * quotation
    * transformation
    * derivative generation
    * conceptual reuse
    * prompt pattern reuse
    * model behavior similarity
    * agent-to-agent transmission
  * Clarifies that usage detection creates a reviewable event candidate, not an automatic claim.

* Added `examples/usage-detection-event.example.yaml`.

  * Provides a sample usage detection event.
  * Connects a personal trace fingerprint to a possible AI-generated output.
  * Demonstrates usage assessment, confidence boundaries, value event candidate preparation, and governance review.

* Added `schemas/attribution-route.schema.json`.

  * Validates Attribution Route records.
  * Defines how a detected usage relationship may be connected back to a person, trace, work, prompt, structure, document, or agent.
  * Clarifies that attribution routes are traceability structures, not payment routes.
  * Adds attribution assessment, evidence, value graph references, review policy, boundary policy, privacy policy, and governance status.

* Added `examples/attribution-route.example.yaml`.

  * Provides a sample attribution route.
  * Connects a usage detection event to a personal trace fingerprint.
  * Demonstrates conceptual attribution, terminology attribution, structural attribution, and citation review preparation.
  * Clarifies that attribution is not payment and does not prove ownership, infringement, compensation, or claim validity.

* Added `schemas/claim-route.schema.json`.

  * Validates Claim Route records.
  * Defines how a personal AI agent may prepare a reviewable request for:

    * attribution review
    * usage review
    * correction
    * dispute handling
    * royalty review
    * value return
    * governance escalation
  * Clarifies that a claim route is not enforcement.
  * Adds claim request, claim assessment, claim action, evidence, value graph reference, return route reference, review policy, boundary policy, privacy policy, and governance status.

* Added `examples/claim-route.example.yaml`.

  * Provides a sample claim route.
  * Connects a personal agent, trace fingerprint, usage detection event, attribution route, and return route candidate.
  * Demonstrates usage review, attribution review, royalty review, and value return review preparation.
  * Clarifies that the claim route does not execute payment, enforcement, legal action, or automatic public accusation.

* Added `schemas/return-route.schema.json`.

  * Validates Return Route records.
  * Defines human-reviewed pathways for:

    * attribution
    * acknowledgment
    * citation
    * reputation credit
    * access credit
    * royalty intent
    * micro-royalty routing
    * wallet reference
    * external settlement preparation
  * Clarifies that a return route is not payment execution.
  * Adds return request, return assessment, return pathway, wallet reference, return units, evidence, value graph reference, review policy, boundary policy, privacy policy, and governance status.

* Added `examples/return-route.example.yaml`.

  * Provides a sample return route.
  * Demonstrates a human-reviewed pathway for attribution, citation, acknowledgment, royalty intent, micro-royalty routing, wallet reference, and external settlement preparation.
  * Clarifies that the record does not execute payment, calculate compensation, enforce claims, or create automatic legal obligations.

* Added `scripts/validate_examples.py`.

  * Validates example YAML files against JSON Schema files.
  * Uses `PyYAML` and `jsonschema`.
  * Supports readable validation error paths.
  * Current validation targets:

    * Personal AI Agent
    * Personal Trace Fingerprint
    * Agent-Mediated Usage Detection Event
    * Attribution Route
    * Claim Route
    * Return Route

* Added `.github/workflows/validate-examples.yml`.

  * Adds GitHub Actions validation for schemas, examples, and the validation script.
  * Runs on push, pull request, and manual workflow dispatch.
  * Installs Python dependencies and runs `python scripts/validate_examples.py`.

* Updated `README.md`.

  * Added project overview for Royalty OS v0.5.
  * Added relationship to Royalty OS v0.4.
  * Added relationship to Communication Royalty OS.
  * Added architecture overview.
  * Added core flow.
  * Added repository structure.
  * Added key documents.
  * Added schema and example descriptions.
  * Added validation instructions.
  * Added recommended reading order.
  * Added non-goals and boundary principles.

### Core Principle Added

Royalty OS v0.5 is based on the following principle:

> Personal AI agents assist with trace management and value routing.
> They do not automatically decide ownership, compensation, payment, or enforcement.

### Structural Transition

This version defines the transition as:

```text
Royalty OS v0.4:
Dynamic Value Relationship OS

Royalty OS v0.5:
Personal AI Agent Royalty OS
```

Or:

```text
v0.4 = value relationship infrastructure
v0.5 = personal representative infrastructure
```

### Core Flow Added

This version defines the main v0.5 flow as:

```text
Personal AI Agent
↓
Personal Trace Fingerprint
↓
Agent-Mediated Usage Detection Event
↓
Attribution Route
↓
Claim Route
↓
Return Route
```

Meaning:

```text
Who represents the individual
↓
What intellectual trace is protected
↓
What possible usage was detected
↓
How the usage may relate back to the trace
↓
What review or claim pathway is requested
↓
How value return may be prepared after review
```

### Boundaries

Royalty OS v0.5 explicitly does not provide:

* automatic legal judgment
* automatic ownership resolution
* automatic copyright enforcement
* automatic payment execution
* automatic royalty calculation
* automatic infringement detection
* automatic platform compliance enforcement

It also clarifies:

* detection is not proof
* attribution is not payment
* a claim route is not enforcement
* a return route is not payment execution
* similarity is not proof
* human review is required

### Validation

The validation package currently checks:

```text
Personal AI Agent
Personal Trace Fingerprint
Agent-Mediated Usage Detection Event
Attribution Route
Claim Route
Return Route
```

Validation can be run with:

```bash
pip install pyyaml jsonschema
python scripts/validate_examples.py
```

GitHub Actions workflow:

```text
.github/workflows/validate-examples.yml
```

### Planned Next Steps

Planned next additions may include:

```text
docs/agent-mediated-value-routing.md
docs/boundary-principles.md
docs/communication-royalty-os-bridge.md
schemas/representative-event.schema.json
examples/representative-event.example.yaml
examples/agent-mediated-value-flow.example.yaml
```

---

## Notes

Royalty OS v0.5 remains a conceptual draft with an initial validation package.

This release does not introduce automatic payment, ownership, compensation, or legal enforcement mechanisms.

The current milestone establishes the first validated flow from personal AI representation to human-reviewed value return preparation.
