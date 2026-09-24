# Clinic Front-Desk Operations Platform — Master PRD

## Overview
This product replaces a six-role clinic's phone booking, paper intake, handwritten reminders, and notebook no-show log with one system spanning patient self-service, front-desk operations, clinical hand-off, billing hand-off, and practice-manager configuration and reporting. Patients book, reschedule, cancel, and complete intake themselves; receptionists run the day's schedule, check-in, no-shows, and clinician-absence rebooking; nurses triage readiness; clinicians close the clinical loop with a fixed-list visit summary code; the billing clerk tracks the hand-off to billing; the practice manager configures the clinic and reviews reporting and audit history. Per the client's Q-01 answer, the clinic's existing shared calendar stays in place and receives a one-way scheduling-data feed from the product. Per the client's Q-02 answer, visit summary codes come from a fixed list the practice manager maintains, not free text. All prior self-audit resolutions (BR-01 through BR-12) are carried forward as binding scope.

## Goals
- Replace phone booking, paper intake, handwritten reminders, and the notebook no-show log with one auditable system.
- Prevent room and clinician double-booking under all circumstances.
- Automate reminders with a one-tap confirm/cancel path applied immediately.
- Give each of the six roles only the screens and data their role requires.
- Capture a valid visit summary code at visit completion and hand it to billing automatically, with a separate clerk-tracked status.
- Give the practice manager configuration control, a per-clinician monthly report, and a full action audit trail.
- Preserve the client's existing patient records system, messaging service, billing system, and shared calendar as read-only or one-way integration boundaries exactly as decided.

## Requirements
### REQ-001
Patients can book an appointment by selecting an appointment type; the system assigns an available clinician and room, and the slot becomes unavailable to other patients immediately on booking.

**Approved sources:** DEC-001

**Acceptance criteria**
- [ ] Given an appointment type with an available clinician+room+time combination, when a patient submits a booking, the system creates the appointment and that slot is no longer offered to other patients (pass) / the slot remains bookable by another patient (fail).
- [ ] Given no slot matches the requested type, the patient cannot submit a booking for it (pass) / a conflicting booking is created (fail).

**Milestone:** M2: Core Scheduling & Configuration

### REQ-002
Patients can reschedule or cancel only their own appointment, and only before a practice-manager-configured cutoff time.

**Approved sources:** DEC-002, DEC-036

**Acceptance criteria**
- [ ] Given the current time is before the cutoff, a patient can reschedule or cancel their own appointment (pass) / the action is blocked (fail).
- [ ] Given the current time is at or after the cutoff, reschedule/cancel controls are unavailable to the patient (pass) / the change still succeeds (fail).
- [ ] A patient cannot reschedule or cancel another patient's appointment (pass) / another patient's appointment is editable (fail).
- [ ] Given the practice manager edits the cutoff time, the new value applies to future reschedule/cancel eligibility checks (pass) / the previous cutoff value continues to apply (fail).

**Milestone:** M2: Core Scheduling & Configuration

### REQ-003
Receptionists can book, reschedule, and cancel an appointment on behalf of any patient, at any time, with no cutoff restriction.

**Approved sources:** DEC-003

**Acceptance criteria**
- [ ] Given any time relative to an appointment, a receptionist can reschedule or cancel it (pass) / the cutoff blocks the receptionist (fail).
- [ ] A receptionist can create a new booking for any looked-up patient (pass) / booking on behalf of a patient is unavailable (fail).

**Milestone:** M2: Core Scheduling & Configuration

### REQ-004
The system sends an automated text and email reminder before each appointment, at an interval the practice manager configures, through the clinic's existing messaging service, and records whether each reminder was sent.

**Approved sources:** DEC-004, DEC-043

**Acceptance criteria**
- [ ] Given the configured interval, both a text and an email reminder are sent that far ahead of each appointment (pass) / no reminder is sent (fail).
- [ ] Every reminder send attempt is recorded with a sent or not-sent status (pass) / no record exists (fail).
- [ ] Given the practice manager edits the reminder interval, reminders for future appointments use the new interval (pass) / the previous interval still applies (fail).

**Milestone:** M3: Reminders & Confirmations

### REQ-005
Each reminder includes a unique confirm link and a unique cancel link; tapping either applies the patient's response to that appointment immediately.

**Approved sources:** DEC-005, BR-03

**Acceptance criteria**
- [ ] Given a patient taps the confirm link, the appointment status updates to confirmed immediately (pass) / it remains unconfirmed (fail).
- [ ] Given a patient taps the cancel link, the appointment is cancelled immediately and the slot becomes available (pass) / the appointment stays booked (fail).
- [ ] A link cannot be used to affect a different patient's appointment (pass) / it does (fail).

**Milestone:** M3: Reminders & Confirmations

### REQ-006
Patients receive a confirmation message through the messaging service whenever their appointment is booked, moved, or cancelled, whether the action was taken by the patient or by staff.

**Approved sources:** DEC-025, DEC-043

**Acceptance criteria**
- [ ] Given a receptionist reschedules a patient's appointment, the patient receives a confirmation reflecting the new time (pass) / no message is sent (fail).
- [ ] Given any booking, reschedule, or cancellation event, a message send attempt is recorded (pass) / no record exists (fail).

