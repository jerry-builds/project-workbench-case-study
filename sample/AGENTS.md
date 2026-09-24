The certified Master specification is the authoritative product source: elm-street-clinic-front-desk-r2-PRD.md
This file explains how to use the specification with this tool. It is a specification handoff, not an implementation plan.
If this file conflicts with the certified Master, the Master controls.

## Reading Order

1. elm-street-clinic-front-desk-r2-PRD.md — the Master. Read overview, goals, requirements, surfaces, flows, scope, nonGoals, dataModel, roadmap, assumptions, and traceability, in that order, before writing code.
2. This file (AGENTS.md) — how to work the Master with an autonomous coding agent.
3. CLAUDE.md, lovable-project-knowledge.txt, replit.md, if present — tool-specific verification and environment notes layered on top of this file. They add no requirements of their own.

If any companion file appears to add a requirement, a role, a permission, or an acceptance condition the Master does not state, treat that as an error in the companion file. The Master controls.

## Inspect the Environment Before Choosing Anything

The Master's `stack` field is intentionally empty — no framework, database, or hosting choice is prescribed. Before writing code:

- Open the repository as it exists now. Check for an existing manifest, scaffold, folder layout, or partially built surfaces (Patient Portal, Receptionist Front Desk, Front-Desk Tablet Check-In, Nurse Day List, Clinician Schedule, Billing Clerk Console, Practice Manager Admin) before assuming a greenfield build.
- Check for existing configuration or credentials pointing at the four external systems the Master names: the clinic's patient records system (read-only, REQ-028), the messaging service (REQ-004, REQ-005, REQ-006), the billing system (one-way send, receipt-only read-back, REQ-013, REQ-032), and the shared calendar (one-way write, no read-back, REQ-033). Use what is already configured; do not invent a new integration contract for a system that already has one.
- If no environment exists yet, any stack, schema, or repository layout that satisfies every requirement and every acceptance criterion is acceptable. That is an implementation choice the Master leaves open, not a gap in the specification.

## Open Questions vs. Open Choices

The Master closed two questions already: Q-01 (keep the existing shared calendar, one-way feed only — REQ-033) and Q-02 (visit summary codes come from a practice-manager-maintained fixed list, never free text — REQ-012). Both are settled; do not reopen them.

For anything else:

- **Unresolved question that changes behavior, access, scope, or an acceptance criterion** — stop work on the affected requirement(s) only. Request clarification, citing the REQ-ID or DEC-ID in question. Keep working on unrelated requirements while waiting.
- **Implementation choice the Master leaves open** (which framework, how a screen lays out its fields, how the six roles are represented internally, how a read-only lookup call is structured) — inspect the environment, pick a workable option, and proceed, provided every requirement and acceptance criterion the choice touches is still met.

Example: the Master does not say how the fixed list of visit summary codes is stored. That is open — pick a way. The Master does say a clinician must select from that list and that free text must never be offered (REQ-012). That is not open.

## Evidence Per Acceptance Criterion

Every requirement, REQ-001 through REQ-034, carries acceptance criteria written as pass/fail pairs (for example: "the appointment is cancelled immediately and the slot becomes available (pass) / the appointment stays booked (fail)"). For each one implemented:

- Show the pass path actually occurs.
- Show the fail path is actually blocked, not just untested.
- Where a criterion names a role, check it from that role's own access, not from an administrative bypass.
- Where a criterion references a configurable value (reminder interval REQ-004, reschedule/cancel cutoff REQ-002, no-show grace period REQ-015), show the behavior before and after the practice manager changes that value.

## Constraints to Preserve, With Provenance

Carried forward from the client's decisions (DEC-XXX) and the prior self-audit resolutions (BR-01 through BR-12). Do not redesign these without a new client decision:

- One-way shared calendar feed only, no read-back, payload limited to patient name, time, duration, room, clinician, and appointment type (DEC-046, BR-01, BR-08, BR-09, REQ-033).
- Visit summary codes are a fixed, practice-manager-maintained list; no free text at visit completion (DEC-047, BR-06, REQ-012).
- Billing transmission carries only the summary code and visit date, sent automatically on visit completion; only a receipt confirmation is read back (DEC-044, DEC-040, BR-10, REQ-013).
- Intake form content never appears in any message or billing transmission (DEC-040, REQ-032).
- A submitted intake form and a completed visit record can never be deleted by any role, including the practice manager (DEC-029, DEC-039, REQ-007, REQ-031).
- The patient records system is read-only from this product — no writes, updates, or deletes to it (DEC-041, DEC-042, REQ-028).
- Staff accounts, across all five staff roles, are created only by the practice manager; patient accounts are created only by receptionist lookup against the records system, never self-registered (DEC-026, DEC-027, BR-05, REQ-027, REQ-029).
- The rolling six-month, three-no-show flag sets and lifts automatically, with no manual override step (DEC-014, ASM-009, BR-12, REQ-016).
- Clinician-absence rebooking copies the submitted intake form onto the new appointment and leaves the original unchanged on the cancelled one (DEC-022, BR-02, BR-11, ASM-008, REQ-024).
- Every staff action on an appointment or intake form is logged with actor identity and timestamp; log entries are never editable or deletable (DEC-019, REQ-021).
- Reminder confirm/cancel actions use a unique tokenized link per message, per REQ-005; how that token is generated and validated is an implementation choice left to the builder — the client declined to mandate a specific mechanism beyond ruling out free-text reply parsing being the only path.

Validation limit: the reschedule/cancel cutoff, the reminder interval, and the no-show grace period are each a single clinic-wide value the practice manager edits. Do not add per-appointment-type or per-clinician overrides of these three values unless a new client decision authorizes it.

## What This File Does Not Do

This file does not prescribe an architecture, a physical schema, a repository layout, a build or run command, a script, or a framework configuration. Any such document found elsewhere in the repository is a working note, not part of the specification, and does not override the Master.