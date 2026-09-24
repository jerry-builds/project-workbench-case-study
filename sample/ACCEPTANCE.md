# Acceptance Checklist — Clinic Front-Desk Operations Platform — Master PRD

Every criterion below is copied verbatim from the Master PRD (revision 2). Sources cite the approved scope baseline; the complete decision record ships as `DECISIONS.md`.

**What has been checked, and what has not.** What we verified is the *specification*: that each criterion is stated in observable pass/fail terms, that it traces to an approved decision, and that nothing here contradicts the Master. **Every box below is unchecked because it is yours to check.** No software was built, run, tested or deployed to produce this package, and no environment was assessed, so nothing here reports that an implementation satisfies a criterion. Tick a box when you have produced the evidence it names, in your own stack's terms.

## Milestone: M2: Core Scheduling & Configuration

### REQ-001
Patients can book an appointment by selecting an appointment type; the system assigns an available clinician and room, and the slot becomes unavailable to other patients immediately on booking.

**Sources:** DEC-001

- [ ] Given an appointment type with an available clinician+room+time combination, when a patient submits a booking, the system creates the appointment and that slot is no longer offered to other patients (pass) / the slot remains bookable by another patient (fail).
- [ ] Given no slot matches the requested type, the patient cannot submit a booking for it (pass) / a conflicting booking is created (fail).

### REQ-002
Patients can reschedule or cancel only their own appointment, and only before a practice-manager-configured cutoff time.

**Sources:** DEC-002, DEC-036

- [ ] Given the current time is before the cutoff, a patient can reschedule or cancel their own appointment (pass) / the action is blocked (fail).
- [ ] Given the current time is at or after the cutoff, reschedule/cancel controls are unavailable to the patient (pass) / the change still succeeds (fail).
- [ ] A patient cannot reschedule or cancel another patient's appointment (pass) / another patient's appointment is editable (fail).
- [ ] Given the practice manager edits the cutoff time, the new value applies to future reschedule/cancel eligibility checks (pass) / the previous cutoff value continues to apply (fail).

### REQ-003
Receptionists can book, reschedule, and cancel an appointment on behalf of any patient, at any time, with no cutoff restriction.

**Sources:** DEC-003

- [ ] Given any time relative to an appointment, a receptionist can reschedule or cancel it (pass) / the cutoff blocks the receptionist (fail).
- [ ] A receptionist can create a new booking for any looked-up patient (pass) / booking on behalf of a patient is unavailable (fail).

### REQ-017
The practice manager configures clinic hours, rooms, appointment types, appointment durations, and the fixed list of visit summary codes; only the practice manager role can edit these.

**Sources:** DEC-015, DEC-047

- [ ] Given a practice manager adds, edits, or removes a room, type, duration, or summary code, the change is reflected immediately in booking and completion screens (pass) / stale values persist (fail).
- [ ] No other role has access to these configuration controls (pass) / another role can edit them (fail).
- [ ] Given a practice manager edits clinic hours, the new hours apply to future booking availability (pass) / the previous hours still apply (fail).

### REQ-018
The system never permits two appointments to hold the same room at overlapping times, and every schedule view shows each appointment's assigned room.

**Sources:** DEC-016, DEC-035

- [ ] Given a room is booked for a time range, a second booking for that room in an overlapping range is rejected (pass) / it succeeds (fail).
- [ ] Every appointment entry in schedule views shows its assigned room (pass) / the room is missing (fail).

### REQ-019
The system never permits a clinician to hold two appointments with overlapping times.

**Sources:** DEC-017, DEC-035

- [ ] Given a clinician is booked for a time range, a second booking for that clinician in an overlapping range is rejected (pass) / it succeeds (fail).

### REQ-023
The system blocks removal or deactivation of a room, appointment type, or clinician that has future appointments, until those appointments are moved or cancelled.

**Sources:** DEC-021

- [ ] Given a room, type, or clinician has a future appointment, a removal/deactivation attempt is rejected and the future appointments are identified (pass) / removal succeeds anyway (fail).
- [ ] Given all future appointments for that entity are moved or cancelled, the removal/deactivation attempt then succeeds (pass) / it remains blocked (fail).

## Milestone: M3: Reminders & Confirmations

### REQ-004
The system sends an automated text and email reminder before each appointment, at an interval the practice manager configures, through the clinic's existing messaging service, and records whether each reminder was sent.

**Sources:** DEC-004, DEC-043

- [ ] Given the configured interval, both a text and an email reminder are sent that far ahead of each appointment (pass) / no reminder is sent (fail).
- [ ] Every reminder send attempt is recorded with a sent or not-sent status (pass) / no record exists (fail).
- [ ] Given the practice manager edits the reminder interval, reminders for future appointments use the new interval (pass) / the previous interval still applies (fail).