**Milestone:** M3: Reminders & Confirmations

### REQ-007
A patient completes an intake form before the visit, and each submitted form instance attaches to one specific appointment; a submitted form can never be deleted.

**Approved sources:** DEC-006, DEC-029, DEC-039

**Acceptance criteria**
- [ ] Given a patient submits an intake form for an appointment, the form is retrievable from that appointment record (pass) / it is unlinked (fail).
- [ ] A submitted intake form cannot be deleted by any user through the product (pass) / a delete action succeeds (fail).

**Milestone:** M4: Intake & Check-In

### REQ-008
If the intake form was not completed ahead of the visit, the patient completes it on a tablet at the front desk during check-in, and the completed form attaches to that same appointment.

**Approved sources:** DEC-007, DEC-045

**Acceptance criteria**
- [ ] Given an appointment with no submitted intake form at arrival, the check-in flow presents the intake form on the front-desk tablet (pass) / check-in proceeds without collecting it (fail).
- [ ] The tablet intake screen fits a small touch-screen viewport with no horizontal scrolling of fields (pass) / fields overflow the viewport (fail).

**Milestone:** M4: Intake & Check-In

### REQ-009
A receptionist checks a patient in on arrival, and the checked-in patient appears on the nurse's list for that day.

**Approved sources:** DEC-008

**Acceptance criteria**
- [ ] Given a receptionist marks a patient checked-in, the patient appears on the nurse's day list without manual refresh action (pass) / the patient does not appear (fail).
- [ ] The nurse's list shows only today's checked-in patients (pass) / it shows other days' patients (fail).

**Milestone:** M4: Intake & Check-In

### REQ-010
A nurse can read a checked-in patient's intake form and mark that patient ready for the clinician; a nurse cannot book, reschedule, or cancel appointments.

**Approved sources:** DEC-009, DEC-028

**Acceptance criteria**
- [ ] Given a nurse opens a checked-in patient's record, the submitted intake form content is viewable (pass) / it is hidden (fail).
- [ ] Given a nurse marks a patient ready, that status appears on the assigned clinician's schedule (pass) / it does not propagate (fail).
- [ ] No booking, reschedule, or cancel control is available to the nurse role (pass) / one is available (fail).

**Milestone:** M4: Intake & Check-In

### REQ-011
A clinician sees patient readiness status directly on their own daily schedule, and sees only their own appointments.

**Approved sources:** DEC-010, DEC-028

**Acceptance criteria**
- [ ] Given a nurse marks a patient ready, the ready indicator appears on that clinician's schedule for that appointment (pass) / it does not appear (fail).
- [ ] A clinician's schedule shows only appointments assigned to that clinician (pass) / it shows another clinician's appointments (fail).

**Milestone:** M4: Intake & Check-In

### REQ-012
A clinician marks a visit complete and, at that time, must select a visit summary code from the practice-manager-maintained fixed list; free-text entry is not offered.

**Approved sources:** DEC-011, DEC-047, BR-06

**Acceptance criteria**
- [ ] Given a clinician completes a visit, completion requires selecting one code from the configured list first (pass) / completion succeeds with no code (fail).
- [ ] The code selection control has no free-text entry field (pass) / a free-text field is present (fail).

**Milestone:** M5: Visit Completion & Billing

### REQ-013
The moment a clinician marks a visit complete, the system automatically sends only the visit summary code and visit date to the clinic's billing system and reads back only a receipt confirmation, with no intake content included.

**Approved sources:** DEC-044, DEC-040, BR-10

**Acceptance criteria**
- [ ] Given a visit is marked complete, a transmission with only the code and date is sent to billing without manual clerk action (pass) / no transmission occurs until a clerk acts (fail).
- [ ] Only a receipt confirmation is stored from the billing system's response (pass) / additional billing-system data is stored (fail).
- [ ] No intake form content appears in the transmission (pass) / it does (fail).

**Milestone:** M5: Visit Completion & Billing

### REQ-014
The billing clerk sees completed visits with their summary codes and dates only, never intake form contents, and can manually mark each visit as sent to billing as a status separate from the automatic transmission.

**Approved sources:** DEC-012, DEC-028, DEC-037, BR-10

**Acceptance criteria**
- [ ] A completed visit's entry for the billing clerk shows only date and summary code, no intake content (pass) / intake content is visible (fail).
- [ ] Given the billing clerk marks a visit as sent to billing, that status is stored distinct from the automatic transmission status and does not alter or repeat it (pass) / it interferes with the automatic transmission (fail).

**Milestone:** M5: Visit Completion & Billing

### REQ-015
A receptionist can mark a patient as a no-show only after a practice-manager-configured grace period has elapsed past the appointment start time with no arrival recorded.

**Approved sources:** DEC-013

**Acceptance criteria**
- [ ] Given the grace period has not elapsed, the no-show action is unavailable (pass) / it is available (fail).
- [ ] Given the grace period has elapsed with no check-in, a receptionist can mark the appointment as a no-show (pass) / the action is blocked (fail).
- [ ] Given the practice manager edits the grace period, future no-show eligibility checks use the new value (pass) / the previous grace period still applies (fail).

