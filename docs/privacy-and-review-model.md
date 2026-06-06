# Privacy and Review Model

**Version:** v0.5.0-draft
**Status:** Draft
**Layer:** Personal AI Agent Royalty OS
**Related Specification:** `specs/royalty-os-v0.5-draft.yaml`
**Related Documents:**

* `docs/boundary-principles.md`
* `docs/agent-mediated-value-routing.md`
* `docs/communication-royalty-os-bridge.md`
* `docs/personal-ai-agent-royalty-os.md`

---

## 1. Overview

The **Privacy and Review Model** defines how Royalty OS v0.5 handles personal trace data, evidence references, wallet references, representative events, and review workflows.

Royalty OS v0.5 introduces personal AI agents that may assist individuals in managing intellectual traces and routing value relationships.

Because these processes may involve sensitive personal, creative, intellectual, or economic information, privacy and review must be treated as core system layers.

This document defines the privacy and review model for:

* Personal AI Agent records
* Personal Trace Fingerprints
* Usage Detection Events
* Attribution Routes
* Claim Routes
* Return Routes
* Representative Events
* Agent-Mediated Value Flows
* Communication Royalty OS bridge records

The core principle is:

```text
Reference instead of exposure.
Summary instead of raw disclosure.
Review before external action.
```

---

## 2. Purpose

The purpose of this model is to ensure that Royalty OS v0.5 can support agent-mediated value routing without exposing unnecessary private data or allowing premature conclusions.

The model exists to prevent:

* overexposure of personal traces
* leakage of private evidence
* storage of sensitive wallet credentials
* public accusation without review
* external sharing without authorization
* payment or settlement preparation without human review
* automatic escalation from detection to claim
* automatic escalation from claim to enforcement

Royalty OS v0.5 must remain reviewable, auditable, and privacy-preserving.

---

## 3. Core Privacy Principle

The core privacy principle is:

```text
Minimal disclosure by default.
```

This means that the system should only expose the smallest amount of information necessary for review.

The system should prefer:

```text
references over raw data
summaries over full content
hashes over exposed originals
review notes over private evidence dumps
wallet references over wallet credentials
public summaries over private trace disclosure
```

The system should avoid storing or exposing:

* private creative drafts
* private prompts
* private conversations
* private evidence
* sensitive personal information
* payment credentials
* wallet private keys
* API secrets
* authentication tokens
* unnecessary raw outputs
* excessive comparison material

---

## 4. Review as a Safety Layer

Review is not an optional feature in Royalty OS v0.5.

It is a safety layer.

Every major transition should remain reviewable:

```text
Trace registration
↓
Usage detection
↓
Attribution route
↓
Claim route
↓
Return route
↓
Representative event
↓
External process
```

The system should assume:

```text
human_review_required: true
```

Review is required before:

* ownership interpretation
* usage interpretation
* attribution interpretation
* claim interpretation
* return interpretation
* compensation assessment
* wallet reference use
* public disclosure
* external sharing
* external process preparation
* governance escalation
* payment execution

---

## 5. Privacy by Component

### 5.1 Personal AI Agent

A Personal AI Agent may assist with trace management, routing, and review preparation.

Privacy requirements:

* The agent should not expose private trace data by default.
* The agent should not store wallet credentials.
* The agent should not disclose private evidence without review.
* The agent should not publicly accuse external systems.
* The agent should preserve representative event logs without revealing unnecessary private material.

Allowed:

```text
reference trace records
prepare summaries
prepare review candidates
log representative actions
request human review
```

Not allowed:

```text
expose private trace data automatically
publish claims automatically
store wallet credentials
execute payment
escalate externally without review
```

---

### 5.2 Personal Trace Fingerprint

A Personal Trace Fingerprint represents an individual's intellectual trace structure.

Privacy requirements:

* Use summaries whenever possible.
* Use references rather than full raw content.
* Mark sensitive elements clearly.
* Avoid exposing private drafts or private prompts.
* Require review before external sharing.

Trace elements may be marked as:

```text
public
limited
private
sensitive
```

Interpretation:

```text
public = may be referenced openly
limited = may be referenced with constraints
private = should not be externally shared by default
sensitive = requires explicit review before use
```

A trace fingerprint is not ownership proof.