### REQ-005
Each reminder includes a unique confirm link and a unique cancel link; tapping either applies the patient's response to that appointment immediately.

**Sources:** DEC-005, BR-03

- [ ] Given a patient taps the confirm link, the appointment status updates to confirmed immediately (pass) / it remains unconfirmed (fail).
- [ ] Given a patient taps the cancel link, the appointment is cancelled immediately and the slot becomes available (pass) / the appointment stays booked (fail).
- [ ] A link cannot be used to affect a different patient's appointment (pass) / it does (fail).

### REQ-006
Patients receive a confirmation message through the messaging service whenever their appointment is booked, moved, or cancelled, whether the action was taken by the patient or by staff.

**Sources:** DEC-025, DEC-043

- [ ] Given a receptionist reschedules a patient's appointment, the patient receives a confirmation reflecting the new time (pass) / no message is sent (fail).
- [ ] Given any booking, reschedule, or cancellation event, a message send attempt is recorded (pass) / no record exists (fail).

## Milestone: M4: Intake & Check-In

### REQ-007
A patient completes an intake form before the visit, and each submitted form instance attaches to one specific appointment; a submitted form can never be deleted.

**Sources:** DEC-006, DEC-029, DEC-039

- [ ] Given a patient submits an intake form for an appointment, the form is retrievable from that appointment record (pass) / it is unlinked (fail).
- [ ] A submitted intake form cannot be deleted by any user through the product (pass) / a delete action succeeds (fail).

### REQ-008
If the intake form was not completed ahead of the visit, the patient completes it on a tablet at the front desk during check-in, and the completed form attaches to that same appointment.

**Sources:** DEC-007, DEC-045

- [ ] Given an appointment with no submitted intake form at arrival, the check-in flow presents the intake form on the front-desk tablet (pass) / check-in proceeds without collecting it (fail).
- [ ] The tablet intake screen fits a small touch-screen viewport with no horizontal scrolling of fields (pass) / fields overflow the viewport (fail).

### REQ-009
A receptionist checks a patient in on arrival, and the checked-in patient appears on the nurse's list for that day.

**Sources:** DEC-008

- [ ] Given a receptionist marks a patient checked-in, the patient appears on the nurse's day list without manual refresh action (pass) / the patient does not appear (fail).
- [ ] The nurse's list shows only today's checked-in patients (pass) / it shows other days' patients (fail).

### REQ-010
A nurse can read a checked-in patient's intake form and mark that patient ready for the clinician; a nurse cannot book, reschedule, or cancel appointments.

**Sources:** DEC-009, DEC-028

- [ ] Given a nurse opens a checked-in patient's record, the submitted intake form content is viewable (pass) / it is hidden (fail).
- [ ] Given a nurse marks a patient ready, that status appears on the assigned clinician's schedule (pass) / it does not propagate (fail).
- [ ] No booking, reschedule, or cancel control is available to the nurse role (pass) / one is available (fail).

### REQ-011
A clinician sees patient readiness status directly on their own daily schedule, and sees only their own appointments.

**Sources:** DEC-010, DEC-028

- [ ] Given a nurse marks a patient ready, the ready indicator appears on that clinician's schedule for that appointment (pass) / it does not appear (fail).
- [ ] A clinician's schedule shows only appointments assigned to that clinician (pass) / it shows another clinician's appointments (fail).

## Milestone: M5: Visit Completion & Billing

### REQ-012
A clinician marks a visit complete and, at that time, must select a visit summary code from the practice-manager-maintained fixed list; free-text entry is not offered.

**Sources:** DEC-011, DEC-047, BR-06

- [ ] Given a clinician completes a visit, completion requires selecting one code from the configured list first (pass) / completion succeeds with no code (fail).
- [ ] The code selection control has no free-text entry field (pass) / a free-text field is present (fail).

### REQ-013
The moment a clinician marks a visit complete, the system automatically sends only the visit summary code and visit date to the clinic's billing system and reads back only a receipt confirmation, with no intake content included.

**Sources:** DEC-044, DEC-040, BR-10

- [ ] Given a visit is marked complete, a transmission with only the code and date is sent to billing without manual clerk action (pass) / no transmission occurs until a clerk acts (fail).
- [ ] Only a receipt confirmation is stored from the billing system's response (pass) / additional billing-system data is stored (fail).
- [ ] No intake form content appears in the transmission (pass) / it does (fail).

### REQ-014
The billing clerk sees completed visits with their summary codes and dates only, never intake form contents, and can manually mark each visit as sent to billing as a status separate from the automatic transmission.