**Milestone:** M6: No-Show & Absence Handling

### REQ-016
The system automatically flags a patient on the third no-show within a rolling six-month window and automatically lifts the flag once fewer than three no-shows remain in that trailing window; while flagged, only a receptionist can create a new booking for that patient.

**Approved sources:** DEC-014, ASM-009, BR-12

**Acceptance criteria**
- [ ] Given a patient's third no-show falls within the trailing six months, the flag is set without staff action (pass) / it requires a manual step (fail).
- [ ] Given re-evaluation finds fewer than three no-shows in the trailing six months, the flag is removed automatically (pass) / it stays set (fail).
- [ ] While flagged, a patient-initiated booking attempt is rejected and a receptionist-initiated booking still succeeds (pass) / the patient can self-book while flagged (fail).

**Milestone:** M6: No-Show & Absence Handling

### REQ-017
The practice manager configures clinic hours, rooms, appointment types, appointment durations, and the fixed list of visit summary codes; only the practice manager role can edit these.

**Approved sources:** DEC-015, DEC-047

**Acceptance criteria**
- [ ] Given a practice manager adds, edits, or removes a room, type, duration, or summary code, the change is reflected immediately in booking and completion screens (pass) / stale values persist (fail).
- [ ] No other role has access to these configuration controls (pass) / another role can edit them (fail).
- [ ] Given a practice manager edits clinic hours, the new hours apply to future booking availability (pass) / the previous hours still apply (fail).

**Milestone:** M2: Core Scheduling & Configuration

### REQ-018
The system never permits two appointments to hold the same room at overlapping times, and every schedule view shows each appointment's assigned room.

**Approved sources:** DEC-016, DEC-035

**Acceptance criteria**
- [ ] Given a room is booked for a time range, a second booking for that room in an overlapping range is rejected (pass) / it succeeds (fail).
- [ ] Every appointment entry in schedule views shows its assigned room (pass) / the room is missing (fail).

**Milestone:** M2: Core Scheduling & Configuration

### REQ-019
The system never permits a clinician to hold two appointments with overlapping times.

**Approved sources:** DEC-017, DEC-035

**Acceptance criteria**
- [ ] Given a clinician is booked for a time range, a second booking for that clinician in an overlapping range is rejected (pass) / it succeeds (fail).

**Milestone:** M2: Core Scheduling & Configuration

### REQ-020
The practice manager can view an on-demand monthly report showing visits, cancellations, no-shows, and average wait between check-in and ready, broken down per clinician; the report is not emailed automatically.

**Approved sources:** DEC-018, ASM-004

**Acceptance criteria**
- [ ] Given a selected month, the report displays all four metrics broken out per clinician (pass) / a metric or breakdown is missing (fail).
- [ ] The report is viewed on demand inside the product (pass) / an automatic email is sent instead or as well (fail).

**Milestone:** M7: Reporting & Audit

### REQ-021
Every staff action on an appointment or intake form is logged with the acting user's identity and a timestamp, and log entries cannot be edited or deleted through the product.

**Approved sources:** DEC-019

**Acceptance criteria**
- [ ] Given a staff member books, reschedules, cancels, checks in, marks ready, completes a visit, or marks no-show, a log entry records the user identity and timestamp (pass) / no entry is created (fail).
- [ ] No interface control allows editing or deleting a log entry (pass) / one exists (fail).

**Milestone:** M7: Reporting & Audit

### REQ-022
The practice manager can deactivate a staff account; deactivation blocks login but preserves that user's logged history of past actions.

**Approved sources:** DEC-020

**Acceptance criteria**
- [ ] Given a practice manager deactivates a staff account, that account can no longer log in (pass) / login still succeeds (fail).
- [ ] All prior logged actions by that user remain visible in audit records after deactivation (pass) / they disappear (fail).

**Milestone:** M7: Reporting & Audit

### REQ-023
The system blocks removal or deactivation of a room, appointment type, or clinician that has future appointments, until those appointments are moved or cancelled.

**Approved sources:** DEC-021

**Acceptance criteria**
- [ ] Given a room, type, or clinician has a future appointment, a removal/deactivation attempt is rejected and the future appointments are identified (pass) / removal succeeds anyway (fail).
- [ ] Given all future appointments for that entity are moved or cancelled, the removal/deactivation attempt then succeeds (pass) / it remains blocked (fail).

**Milestone:** M2: Core Scheduling & Configuration

### REQ-024
When a clinician is marked absent for a date range, the system blocks new bookings for that clinician's future slots in the range, cancels existing affected appointments, presents the receptionist with the affected list to rebook, and copies each affected patient's already-submitted intake form onto the newly created appointment while leaving the original form unchanged on the cancelled appointment.

**Approved sources:** DEC-022, BR-02, BR-11, ASM-008

**Acceptance criteria**
- [ ] Given a clinician is marked absent for a date range, no new booking can be created for that clinician in that range (pass) / one succeeds (fail).
- [ ] Given existing appointments fall in that range, each is cancelled and listed for the receptionist to rebook (pass) / an affected appointment is left unresolved or unlisted (fail).
- [ ] Given an affected appointment had a submitted intake form, the new appointment carries an editable copy of it while the original stays unchanged on the cancelled appointment (pass) / the new appointment has no form or the original is altered (fail).