It is a privacy-aware review structure.

---

### 5.3 Usage Detection Event

A Usage Detection Event records possible usage of a trace.

Privacy requirements:

* Avoid including excessive raw detected content.
* Summarize observed usage where possible.
* Reference evidence rather than embedding it.
* Mark private evidence clearly.
* Require review before external sharing or escalation.

Correct use:

```text
content_summary: short reviewable summary
evidence_references: references to supporting material
private_trace_data_included: false
```

Incorrect use:

```text
full private content embedded
sensitive trace material exposed
public accusation generated automatically
```

---

### 5.4 Attribution Route

An Attribution Route connects possible usage to a trace or subject.

Privacy requirements:

* Attribution should not expose private trace data unless reviewed.
* Public attribution should require human review.
* Evidence should be referenced rather than fully embedded.
* The route should preserve uncertainty.

Attribution is not payment.

Attribution is not ownership proof.

Attribution is not infringement proof.

---

### 5.5 Claim Route

A Claim Route structures a reviewable request.

Privacy requirements:

* Claim routes should not automatically become public.
* Claim route evidence should remain minimally disclosed.
* External process preparation should require review.
* Public accusation must not be automatic.
* Private trace or evidence data should not be exposed without review.

A claim route is not enforcement.

It is a reviewable request pathway.

---

### 5.6 Return Route

A Return Route prepares possible value return.

Privacy requirements:

* Wallet references must not include sensitive credentials.
* Payment instructions must not be stored in the core OS.
* Amount references must not be treated as automatic payment commands.
* External settlement preparation must require review.
* Compensation assessment must remain outside automatic execution.

A return route is not payment execution.

It is a reviewable value return pathway.

---

### 5.7 Representative Event

A Representative Event records agent-mediated activity.

Privacy requirements:

* Event logs should be auditable but not overexposing.
* Private evidence should not be embedded by default.
* Representative events should use references where possible.
* Logs should avoid storing sensitive wallet credentials.
* Logs should support governance review.

A representative event is not legal proof by itself.

It is an audit log entry.

---

### 5.8 Agent-Mediated Value Flow

An Agent-Mediated Value Flow connects all major records.

Privacy requirements:

* It should reference records rather than duplicate sensitive content.
* It should preserve review states.
* It should not expose private trace material unnecessarily.
* It should not convert the workflow into an execution process.

The integrated flow is a workflow map.

It is not a settlement engine.

---

## 6. Review States

Royalty OS v0.5 uses review states to prevent premature conclusions.

Common review states include:

```text
unreviewed
under_review
accepted_for_review
rejected
disputed
escalated
archived
resolved
```

Recommended interpretation:

```text
unreviewed = no conclusion
under_review = review is in progress
accepted_for_review = worth examining, not confirmed
rejected = not accepted for further routing
disputed = disagreement exists
escalated = moved to higher review
archived = preserved without active action
resolved = review process completed
```

The system should avoid collapsing review states into binary outcomes too early.

---

## 7. Confidence Levels

Confidence levels may include:

```text
unknown
low
medium
high
requires_human_review
```

Confidence is not proof.

A high confidence signal may justify deeper review.

It must not justify automatic enforcement.

Correct interpretation:

```text
high confidence = stronger review candidate
```

Incorrect interpretation:

```text
high confidence = automatic claim validity
```

The safest default for sensitive contexts is:

```text
requires_human_review
```

---

## 8. Minimal Disclosure Model

The minimal disclosure model has four layers.

### Layer 1 — Public Summary

A short description suitable for public or low-risk review.

Example:

```text
A possible conceptual overlap was detected between a registered trace and an AI-generated output.
```

### Layer 2 — Review Reference

A reference to supporting material without exposing raw data.

Example:

```text
evidence_references:
  - evidence:comparison:sample-001
```

### Layer 3 — Restricted Evidence

Evidence available only to authorized reviewers.

Example:

```text
private_evidence_included: true
external_sharing_requires_review: true
```

### Layer 4 — Sensitive Material

Highly restricted material that should not be included in core records.

Examples:

```text
private keys
wallet credentials
private drafts
private conversations
authentication tokens
```

Layer 4 material should remain outside core Royalty OS v0.5 records.