**Sources:** DEC-012, DEC-028, DEC-037, BR-10

- [ ] A completed visit's entry for the billing clerk shows only date and summary code, no intake content (pass) / intake content is visible (fail).
- [ ] Given the billing clerk marks a visit as sent to billing, that status is stored distinct from the automatic transmission status and does not alter or repeat it (pass) / it interferes with the automatic transmission (fail).

### REQ-032
Intake form contents are never included in any message sent through the messaging service or any data sent to the billing system.

**Sources:** DEC-040

- [ ] Given a reminder or confirmation message is generated, its content contains only scheduling information, never intake fields (pass) / intake data appears (fail).
- [ ] Given a billing transmission is generated on visit completion, its payload contains only the summary code and date, never intake fields (pass) / intake data appears (fail).

## Milestone: M6: No-Show & Absence Handling

### REQ-015
A receptionist can mark a patient as a no-show only after a practice-manager-configured grace period has elapsed past the appointment start time with no arrival recorded.

**Sources:** DEC-013

- [ ] Given the grace period has not elapsed, the no-show action is unavailable (pass) / it is available (fail).
- [ ] Given the grace period has elapsed with no check-in, a receptionist can mark the appointment as a no-show (pass) / the action is blocked (fail).
- [ ] Given the practice manager edits the grace period, future no-show eligibility checks use the new value (pass) / the previous grace period still applies (fail).

### REQ-016
The system automatically flags a patient on the third no-show within a rolling six-month window and automatically lifts the flag once fewer than three no-shows remain in that trailing window; while flagged, only a receptionist can create a new booking for that patient.

**Sources:** DEC-014, ASM-009, BR-12

- [ ] Given a patient's third no-show falls within the trailing six months, the flag is set without staff action (pass) / it requires a manual step (fail).
- [ ] Given re-evaluation finds fewer than three no-shows in the trailing six months, the flag is removed automatically (pass) / it stays set (fail).
- [ ] While flagged, a patient-initiated booking attempt is rejected and a receptionist-initiated booking still succeeds (pass) / the patient can self-book while flagged (fail).

### REQ-024
When a clinician is marked absent for a date range, the system blocks new bookings for that clinician's future slots in the range, cancels existing affected appointments, presents the receptionist with the affected list to rebook, and copies each affected patient's already-submitted intake form onto the newly created appointment while leaving the original form unchanged on the cancelled appointment.

**Sources:** DEC-022, BR-02, BR-11, ASM-008

- [ ] Given a clinician is marked absent for a date range, no new booking can be created for that clinician in that range (pass) / one succeeds (fail).
- [ ] Given existing appointments fall in that range, each is cancelled and listed for the receptionist to rebook (pass) / an affected appointment is left unresolved or unlisted (fail).
- [ ] Given an affected appointment had a submitted intake form, the new appointment carries an editable copy of it while the original stays unchanged on the cancelled appointment (pass) / the new appointment has no form or the original is altered (fail).

### REQ-025
A patient who arrives for an appointment cancelled due to clinician absence is told the appointment is no longer active and is offered the next available slots to rebook, instead of being checked in.

**Sources:** DEC-023

- [ ] Given a patient arrives for a cancelled-due-to-absence appointment, the check-in screen shows an inactive-appointment message with next-available-slot options instead of a check-in confirmation (pass) / the patient is checked in normally (fail).

### REQ-026
A patient who arrives after the no-show grace period, but before being marked no-show, can still be checked in, with the appointment flagged as late for the nurse and clinician.

**Sources:** DEC-024

- [ ] Given a patient arrives after the grace period but before a no-show mark, a receptionist can check the patient in (pass) / check-in is blocked (fail).
- [ ] Given that check-in, a late flag is visible on both the nurse's list and the clinician's schedule for that appointment (pass) / the flag is missing from either view (fail).

## Milestone: M7: Reporting & Audit

### REQ-020
The practice manager can view an on-demand monthly report showing visits, cancellations, no-shows, and average wait between check-in and ready, broken down per clinician; the report is not emailed automatically.

**Sources:** DEC-018, ASM-004

- [ ] Given a selected month, the report displays all four metrics broken out per clinician (pass) / a metric or breakdown is missing (fail).
- [ ] The report is viewed on demand inside the product (pass) / an automatic email is sent instead or as well (fail).

### REQ-021
Every staff action on an appointment or intake form is logged with the acting user's identity and a timestamp, and log entries cannot be edited or deleted through the product.

**Sources:** DEC-019

