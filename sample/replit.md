The certified Master specification is the authoritative product source: elm-street-clinic-front-desk-r2-PRD.md
This file explains how to use the specification with this tool. It is a specification handoff, not an implementation plan.
If this file conflicts with the certified Master, the Master controls.

## Reading Order

1. elm-street-clinic-front-desk-r2-PRD.md — the Master. It is the sole authoritative source for requirements, acceptance criteria, roles, surfaces, and flows.
2. This file (replit.md) — a self-contained handoff for working the Master inside a Replit Agent session. It states no requirement the Master does not already state; where the two disagree, the Master controls.

## Inspect the Environment Before Choosing Anything

The Master's `stack` field is empty on purpose — it prescribes no language, framework, database, or hosting setup. Before writing code in this Repl:

- Check what already exists: any existing files, any existing secrets or environment variables, any partially built screens for the six roles (Patient, Receptionist, Nurse, Clinician, Billing Clerk, Practice Manager).
- Check for existing configuration pointing at the four external systems the Master names: the clinic's patient records system (read-only, REQ-028), the messaging service (REQ-004, REQ-005, REQ-006), the billing system (one-way send, receipt-only read-back, REQ-013, REQ-032), and the shared calendar (one-way write, no read-back, REQ-033). Use what is already configured; do not invent a new integration contract for a system that already has one.
- If the Repl is empty, any stack or layout that satisfies every requirement and acceptance criterion is acceptable — that is an implementation choice the Master leaves open, not a specification gap.

## Open Questions vs. Open Choices

The client already answered two open questions in the Master: Q-01 keeps the existing shared calendar in place with a one-way feed from this product (REQ-033); Q-02 fixes visit summary codes to a practice-manager-maintained list, never free text (REQ-012). Do not reopen either.

For anything else found while building:

- **If an unresolved point would change behavior, access, scope, or an acceptance criterion** — pause work on that specific requirement, request clarification citing the REQ-ID or DEC-ID, and continue working on unrelated requirements in the meantime.
- **If the Master simply leaves an implementation choice open** — inspect the Repl's current state, pick an option, and proceed, as long as the requirements and acceptance criteria the choice touches are still met.

## Evidence Per Acceptance Criterion

Every requirement, REQ-001 through REQ-034, states acceptance criteria as pass/fail pairs. For each one built or modified in this Repl:

- Confirm the pass path actually happens.
- Confirm the paired fail path is actually blocked, not merely unexercised.
- Where a criterion names a role, verify it from that role's own access.
- Where a criterion references a practice-manager-configurable value (reminder interval, reschedule/cancel cutoff, no-show grace period), verify behavior both before and after the value changes.

## Constraints to Preserve, With Provenance

Carried from the client's decisions (DEC-XXX) and prior self-audit resolutions (BR-01 through BR-12):

- One-way shared calendar feed, no read-back, payload limited to patient name, time, duration, room, clinician, appointment type (DEC-046, BR-01, BR-08, BR-09, REQ-033).
- Visit summary codes are a fixed, practice-manager-maintained list; no free text (DEC-047, BR-06, REQ-012).
- Billing transmission carries only summary code and visit date, automatic on visit completion; only a receipt confirmation is read back (DEC-044, DEC-040, BR-10, REQ-013).
- Intake content never appears in a message or a billing transmission (DEC-040, REQ-032).
- A submitted intake form and a completed visit record can never be deleted by any role (DEC-029, DEC-039, REQ-007, REQ-031).
- The patient records system is read-only from this product (DEC-041, DEC-042, REQ-028).
- Staff accounts are created only by the practice manager; patient accounts are created only by receptionist lookup against the records system (DEC-026, DEC-027, BR-05, REQ-027, REQ-029).
- The rolling six-month, three-no-show flag sets and lifts automatically, with no manual override (DEC-014, ASM-009, BR-12, REQ-016).
- Clinician-absence rebooking copies the submitted intake form onto the new appointment, leaving the original unchanged on the cancelled one (DEC-022, BR-02, BR-11, ASM-008, REQ-024).
- Every staff action on an appointment or intake form is logged with actor identity and timestamp; log entries are never editable or deletable (DEC-019, REQ-021).
- Reminder confirm/cancel links use a unique token per message (REQ-005); the client left the token generation and validation mechanism itself open, only ruling out relying on free-text reply parsing as the sole path.

Validation limit: the reschedule/cancel cutoff, the reminder interval, and the no-show grace period are each a single clinic-wide value. Do not add per-type or per-clinician overrides of these three without a new client decision.

## What This File Does Not Do

It does not prescribe an architecture, a physical schema, a repository layout, a run command, a script, or a Replit configuration. Any such content found elsewhere in this Repl is a working note, not specification content, and does not override the Master.