# Decision Ledger — Clinic Front-Desk Operations Platform — Master PRD

Complete record of the approved scope baseline frozen at brief approval (before Master generation). IDs — including positional DEC/ASM numbering — match the frozen approved brief and every Master source citation exactly.

| ID | Status | Detail | Affected requirements |
| --- | --- | --- | --- |
| DEC-001 | Approved | Patients book an appointment by type with an available clinician and room; the slot becomes unavailable to other patients immediately on booking. | REQ-001 |
| DEC-002 | Approved | Patients can reschedule or cancel their own appointment up until a cut-off time set by the practice manager. | REQ-002 |
| DEC-003 | Approved | Receptionists can book, reschedule, and cancel an appointment on behalf of any patient, with no cut-off restriction. | REQ-003 |
| DEC-004 | Approved | Automated reminders are sent before each appointment at timing set by the practice manager, through the clinic's existing messaging service (text and email). | REQ-004 |
| DEC-005 | Approved | A reminder includes a way for the patient to confirm or cancel the appointment, and that response is applied immediately. | REQ-005 |
| DEC-006 | Approved | Patients complete an intake form before the visit; the form is attached to that specific appointment. | REQ-007 |
| DEC-007 | Approved | If the intake form is not completed ahead of time, the patient completes it on a tablet at the front desk during check-in. | REQ-008 |
| DEC-008 | Approved | Receptionists check a patient in on arrival; a checked-in patient appears on the nurse's list for that day. | REQ-009 |
| DEC-009 | Approved | Nurses can read a checked-in patient's intake form and mark that patient ready for the clinician. | REQ-010 |
| DEC-010 | Approved | Clinicians see patient readiness status on their own schedule. | REQ-011 |
| DEC-011 | Approved | Clinicians mark a visit complete and record a visit summary code at that time. | REQ-012 |
| DEC-012 | Approved | The billing clerk sees completed visits with their summary codes and marks each as sent to billing. | REQ-014 |
| DEC-013 | Approved | Receptionists mark a patient as a no-show after a grace period (set by the practice manager) has passed with no arrival. | REQ-015 |
| DEC-014 | Approved | A patient with three no-shows within six months is automatically flagged; only a receptionist can book a further appointment for that patient while flagged. | REQ-016 |
| DEC-015 | Approved | The practice manager sets clinic hours, rooms, appointment types, and appointment durations. | REQ-017 |
| DEC-016 | Approved | Rooms cannot be double-booked, and the schedule view shows room assignment for each appointment. | REQ-018 |
| DEC-017 | Approved | Clinicians cannot be double-booked across appointments. | REQ-019 |
| DEC-018 | Approved | The monthly report available to the practice manager shows visits, cancellations, no-shows, and average wait between check-in and ready, broken down per clinician. | REQ-020 |
| DEC-019 | Approved | Every staff action taken on an appointment or intake form is logged with the acting user's identity and a timestamp. | REQ-021 |
| DEC-020 | Approved | The practice manager can deactivate a staff account without deleting that staff member's history of past actions. | REQ-022 |
| DEC-021 | Approved | A room, appointment type, or clinician with future appointments cannot be removed or deactivated until those appointments are moved or cancelled. | REQ-023 |
| DEC-022 | Approved | When a clinician is marked absent, their future slots are blocked from new booking, existing affected appointments are cancelled by the clinic, and the receptionist is shown those appointments and rebooks each patient into a new slot. | REQ-024 |
| DEC-023 | Approved | A patient who arrives after a cancellation caused by clinician absence is told the appointment is no longer active and is offered the next available slots to rebook, instead of being checked in. | REQ-025 |
| DEC-024 | Approved | A patient arriving after the no-show grace period can still be checked in, but the appointment is flagged as late for the nurse and clinician to see. | REQ-026 |
| DEC-025 | Approved | Patients receive a confirmation message when their appointment is booked, moved, or cancelled. | REQ-006 |
| DEC-026 | Approved | Patient accounts are created only by a receptionist, who looks the patient up in the clinic's existing patient records system and sends an invitation for the patient to set a password; patients cannot self-register. | REQ-027 |
| DEC-027 | Approved | Staff accounts are created only by the practice manager. | REQ-029 |
| DEC-028 | Approved | Role permissions: patients see only their own appointments and forms; receptionists see the day's full schedule and cannot see clinical notes or change billing codes; nurses see only the day's checked-in patients and cannot book appointments; clinicians see only their own schedule and their own patients' intake forms; the billing clerk sees completed visits and summary codes only, never intake form contents; the practice manager sees all schedules and reports but does not record clinical information. | REQ-010, REQ-011, REQ-014, REQ-030 |
| DEC-029 | Approved | A completed visit and a submitted intake form can never be deleted by any user. | REQ-007, REQ-031 |
| DEC-030 | Approved | Non-goal, deferred to a later version: online payment. | — |
| DEC-031 | Approved | Non-goal, deferred to a later version: a patient portal for viewing test results. | — |
| DEC-032 | Approved | Non-goal, deferred to a later version: telephone-call reminders. | — |
| DEC-033 | Approved | Non-goal, deferred to a later version: waiting-list management. | — |
| DEC-034 | Approved | Non-goal, deferred to a later version: clinical note-taking of any kind. | — |
| DEC-035 | Approved | Prohibition, must never happen in any version: a room or clinician is ever double-booked. | REQ-018, REQ-019 |
| DEC-036 | Approved | Prohibition, must never happen in any version: a patient can see another patient's appointments or intake forms. | REQ-002, REQ-030 |
| DEC-037 | Approved | Prohibition, must never happen in any version: a receptionist or the billing clerk can see intake form contents. | REQ-014, REQ-030 |
| DEC-038 | Approved | Prohibition, must never happen in any version: a clinician can see another clinician's intake forms. | REQ-030 |
| DEC-039 | Approved | Prohibition, must never happen in any version: a completed visit or submitted intake form is deleted. | REQ-007, REQ-031 |
| DEC-040 | Approved | Prohibition, must never happen in any version: intake form contents are sent to the billing system or the messaging service. | REQ-013, REQ-032 |
| DEC-041 | Approved | Prohibition, must never happen in any version: the product writes or changes any data in the clinic's patient records system. | REQ-028 |
| DEC-042 | Approved | Integration: the product reads patient name and contact details from the existing patient records system for display only; it never writes to that system. | REQ-028 |
| DEC-043 | Approved | Integration: the product sends reminders and confirmations through the clinic's existing messaging service and records whether each message was sent. | REQ-004, REQ-006 |
| DEC-044 | Approved | Integration: on visit completion, the product sends the visit summary code and date to the clinic's billing system and reads back only a receipt confirmation. | REQ-013 |
| DEC-045 | Approved | The product must operate well on small touch-screen tablets, since staff use it at the front desk on tablets. | REQ-008, REQ-034 |
| DEC-046 | Approved | Integration: the clinic's existing shared calendar is kept in place; the product writes appointment data into it one-way so clinicians keep one familiar view, and the product never reads bookings from that calendar. | REQ-033 |
| DEC-047 | Approved | The practice manager maintains a fixed list of visit summary codes, alongside appointment types and rooms; clinicians select a code from that list when completing a visit rather than typing free text. | REQ-012, REQ-017 |
| ASM-001 | Approved | Any active clinician can be scheduled for any appointment type; the practice manager is not required to restrict specific types to specific clinicians in v1. | — |
| ASM-002 | Approved | The no-show grace period and the patient self-service cut-off are single clinic-wide values, not configured separately per appointment type, in v1. | — |
| ASM-003 | Approved | The clinic operates from a single site; multi-location scheduling is not required. | — |
| ASM-004 | Approved | The monthly report is viewed on demand inside the product by the practice manager; it is not emailed automatically. | REQ-020 |
| ASM-005 | Approved | The practice manager does not book, reschedule, or check in patients directly; those actions are performed by receptionists, consistent with the manager's stated scope of configuration and reporting. | — |
| ASM-006 | Approved | Only scheduling-relevant fields — patient name, appointment time, duration, room, clinician, and appointment type — are written to the external shared calendar feed; intake form contents, visit summary codes, and billing information are never included in that feed. | REQ-033 |
| ASM-007 | Approved | The clinician permission restriction limiting visibility to a clinician's own patients applies only within the product's own interface; the external shared calendar kept per the client's Q-01 decision retains its pre-existing shared, clinic-wide visibility across all clinicians and is not restricted by in-product role permissions. | REQ-033 |
| ASM-008 | Approved | When a clinician-absence cancellation triggers a rebooking, the product automatically copies the patient's already-submitted intake form onto the new appointment rather than requiring resubmission; the original form instance remains attached to the cancelled appointment as an unchanged historical record, and the patient may edit the copy before the new visit. | REQ-024 |
| ASM-009 | Approved | The three-no-shows-in-six-months flag is evaluated dynamically against a rolling six-month window from the current date; the flag lifts automatically once fewer than three no-shows remain within the trailing six months, with no manual unflag action required from staff. | REQ-016 |
| BR-01 | Resolved | Keep the existing shared calendar as the source clinicians already trust, and have the product write into it while never reading bookings from it. (client decision via Q-01) | REQ-033 |
| BR-02 | Resolved | Clinician-absence handling implemented as cancel-then-rebook, presented to receptionists as moving affected appointments; all three cited statements remain true under this single behavior. | REQ-024 |
| BR-03 | Resolved | Reminders include a unique confirm link and a unique cancel link per appointment; tapping either applies the response immediately without requiring reply-text parsing. (recommended and disclosed during audit) | REQ-005 |
| BR-04 | Rejected | Staff directory integration excluded from v1 scope; staff accounts are created manually by the practice manager as stated in the firm decision. (recommended and disclosed during audit) | — |
| BR-05 | Resolved | Account creation is blocked until a matching patient exists in the records system; no fallback manual-entry account creation is provided in this product. (recommended and disclosed during audit) | REQ-027 |
| BR-06 | Resolved | Practice manager maintains a fixed list of visit summary codes; clinicians select from that list when completing a visit. (client decision via Q-02) | REQ-012 |
| BR-07 | Resolved | Single-site scope confirmed as the default; recorded as assumption ASM-003. (auto-resolved during audit) | — |
| BR-08 | Resolved | The calendar write feed is limited to patient name, appointment time, duration, room, clinician, and appointment type; intake form contents, visit summary codes, and billing information are excluded from the feed, consistent with the existing prohibition on sending intake data to other external systems. (recommended and disclosed during audit) | REQ-033 |
| BR-09 | Resolved | Recorded as a compatible reading: the in-product rule that a clinician cannot see another clinician's patients (DEC-028) governs the product's own interface only, and the external shared calendar kept per the client's Q-01 answer keeps its pre-existing shared, clinic-wide visibility, limited to the minimum scheduling fields already defined for that feed (patient name, time, duration, room, clinician, appointment type), never intake or billing data. | REQ-033 |
| BR-10 | Resolved | Applied as a compatible reading: the product automatically sends the visit summary code and date to the billing system the moment a clinician marks a visit complete, satisfying the mandatory integration requirement, and the billing clerk's manual 'mark as sent to billing' action remains a separate in-product status the clerk sets when reviewing completed visits, used for their own tracking and never gating or duplicating the automatic transmission. | REQ-013, REQ-014 |
| BR-11 | Resolved | The product copies the patient's already-submitted intake form onto the new appointment created during a clinician-absence rebooking; the original form stays attached to the cancelled appointment as an untouched historical record, and the patient can edit the copy before the new visit if needed. (recommended and disclosed during audit) | REQ-024 |
| BR-12 | Resolved | The no-show flag is recalculated from a rolling six-month window; it lifts automatically once fewer than three no-shows remain within the trailing six months, and no manual staff action is provided to remove it. (recommended and disclosed during audit) | REQ-016 |
| Q-01 | Resolved | The intake says the existing shared calendar 'will be replaced,' but also requires the product to show appointments inside 'the clinicians' shared calendar' so clinicians keep one view. Should the old shared calendar be fully retired, or should it continue to exist as a read-only display target the product feeds into? → Keep the existing shared calendar as the source clinicians already trust, and have the product write into it while never reading bookings from it. | — |
| Q-02 | Resolved | Where do visit summary codes come from when a clinician completes a visit: a fixed list the practice manager maintains, or free text the clinician types? → Practice manager maintains a fixed list of visit summary codes; clinicians select from that list when completing a visit. | — |

Open items: none.

Statuses: **Approved** = frozen baseline source cited by Master requirements; **Resolved** = settled during discovery or reconciliation; **Rejected** = unapproved scope expansion excluded from v1; **Open** = awaiting a client decision (none can remain after brief approval).

## Authority

In any conflict the Master controls: `elm-street-clinic-front-desk-r2-PRD.md` is the authoritative document, and its approved-scope citations decide disputes. This ledger records the approved scope baseline; it does not override the specification derived from it.