- [ ] Given a staff member books, reschedules, cancels, checks in, marks ready, completes a visit, or marks no-show, a log entry records the user identity and timestamp (pass) / no entry is created (fail).
- [ ] No interface control allows editing or deleting a log entry (pass) / one exists (fail).

### REQ-022
The practice manager can deactivate a staff account; deactivation blocks login but preserves that user's logged history of past actions.

**Sources:** DEC-020

- [ ] Given a practice manager deactivates a staff account, that account can no longer log in (pass) / login still succeeds (fail).
- [ ] All prior logged actions by that user remain visible in audit records after deactivation (pass) / they disappear (fail).

### REQ-031
No role, including the practice manager, can delete a completed visit record or a submitted intake form.

**Sources:** DEC-029, DEC-039

- [ ] Given any role attempts to delete a completed visit, no delete control is available and the attempt fails (pass) / deletion succeeds (fail).
- [ ] Given any role attempts to delete a submitted intake form, no delete control is available and the attempt fails (pass) / deletion succeeds (fail).

## Milestone: M1: Accounts & Access

### REQ-027
A receptionist creates a patient account only by looking the patient up in the clinic's existing patient records system and sending a password-setup invitation; patients cannot self-register; if no match is found, no account is created.

**Sources:** DEC-026, BR-05

- [ ] Given a receptionist finds a matching patient in the records system, a password-setup invitation is sent to that patient (pass) / none is sent (fail).
- [ ] No self-registration entry point exists in the product (pass) / one exists (fail).
- [ ] Given a records-system search returns no match, the account-creation action is unavailable and no local account is created (pass) / one is created anyway (fail).

### REQ-028
The system reads patient name and contact details from the clinic's existing patient records system for display only, and never writes to that system.

**Sources:** DEC-042, DEC-041

- [ ] Given a patient record is displayed, the name and contact details match the records-system source (pass) / they diverge without an update (fail).
- [ ] No product action results in a write, update, or delete call to the patient records system (pass) / one occurs (fail).

### REQ-029
Staff accounts, across all five staff roles, are created only by the practice manager; no other role or automated source creates them.

**Sources:** DEC-027

- [ ] Given a practice manager creates a staff account with an assigned role, that account can log in with that role's permissions (pass) / a non-practice-manager role can create a staff account (fail).

### REQ-030
The system enforces role-scoped access: patients see only their own appointments and forms; receptionists see the full day schedule but not clinical notes or billing codes; nurses see only today's checked-in patients and cannot book; clinicians see only their own schedule and their own patients' intake forms; the billing clerk sees only completed visits and summary codes, never intake content; the practice manager sees all schedules and reports but records no clinical information.

**Sources:** DEC-028, DEC-036, DEC-037, DEC-038

- [ ] Given a patient attempts to view another patient's appointment or form, access is denied (pass) / granted (fail).
- [ ] Given a receptionist attempts to view intake form contents or change a billing code, the action is denied (pass) / it succeeds (fail).
- [ ] Given a clinician attempts to view another clinician's intake forms, access is denied (pass) / granted (fail).
- [ ] Given the billing clerk attempts to view intake form contents, access is denied (pass) / granted (fail).
- [ ] No control for recording clinical information is available to the practice manager role (pass) / one exists (fail).

## Milestone: M8: Calendar Integration & Tablet Optimization

### REQ-033
The system writes appointment scheduling data (patient name, time, duration, room, clinician, appointment type) into the clinic's existing shared calendar one-way on create, reschedule, and cancel, never reads bookings back from it, and excludes intake content, summary codes, and billing information from the feed; this feed's pre-existing shared visibility across all clinicians is unaffected by in-product role permissions.

**Sources:** DEC-046, BR-01, BR-08, ASM-006, BR-09, ASM-007

- [ ] Given an appointment is created, rescheduled, or cancelled, the shared calendar entry reflects the change (pass) / it is not updated (fail).
- [ ] The calendar write payload contains only patient name, time, duration, room, clinician, and appointment type (pass) / it contains intake, code, or billing data (fail).
- [ ] No product action reads or imports a booking from the shared calendar (pass) / one is imported (fail).

### REQ-034
All front-desk and clinical staff screens used at the point of care (check-in, tablet intake, no-show marking) operate correctly on small touch-screen tablets.

**Sources:** DEC-045

- [ ] Given the check-in and intake screens render on a small tablet touch-screen viewport, all controls are reachable and operable by touch with no horizontal scrolling (pass) / a control is unreachable or requires horizontal scroll (fail).

## Authority

In any conflict the Master controls: `elm-street-clinic-front-desk-r2-PRD.md` is the authoritative document, and its approved-scope citations decide disputes. This checklist is a projection of that document.