**Milestone:** M6: No-Show & Absence Handling

### REQ-025
A patient who arrives for an appointment cancelled due to clinician absence is told the appointment is no longer active and is offered the next available slots to rebook, instead of being checked in.

**Approved sources:** DEC-023

**Acceptance criteria**
- [ ] Given a patient arrives for a cancelled-due-to-absence appointment, the check-in screen shows an inactive-appointment message with next-available-slot options instead of a check-in confirmation (pass) / the patient is checked in normally (fail).

**Milestone:** M6: No-Show & Absence Handling

### REQ-026
A patient who arrives after the no-show grace period, but before being marked no-show, can still be checked in, with the appointment flagged as late for the nurse and clinician.

**Approved sources:** DEC-024

**Acceptance criteria**
- [ ] Given a patient arrives after the grace period but before a no-show mark, a receptionist can check the patient in (pass) / check-in is blocked (fail).
- [ ] Given that check-in, a late flag is visible on both the nurse's list and the clinician's schedule for that appointment (pass) / the flag is missing from either view (fail).

**Milestone:** M6: No-Show & Absence Handling

### REQ-027
A receptionist creates a patient account only by looking the patient up in the clinic's existing patient records system and sending a password-setup invitation; patients cannot self-register; if no match is found, no account is created.

**Approved sources:** DEC-026, BR-05

**Acceptance criteria**
- [ ] Given a receptionist finds a matching patient in the records system, a password-setup invitation is sent to that patient (pass) / none is sent (fail).
- [ ] No self-registration entry point exists in the product (pass) / one exists (fail).
- [ ] Given a records-system search returns no match, the account-creation action is unavailable and no local account is created (pass) / one is created anyway (fail).

**Milestone:** M1: Accounts & Access

### REQ-028
The system reads patient name and contact details from the clinic's existing patient records system for display only, and never writes to that system.

**Approved sources:** DEC-042, DEC-041

**Acceptance criteria**
- [ ] Given a patient record is displayed, the name and contact details match the records-system source (pass) / they diverge without an update (fail).
- [ ] No product action results in a write, update, or delete call to the patient records system (pass) / one occurs (fail).

**Milestone:** M1: Accounts & Access

### REQ-029
Staff accounts, across all five staff roles, are created only by the practice manager; no other role or automated source creates them.

**Approved sources:** DEC-027

**Acceptance criteria**
- [ ] Given a practice manager creates a staff account with an assigned role, that account can log in with that role's permissions (pass) / a non-practice-manager role can create a staff account (fail).

**Milestone:** M1: Accounts & Access

### REQ-030
The system enforces role-scoped access: patients see only their own appointments and forms; receptionists see the full day schedule but not clinical notes or billing codes; nurses see only today's checked-in patients and cannot book; clinicians see only their own schedule and their own patients' intake forms; the billing clerk sees only completed visits and summary codes, never intake content; the practice manager sees all schedules and reports but records no clinical information.

**Approved sources:** DEC-028, DEC-036, DEC-037, DEC-038

**Acceptance criteria**
- [ ] Given a patient attempts to view another patient's appointment or form, access is denied (pass) / granted (fail).
- [ ] Given a receptionist attempts to view intake form contents or change a billing code, the action is denied (pass) / it succeeds (fail).
- [ ] Given a clinician attempts to view another clinician's intake forms, access is denied (pass) / granted (fail).
- [ ] Given the billing clerk attempts to view intake form contents, access is denied (pass) / granted (fail).
- [ ] No control for recording clinical information is available to the practice manager role (pass) / one exists (fail).

**Milestone:** M1: Accounts & Access

### REQ-031
No role, including the practice manager, can delete a completed visit record or a submitted intake form.

**Approved sources:** DEC-029, DEC-039

**Acceptance criteria**
- [ ] Given any role attempts to delete a completed visit, no delete control is available and the attempt fails (pass) / deletion succeeds (fail).
- [ ] Given any role attempts to delete a submitted intake form, no delete control is available and the attempt fails (pass) / deletion succeeds (fail).

**Milestone:** M7: Reporting & Audit

### REQ-032
Intake form contents are never included in any message sent through the messaging service or any data sent to the billing system.

**Approved sources:** DEC-040

**Acceptance criteria**
- [ ] Given a reminder or confirmation message is generated, its content contains only scheduling information, never intake fields (pass) / intake data appears (fail).
- [ ] Given a billing transmission is generated on visit completion, its payload contains only the summary code and date, never intake fields (pass) / intake data appears (fail).

**Milestone:** M5: Visit Completion & Billing

### REQ-033
The system writes appointment scheduling data (patient name, time, duration, room, clinician, appointment type) into the clinic's existing shared calendar one-way on create, reschedule, and cancel, never reads bookings back from it, and excludes intake content, summary codes, and billing information from the feed; this feed's pre-existing shared visibility across all clinicians is unaffected by in-product role permissions.

**Approved sources:** DEC-046, BR-01, BR-08, ASM-006, BR-09, ASM-007