---

## 9. External Sharing Rules

External sharing should require review when the record involves:

* private trace data
* private evidence
* wallet references
* claim routes
* public attribution
* public accusation
* external settlement preparation
* legal interpretation
* compensation assessment
* platform reports

Recommended rule:

```text
external_sharing_requires_review: true
```

External sharing should not occur automatically.

---

## 10. Wallet Reference Privacy

Royalty OS v0.5 may include wallet references.

However, wallet references must not include:

* private keys
* seed phrases
* payment credentials
* authentication tokens
* account passwords
* executable payment instructions

Allowed:

```text
wallet_reference_id
wallet_type
wallet_reference_status
non-sensitive notes
```

Not allowed:

```text
private key
seed phrase
secret token
payment authorization credential
```

The core boundary is:

```text
Wallet reference is allowed.
Wallet credential storage is not allowed.
```

---

## 11. Evidence Handling

Evidence should be handled carefully.

Preferred structure:

```text
evidence_summary
evidence_references
private_evidence_included
review_status
```

Avoid:

```text
full private evidence dumps
unreviewed accusations
large raw content embeddings
sensitive data in public records
```

Evidence should support review.

Evidence should not replace review.

---

## 12. Public Disclosure Rules

Public disclosure requires review when it may affect:

* reputation
* attribution
* ownership interpretation
* claim validity
* compensation expectation
* external dispute
* legal or platform action

Before public disclosure, the system should confirm:

```text
human_review_required: true
public_disclosure reviewed
privacy impact reviewed
boundary policy preserved
```

Public disclosure should never be triggered automatically by a personal AI agent.

---

## 13. Review Before External Process

External processes may include:

* platform reports
* legal review
* settlement preparation
* public attribution request
* compensation negotiation
* payment execution
* governance escalation
* dispute handling

Royalty OS v0.5 may prepare references for these processes.

It must not execute them automatically.

Recommended sequence:

```text
candidate record
↓
human review
↓
governance review
↓
authorization
↓
external process
```

---

## 14. Privacy and Governance Relationship

Privacy and governance are connected.

Privacy protects the individual from overexposure.

Governance protects the system from premature or harmful action.

Together, they ensure that agent-mediated value routing remains responsible.

```text
Privacy = what should be exposed?
Governance = what should be done?
Review = who decides before action?
```

All three must work together.

---

## 15. Auditability Without Overexposure

Royalty OS v0.5 needs auditability.

But auditability should not mean exposing everything.

A good audit log should show:

* what action occurred
* which agent prepared it
* which record was affected
* what review status applies
* what boundary policy applies
* what evidence references exist

It should not expose:

* unnecessary raw private data
* wallet credentials
* sensitive evidence
* private keys
* excessive content

Recommended principle:

```text
Auditable does not mean fully exposed.
```

---

## 16. Implementation Guidelines

Implementations should follow these guidelines:

1. Default to minimal disclosure.
2. Use references instead of raw private data.
3. Use summaries instead of full content where possible.
4. Require human review before external sharing.
5. Require review before public disclosure.
6. Do not store sensitive wallet credentials.
7. Do not treat confidence as proof.
8. Do not treat detection as proof.
9. Preserve review states.
10. Log representative actions.
11. Keep private evidence separate from public records.
12. Separate review preparation from external execution.
13. Keep payment execution outside the core OS boundary.
14. Keep legal interpretation outside the automatic OS boundary.
15. Make all major route transitions auditable.

---

## 17. Non-Goals

The Privacy and Review Model does not provide:

* legal advice
* automatic legal judgment
* automatic evidence validation
* automatic privacy classification
* automatic payment authorization
* automatic public disclosure
* automatic platform reporting
* automatic settlement execution

It provides a structure for responsible handling, review, and disclosure boundaries.

---

## 18. Core Statement

The core statement of the Privacy and Review Model is:

```text
Expose less.
Reference more.
Review before action.
Log without overexposing.
Protect the individual first.
```

Royalty OS v0.5 can only function responsibly if personal traces, usage events, claims, return routes, and representative events are handled with privacy and review at the center.

In short:

```text
Privacy and Review Model
= the layer that protects individuals while allowing agent-mediated value relationships to be reviewed responsibly
```
