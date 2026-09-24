The certified Master specification is the authoritative product source: elm-street-clinic-front-desk-r2-PRD.md
This file explains how to use the specification with this tool. It is a specification handoff, not an implementation plan.
If this file conflicts with the certified Master, the Master controls.

## Reading Order

1. elm-street-clinic-front-desk-r2-PRD.md — the Master. Read overview, goals, requirements, surfaces, flows, scope, nonGoals, dataModel, roadmap, assumptions, and traceability, in that order, before writing code.
2. This file (CLAUDE.md) — tool-specific verification and environment notes for working the Master with Claude Code. It adds no requirements of their own.
3. AGENTS.md, lovable-project-knowledge.txt, replit.md, if present — layered notes for other tools; consult AGENTS.md for the general agent-handoff conventions this file assumes.

## Environment Inspection

The Master's `stack` field is empty on purpose — no framework, database, or hosting choice is prescribed. Before writing or changing code in a Claude Code session:

- Open the repository as it exists now. Check for an existing manifest, scaffold, folder layout, or partially built surfaces (Patient Portal, Receptionist Front Desk, Front-Desk Tablet Check-In, Nurse Day List, Clinician Schedule, Billing Clerk Console, Practice Manager Admin) before assuming a greenfield build.
- Check for existing configuration or credentials pointing at the four external systems the Master names: the clinic's patient records system (read-only, REQ-028), the messaging service (REQ-004, REQ-005, REQ-006), the billing system (one-way send, receipt-only read-back, REQ-013, REQ-032), and the shared calendar (one-way write, no read-back, REQ-033). Use what is already configured; do not invent a new integration contract for a system that already has one.
- If no environment exists yet, any stack, schema, or repository layout that satisfies every requirement and every acceptance criterion is acceptable. That is an implementation choice the Master leaves open, not a gap in the specification.

## Open Questions vs. Open Choices

The Master closed two questions already: Q-01 (keep the existing shared calendar, one-way feed only — REQ-033) and Q-02 (visit summary codes come from a practice-manager-maintained fixed list, never free text — REQ-012). Both are settled; do not reopen them.

For anything else found while working in this session:

- **Unresolved question that changes behavior, access, scope, or an acceptance criterion** — stop work on the affected requirement(s) only. Request clarification, citing the REQ-ID or DEC-ID in question. Keep working on unrelated requirements while waiting.
- **Implementation choice the Master leaves open** (which framework, how a screen lays out its fields, how the six roles are represented internally, how a read-only lookup call is structured) — inspect the environment, pick a workable option, and proceed, provided every requirement and acceptance criterion the choice touches is still met.

## Verifying Work Against the Specification

- Treat each of the Master's requirements, REQ-001 through REQ-034, as a checklist item. Before marking one done, restate its acceptance criteria and confirm both the pass condition and the fail condition were actually exercised, not just the pass condition.
- Where a criterion gives two conditions for the same requirement (for example REQ-002's before-cutoff versus at-or-after-cutoff behavior, or REQ-015's before-grace-period versus after-grace-period behavior), test both sides in the same pass. A single successful run against one side is not coverage.
- Check role-scoped visibility (REQ-030) directly for every screen touched: confirm what a patient, receptionist, nurse, clinician, billing clerk, and practice manager each see from it, not only the role the work started from.
- Check the "never" constraints separately, since they are easy to break while adding an unrelated feature: intake content never reaches a message or a billing transmission (REQ-032), no delete path exists for a submitted intake form or a completed visit (REQ-031), and audit log entries are never editable or deletable (REQ-021).
- When a practice-manager-configurable value changes — clinic hours, the reschedule/cancel cutoff, the no-show grace period, the reminder interval, rooms, appointment types, durations, or the visit summary code list (REQ-017) — confirm the new value applies to future evaluations without altering records already tied to the old value.
- If two parts of the Master appear to conflict, stop and flag it by citing both REQ-IDs, rather than picking one silently.
- Report a requirement complete based on its specific pass/fail behavior having been checked, not based on the code existing.