**Acceptance criteria**
- [ ] Given an appointment is created, rescheduled, or cancelled, the shared calendar entry reflects the change (pass) / it is not updated (fail).
- [ ] The calendar write payload contains only patient name, time, duration, room, clinician, and appointment type (pass) / it contains intake, code, or billing data (fail).
- [ ] No product action reads or imports a booking from the shared calendar (pass) / one is imported (fail).

**Milestone:** M8: Calendar Integration & Tablet Optimization

### REQ-034
All front-desk and clinical staff screens used at the point of care (check-in, tablet intake, no-show marking) operate correctly on small touch-screen tablets.

**Approved sources:** DEC-045

**Acceptance criteria**
- [ ] Given the check-in and intake screens render on a small tablet touch-screen viewport, all controls are reachable and operable by touch with no horizontal scrolling (pass) / a control is unreachable or requires horizontal scroll (fail).

**Milestone:** M8: Calendar Integration & Tablet Optimization

## Application Surfaces
### Patient Portal
**Intended user/role:** Patient

**Primary purpose:** Let a patient manage their own appointments, intake form, and reminder responses.

**Major actions**
- View own upcoming and past appointments
- Book a new appointment by type
- Reschedule or cancel own appointment before the cutoff
- Complete the intake form for an upcoming appointment
- Confirm or cancel an appointment from a reminder link
- Edit a carried-forward intake form after a clinician-absence rebooking

**Related requirements:** REQ-001, REQ-002, REQ-005, REQ-006, REQ-007, REQ-016, REQ-024

### Receptionist Front Desk
**Intended user/role:** Receptionist

**Primary purpose:** Manage the day's schedule, patient accounts, check-in, no-shows, and clinician-absence rebooking.

**Major actions**
- Look up a patient in the records system and send an account invitation
- Book, reschedule, or cancel an appointment for any patient
- Check in an arriving patient
- Mark a patient as a no-show after the grace period
- Rebook patients affected by a clinician absence
- Redirect a walk-in whose appointment was cancelled for clinician absence to rebooking

**Related requirements:** REQ-003, REQ-009, REQ-015, REQ-016, REQ-024, REQ-025, REQ-026, REQ-027

### Front-Desk Tablet Check-In
**Intended user/role:** Patient (in-clinic, staff-assisted tablet)

**Primary purpose:** Let a patient complete the intake form at the front desk when it was not done ahead of the visit.

**Major actions**
- Complete intake form on the front-desk tablet during check-in

**Related requirements:** REQ-008, REQ-034

### Nurse Day List
**Intended user/role:** Nurse

**Primary purpose:** Track today's checked-in patients and mark them ready for the clinician.

**Major actions**
- View today's checked-in patients only
- Read a checked-in patient's intake form
- Mark a patient ready for the clinician
- See late-arrival flag for checked-in patients

**Related requirements:** REQ-009, REQ-010, REQ-026

### Clinician Schedule
**Intended user/role:** Clinician

**Primary purpose:** View the clinician's own daily schedule with readiness and late status, and complete visits.

**Major actions**
- View own schedule with patient readiness and late-arrival indicators
- Open own patients' intake forms
- Mark a visit complete and select a visit summary code from the fixed list

**Related requirements:** REQ-011, REQ-012, REQ-026, REQ-030

### Billing Clerk Console
**Intended user/role:** Billing Clerk

**Primary purpose:** Review completed visits and their summary codes, and track which have been sent to billing.

**Major actions**
- View completed visits with summary codes and dates only
- Mark a completed visit as sent to billing

**Related requirements:** REQ-014, REQ-030

### Practice Manager Admin
**Intended user/role:** Practice Manager

**Primary purpose:** Configure clinic settings, manage staff accounts, mark clinician absences, and review reports and audit history.

**Major actions**
- Set clinic hours, rooms, appointment types, and durations
- Maintain the fixed list of visit summary codes
- Set reminder timing, no-show grace period, and patient cutoff
- Create a staff account and assign a role
- Deactivate a staff account
- Mark a clinician absent for a date range
- View the monthly per-clinician report
- View the audit log
- Attempt to remove a room, appointment type, or clinician (blocked while future appointments exist)

**Related requirements:** REQ-002, REQ-004, REQ-015, REQ-017, REQ-020, REQ-021, REQ-022, REQ-023, REQ-024, REQ-029

## User Flows
### Flow: Patient Self-Booking
**Initiating role:** Patient

**Trigger:** Patient wants to schedule an appointment and opens the patient portal.

**Steps**
1. Patient selects an appointment type.
2. System shows available clinician/room/time slots for that type.
3. Patient selects a slot and confirms the booking.
4. System reserves the clinician and room for that slot immediately.
5. System sends a booking confirmation message and writes the appointment to the shared calendar.

**Decision points**
- If the patient is flagged for three no-shows in six months, self-booking is blocked and the patient must contact a receptionist.
- If no slot matches the requested type, the booking cannot proceed.

**Completion:** Appointment created, slot unavailable to other patients, confirmation sent, calendar updated.
**Failure/rejection:** No matching slot is available, or the patient is no-show-flagged; the booking is rejected with the reason shown to the patient.
**Related requirements:** REQ-001, REQ-006, REQ-016, REQ-033

### Flow: Reminder Confirm or Cancel
**Initiating role:** Patient

**Trigger:** An automated reminder is due to be sent before an upcoming appointment.

**Steps**
1. System sends a text and email reminder at the configured interval before the appointment.
2. The message includes a unique confirm link and a unique cancel link.
3. Patient taps confirm or cancel.
4. System applies the response to the appointment immediately.
5. If cancelled, the slot becomes available and a cancellation confirmation is sent.

**Decision points**
- Patient taps confirm versus cancel.

**Completion:** Appointment status updated (confirmed or cancelled) and the response recorded as applied.
**Failure/rejection:** The reminder fails to send through the messaging service; the failure is recorded as not-sent.
**Related requirements:** REQ-004, REQ-005, REQ-006

### Flow: Check-In Through Visit Completion
**Initiating role:** Receptionist, Nurse, and Clinician

**Trigger:** Patient arrives at the clinic for a scheduled appointment.

**Steps**
1. Receptionist checks the patient in on arrival.
2. If no intake form was submitted ahead of time, the patient completes it on the front-desk tablet.
3. The checked-in patient appears on the nurse's day list.
4. Nurse reads the intake form and marks the patient ready.
5. Clinician sees the readiness status on their schedule and begins the visit.
6. Clinician marks the visit complete and selects a visit summary code.
7. System automatically sends the summary code and date to the billing system.
8. Billing clerk reviews the completed visit and marks it sent to billing.

**Decision points**
- If the patient arrives after the no-show grace period but has not yet been marked no-show, check-in proceeds with a late flag.
- If the patient arrives for an appointment already cancelled due to clinician absence, check-in is refused and rebooking slots are offered instead.

**Completion:** Visit marked complete, summary code transmitted to billing, billing clerk marks it sent.
**Failure/rejection:** Patient arrives for a clinician-absence-cancelled appointment and is redirected to rebooking instead of check-in.
**Related requirements:** REQ-008, REQ-009, REQ-010, REQ-011, REQ-012, REQ-013, REQ-014, REQ-025, REQ-026

### Flow: No-Show Marking and Flag Recalculation
**Initiating role:** Receptionist

**Trigger:** The grace period elapses after an appointment's start time with no patient arrival.

**Steps**
1. Receptionist observes the appointment has passed the grace period with no check-in.
2. Receptionist marks the appointment as a no-show.
3. System records the no-show and recalculates the patient's rolling six-month no-show count.
4. If the count reaches three, the system flags the patient for receptionist-only booking.

**Decision points**
- If the patient's rolling six-month no-show count is at or above three, the flag stays set; otherwise it lifts automatically.

**Completion:** No-show recorded; flag state reflects the current rolling six-month count.
**Failure/rejection:** The grace period has not elapsed yet, so the no-show action is unavailable.
**Related requirements:** REQ-015, REQ-016

### Flow: Clinician Absence Handling
**Initiating role:** Practice Manager and Receptionist

**Trigger:** Practice manager marks a clinician absent for a date range.

**Steps**
1. Practice manager marks a clinician absent for a date range.
2. System blocks new bookings for that clinician's future slots in the range.
3. System cancels existing appointments that fall within the range.
4. Receptionist reviews the list of affected appointments.
5. Receptionist books a new appointment in an available slot for each affected patient.
6. System copies each patient's already-submitted intake form onto the new appointment, leaving the original attached unchanged to the cancelled appointment.
7. System sends each patient a cancellation confirmation and a new booking confirmation.

**Decision points**
- If the affected appointment had no submitted intake form, no form is copied.

**Completion:** All affected appointments rebooked into new slots, with intake forms carried forward where applicable.
**Failure/rejection:** A patient arrives at the clinic for the cancelled appointment before rebooking is complete; front desk redirects them to rebooking.
**Related requirements:** REQ-024, REQ-025, REQ-006, REQ-033

### Flow: Staff and Patient Account Provisioning
**Initiating role:** Practice Manager and Receptionist

**Trigger:** A new staff member joins the clinic, or a new patient needs product access.

**Steps**
1. Practice manager creates a staff account and assigns a role.
2. Receptionist looks up a new patient in the clinic's existing patient records system.
3. If a match is found, receptionist sends an account invitation for the patient to set a password.
4. If no match is found, account creation is blocked until the patient exists in the records system.

**Decision points**
- Match found in the records system versus no match found.

**Completion:** Staff account active with an assigned role, or patient invitation sent and pending password setup.
**Failure/rejection:** No matching patient record exists in the records system; account creation does not proceed.
**Related requirements:** REQ-027, REQ-028, REQ-029

### Flow: Clinic Configuration
**Initiating role:** Practice Manager

**Trigger:** Practice manager needs to set up or adjust clinic operating parameters.

**Steps**
1. Practice manager sets clinic hours, rooms, appointment types, and durations.
2. Practice manager maintains the fixed list of visit summary codes.
3. Practice manager sets reminder timing, the no-show grace period, and the patient self-service cutoff.
4. Practice manager attempts to remove a room, appointment type, or clinician.
5. System blocks removal if future appointments exist for that entity; practice manager moves or cancels those appointments before removal succeeds.

**Decision points**
- Entity has future appointments versus none.

**Completion:** Configuration values saved and applied to booking, completion, and reminder logic clinic-wide.
**Failure/rejection:** Removal is blocked because future appointments exist for the entity.
**Related requirements:** REQ-017, REQ-018, REQ-019, REQ-023

### Flow: Monthly Reporting and Audit Review
**Initiating role:** Practice Manager

**Trigger:** Practice manager wants to review clinic performance or investigate a staff action.

**Steps**
1. Practice manager selects a month and views the report of visits, cancellations, no-shows, and average check-in-to-ready wait per clinician.
2. Practice manager reviews the audit log for a specific appointment or intake form to see which staff member acted and when.

**Completion:** Report and audit data displayed on demand inside the product.
**Related requirements:** REQ-020, REQ-021, REQ-022

## Scope
- Patient self-service booking, reschedule, and cancel with a practice-manager-configured cutoff.
- Unrestricted receptionist booking, reschedule, and cancel on behalf of any patient.
- Automated text/email reminders with one-tap confirm/cancel links applied immediately.
- Booking/move/cancel confirmation messages to patients.
- Intake form completion ahead of visit or on a front-desk tablet at check-in, attached to a specific appointment.
- Receptionist check-in, nurse readiness triage, and clinician readiness visibility.
- Clinician visit completion with a fixed-list visit summary code.
- Automatic billing-system transmission of code and date on visit completion, plus a separate billing-clerk 'sent to billing' tracking status.
- Grace-period-based no-show marking and a rolling six-month three-no-show flag restricting self-booking.
- Practice-manager configuration of hours, rooms, appointment types, durations, and summary codes.
- Room and clinician double-booking prevention.
- Monthly per-clinician report and full staff-action audit logging.
- Staff account deactivation preserving history; protected removal of in-use rooms/types/clinicians.
- Clinician-absence cancellation and receptionist-led rebooking with intake form carry-forward.
- Late-arrival check-in with a visible late flag.
- Receptionist-only, records-system-matched patient account creation; practice-manager-only staff account creation.
- Role-scoped permissions across all six roles.
- One-way appointment data feed into the clinic's existing shared calendar.
- Tablet-usable front-desk and clinical screens.

## Non-Goals
- Online payment processing — deferred to a later version (DEC-030).
- A patient portal for viewing test results — deferred to a later version (DEC-031).
- Telephone-call reminders — deferred to a later version (DEC-032).
- Waiting-list management — deferred to a later version (DEC-033).
- Clinical note-taking of any kind — deferred to a later version (DEC-034).
- Staff-directory integration for automatic account provisioning — excluded from v1; staff accounts remain manually created by the practice manager.

## Data Model
- Patient: identity matched to the clinic's patient records system; holds read-only display name and contact details, a no-show history, and a current flag status derived from that history.
- Staff Account: one of five roles (Receptionist, Nurse, Clinician, Billing Clerk, Practice Manager); has an active/deactivated state; identity is preserved in audit logs after deactivation.
- Appointment: belongs to one Patient, one Clinician, one Room, and one Appointment Type; has a scheduled time and duration; moves through states including booked, confirmed, checked-in, ready, late, completed, cancelled, and no-show; relates to zero or one Intake Form and, once completed, one Visit Summary Code.
- Intake Form: exactly one submitted instance per appointment; readable only by the assigned clinician and by nurses for checked-in patients; when a clinician-absence rebooking occurs, a copy attaches to the new appointment while the original remains unchanged on the cancelled appointment.
- Room: distinguished by name; cannot be held by two overlapping appointments; cannot be removed while it has future appointments.
- Appointment Type: distinguished by name and default duration; cannot be removed while it has future appointments.
- Clinician: a Staff Account with a schedule; cannot hold two overlapping appointments; can be marked absent for a date range; cannot be deactivated while it has future appointments.
- Visit Summary Code: an item in the practice-manager-maintained fixed list; selected exactly once per completed visit, never free text.
- No-Show Record: linked to one Patient and one Appointment; counted within a rolling six-month window to determine the patient's flag status.
- Reminder/Confirmation Message: linked to one Appointment; records channel (text/email), sent status, and any patient response (confirm/cancel) applied.
- Audit Log Entry: linked to one Staff Account, one action, one target (Appointment or Intake Form), and a timestamp; never editable or deletable.
- Billing Transmission Record: linked to one completed visit; holds the code and date automatically sent plus the receipt confirmation; distinct from the billing clerk's manual 'sent to billing' status on that same visit.
- Shared Calendar Entry: a one-way projection of an Appointment's scheduling fields (patient name, time, duration, room, clinician, type) into the external calendar; not editable or readable back into the product.

## Roadmap
- M1: Accounts & Access — practice manager creates staff accounts with roles; receptionists look up patients in the records system and invite them; role-scoped permissions are enforced everywhere.
- M2: Core Scheduling & Configuration — practice manager configures hours, rooms, types, durations, and summary codes; patients and receptionists book, reschedule, and cancel with room/clinician double-booking prevented.
- M3: Reminders & Confirmations — automated reminders send with confirm/cancel links; patients receive confirmations for booking, move, and cancellation events.
- M4: Intake & Check-In — intake completes ahead of time or on the front-desk tablet; receptionists check patients in; nurses triage readiness; clinicians see readiness on their schedule.
- M5: Visit Completion & Billing — clinicians complete visits with a selected summary code; the code and date transmit automatically to billing; the billing clerk reviews and marks visits sent.
- M6: No-Show & Absence Handling — grace-period no-shows and the rolling three-no-show flag apply automatically; clinician-absence cancellation and rebooking with intake carry-forward work end to end; late arrivals check in with a flag.
- M7: Reporting & Audit — practice manager views the monthly per-clinician report and full audit log; staff deactivation preserves history; completed visits and intake forms are permanently retained.
- M8: Calendar Integration & Tablet Optimization — appointment data writes one-way into the existing shared calendar; all front-desk and tablet screens operate on small touch-screen viewports.

## Assumptions
- Any active clinician can be scheduled for any appointment type; the practice manager is not required to restrict specific types to specific clinicians in v1.
- The no-show grace period and the patient self-service cutoff are single clinic-wide values, not configured separately per appointment type, in v1.
- The clinic operates from a single site; multi-location scheduling is not required.
- The monthly report is viewed on demand inside the product by the practice manager; it is not emailed automatically.
- The practice manager does not book, reschedule, or check in patients directly; those actions are performed by receptionists.
- Only scheduling-relevant fields — patient name, appointment time, duration, room, clinician, and appointment type — are written to the external shared calendar feed; intake content, visit summary codes, and billing information are never included.
- The in-product clinician-visibility restriction applies only to the product's own interface; the external shared calendar kept per the client's Q-01 decision retains its pre-existing shared, clinic-wide visibility and is not restricted by in-product role permissions.
- When a clinician-absence rebooking occurs, the product automatically copies the patient's already-submitted intake form onto the new appointment; the original form stays attached unchanged to the cancelled appointment, and the patient may edit the copy before the new visit.
- The three-no-shows-in-six-months flag is evaluated dynamically against a rolling six-month window; it lifts automatically once fewer than three no-shows remain in that window, with no manual unflag action required.

## Traceability
- REQ-001 → M2: Core Scheduling & Configuration → DEC-001
- REQ-002 → M2: Core Scheduling & Configuration → DEC-002, DEC-036
- REQ-003 → M2: Core Scheduling & Configuration → DEC-003
- REQ-004 → M3: Reminders & Confirmations → DEC-004, DEC-043
- REQ-005 → M3: Reminders & Confirmations → DEC-005, BR-03
- REQ-006 → M3: Reminders & Confirmations → DEC-025, DEC-043
- REQ-007 → M4: Intake & Check-In → DEC-006, DEC-029, DEC-039
- REQ-008 → M4: Intake & Check-In → DEC-007, DEC-045
- REQ-009 → M4: Intake & Check-In → DEC-008
- REQ-010 → M4: Intake & Check-In → DEC-009, DEC-028
- REQ-011 → M4: Intake & Check-In → DEC-010, DEC-028
- REQ-012 → M5: Visit Completion & Billing → DEC-011, DEC-047, BR-06
- REQ-013 → M5: Visit Completion & Billing → DEC-044, DEC-040, BR-10
- REQ-014 → M5: Visit Completion & Billing → DEC-012, DEC-028, DEC-037, BR-10
- REQ-015 → M6: No-Show & Absence Handling → DEC-013
- REQ-016 → M6: No-Show & Absence Handling → DEC-014, ASM-009, BR-12
- REQ-017 → M2: Core Scheduling & Configuration → DEC-015, DEC-047
- REQ-018 → M2: Core Scheduling & Configuration → DEC-016, DEC-035
- REQ-019 → M2: Core Scheduling & Configuration → DEC-017, DEC-035
- REQ-020 → M7: Reporting & Audit → DEC-018, ASM-004
- REQ-021 → M7: Reporting & Audit → DEC-019
- REQ-022 → M7: Reporting & Audit → DEC-020
- REQ-023 → M2: Core Scheduling & Configuration → DEC-021
- REQ-024 → M6: No-Show & Absence Handling → DEC-022, BR-02, BR-11, ASM-008
- REQ-025 → M6: No-Show & Absence Handling → DEC-023
- REQ-026 → M6: No-Show & Absence Handling → DEC-024
- REQ-027 → M1: Accounts & Access → DEC-026, BR-05
- REQ-028 → M1: Accounts & Access → DEC-042, DEC-041
- REQ-029 → M1: Accounts & Access → DEC-027
- REQ-030 → M1: Accounts & Access → DEC-028, DEC-036, DEC-037, DEC-038
- REQ-031 → M7: Reporting & Audit → DEC-029, DEC-039
- REQ-032 → M5: Visit Completion & Billing → DEC-040
- REQ-033 → M8: Calendar Integration & Tablet Optimization → DEC-046, BR-01, BR-08, ASM-006, BR-09, ASM-007
- REQ-034 → M8: Calendar Integration & Tablet Optimization → DEC-045