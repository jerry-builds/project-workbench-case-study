# Developer Handoff — Clinic Front-Desk Operations Platform — Master PRD

Revision 2 · Derived convenience view computed from the frozen approved brief and the Master PRD. This file is regenerated on every export and is never edited directly.

## Purpose

This product replaces a six-role clinic's phone booking, paper intake, handwritten reminders, and notebook no-show log with one system spanning patient self-service, front-desk operations, clinical hand-off, billing hand-off, and practice-manager configuration and reporting. Patients book, reschedule, cancel, and complete intake themselves; receptionists run the day's schedule, check-in, no-shows, and clinician-absence rebooking; nurses triage readiness; clinicians close the clinical loop with a fixed-list visit summary code; the billing clerk tracks the hand-off to billing; the practice manager configures the clinic and reviews reporting and audit history. Per the client's Q-01 answer, the clinic's existing shared calendar stays in place and receives a one-way scheduling-data feed from the product. Per the client's Q-02 answer, visit summary codes come from a fixed list the practice manager maintains, not free text. All prior self-audit resolutions (BR-01 through BR-12) are carried forward as binding scope.

## Who uses it

- **Patient** — Patient Portal: Let a patient manage their own appointments, intake form, and reminder responses.
- **Receptionist** — Receptionist Front Desk: Manage the day's schedule, patient accounts, check-in, no-shows, and clinician-absence rebooking.
- **Patient (in-clinic, staff-assisted tablet)** — Front-Desk Tablet Check-In: Let a patient complete the intake form at the front desk when it was not done ahead of the visit.
- **Nurse** — Nurse Day List: Track today's checked-in patients and mark them ready for the clinician.
- **Clinician** — Clinician Schedule: View the clinician's own daily schedule with readiness and late status, and complete visits.
- **Billing Clerk** — Billing Clerk Console: Review completed visits and their summary codes, and track which have been sent to billing.
- **Practice Manager** — Practice Manager Admin: Configure clinic settings, manage staff accounts, mark clinician absences, and review reports and audit history.

## MVP scope

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

## Major workflows

### Patient Self-Booking
Initiating role: Patient · Trigger: Patient wants to schedule an appointment and opens the patient portal.
1. Patient selects an appointment type.
2. System shows available clinician/room/time slots for that type.
3. Patient selects a slot and confirms the booking.
4. System reserves the clinician and room for that slot immediately.
5. System sends a booking confirmation message and writes the appointment to the shared calendar.
Completion: Appointment created, slot unavailable to other patients, confirmation sent, calendar updated.
Failure/rejection: No matching slot is available, or the patient is no-show-flagged; the booking is rejected with the reason shown to the patient.

### Reminder Confirm or Cancel
Initiating role: Patient · Trigger: An automated reminder is due to be sent before an upcoming appointment.
1. System sends a text and email reminder at the configured interval before the appointment.
2. The message includes a unique confirm link and a unique cancel link.
3. Patient taps confirm or cancel.
4. System applies the response to the appointment immediately.
5. If cancelled, the slot becomes available and a cancellation confirmation is sent.
Completion: Appointment status updated (confirmed or cancelled) and the response recorded as applied.
Failure/rejection: The reminder fails to send through the messaging service; the failure is recorded as not-sent.

### Check-In Through Visit Completion
Initiating role: Receptionist, Nurse, and Clinician · Trigger: Patient arrives at the clinic for a scheduled appointment.
1. Receptionist checks the patient in on arrival.
2. If no intake form was submitted ahead of time, the patient completes it on the front-desk tablet.
3. The checked-in patient appears on the nurse's day list.
4. Nurse reads the intake form and marks the patient ready.
5. Clinician sees the readiness status on their schedule and begins the visit.
6. Clinician marks the visit complete and selects a visit summary code.
7. System automatically sends the summary code and date to the billing system.
8. Billing clerk reviews the completed visit and marks it sent to billing.
Completion: Visit marked complete, summary code transmitted to billing, billing clerk marks it sent.
Failure/rejection: Patient arrives for a clinician-absence-cancelled appointment and is redirected to rebooking instead of check-in.

### No-Show Marking and Flag Recalculation
Initiating role: Receptionist · Trigger: The grace period elapses after an appointment's start time with no patient arrival.
1. Receptionist observes the appointment has passed the grace period with no check-in.
2. Receptionist marks the appointment as a no-show.
3. System records the no-show and recalculates the patient's rolling six-month no-show count.
4. If the count reaches three, the system flags the patient for receptionist-only booking.
Completion: No-show recorded; flag state reflects the current rolling six-month count.
Failure/rejection: The grace period has not elapsed yet, so the no-show action is unavailable.

### Clinician Absence Handling
Initiating role: Practice Manager and Receptionist · Trigger: Practice manager marks a clinician absent for a date range.
1. Practice manager marks a clinician absent for a date range.
2. System blocks new bookings for that clinician's future slots in the range.
3. System cancels existing appointments that fall within the range.
4. Receptionist reviews the list of affected appointments.
5. Receptionist books a new appointment in an available slot for each affected patient.
6. System copies each patient's already-submitted intake form onto the new appointment, leaving the original attached unchanged to the cancelled appointment.
7. System sends each patient a cancellation confirmation and a new booking confirmation.
Completion: All affected appointments rebooked into new slots, with intake forms carried forward where applicable.
Failure/rejection: A patient arrives at the clinic for the cancelled appointment before rebooking is complete; front desk redirects them to rebooking.

### Staff and Patient Account Provisioning
Initiating role: Practice Manager and Receptionist · Trigger: A new staff member joins the clinic, or a new patient needs product access.
1. Practice manager creates a staff account and assigns a role.
2. Receptionist looks up a new patient in the clinic's existing patient records system.
3. If a match is found, receptionist sends an account invitation for the patient to set a password.
4. If no match is found, account creation is blocked until the patient exists in the records system.
Completion: Staff account active with an assigned role, or patient invitation sent and pending password setup.
Failure/rejection: No matching patient record exists in the records system; account creation does not proceed.

### Clinic Configuration
Initiating role: Practice Manager · Trigger: Practice manager needs to set up or adjust clinic operating parameters.
1. Practice manager sets clinic hours, rooms, appointment types, and durations.
2. Practice manager maintains the fixed list of visit summary codes.
3. Practice manager sets reminder timing, the no-show grace period, and the patient self-service cutoff.
4. Practice manager attempts to remove a room, appointment type, or clinician.
5. System blocks removal if future appointments exist for that entity; practice manager moves or cancels those appointments before removal succeeds.
Completion: Configuration values saved and applied to booking, completion, and reminder logic clinic-wide.
Failure/rejection: Removal is blocked because future appointments exist for the entity.

### Monthly Reporting and Audit Review
Initiating role: Practice Manager · Trigger: Practice manager wants to review clinic performance or investigate a staff action.
1. Practice manager selects a month and views the report of visits, cancellations, no-shows, and average check-in-to-ready wait per clinician.
2. Practice manager reviews the audit log for a specific appointment or intake form to see which staff member acted and when.
Completion: Report and audit data displayed on demand inside the product.

## Application surfaces

### Patient Portal
Role: Patient — Let a patient manage their own appointments, intake form, and reminder responses.

Major actions:
- View own upcoming and past appointments
- Book a new appointment by type
- Reschedule or cancel own appointment before the cutoff
- Complete the intake form for an upcoming appointment
- Confirm or cancel an appointment from a reminder link
- Edit a carried-forward intake form after a clinician-absence rebooking

### Receptionist Front Desk
Role: Receptionist — Manage the day's schedule, patient accounts, check-in, no-shows, and clinician-absence rebooking.

Major actions:
- Look up a patient in the records system and send an account invitation
- Book, reschedule, or cancel an appointment for any patient
- Check in an arriving patient
- Mark a patient as a no-show after the grace period
- Rebook patients affected by a clinician absence
- Redirect a walk-in whose appointment was cancelled for clinician absence to rebooking

### Front-Desk Tablet Check-In
Role: Patient (in-clinic, staff-assisted tablet) — Let a patient complete the intake form at the front desk when it was not done ahead of the visit.

Major actions:
- Complete intake form on the front-desk tablet during check-in

### Nurse Day List
Role: Nurse — Track today's checked-in patients and mark them ready for the clinician.

Major actions:
- View today's checked-in patients only
- Read a checked-in patient's intake form
- Mark a patient ready for the clinician
- See late-arrival flag for checked-in patients

### Clinician Schedule
Role: Clinician — View the clinician's own daily schedule with readiness and late status, and complete visits.

Major actions:
- View own schedule with patient readiness and late-arrival indicators
- Open own patients' intake forms
- Mark a visit complete and select a visit summary code from the fixed list

### Billing Clerk Console
Role: Billing Clerk — Review completed visits and their summary codes, and track which have been sent to billing.

Major actions:
- View completed visits with summary codes and dates only
- Mark a completed visit as sent to billing

### Practice Manager Admin
Role: Practice Manager — Configure clinic settings, manage staff accounts, mark clinician absences, and review reports and audit history.

Major actions:
- Set clinic hours, rooms, appointment types, and durations
- Maintain the fixed list of visit summary codes
- Set reminder timing, no-show grace period, and patient cutoff
- Create a staff account and assign a role
- Deactivate a staff account
- Mark a clinician absent for a date range
- View the monthly per-clinician report
- View the audit log
- Attempt to remove a room, appointment type, or clinician (blocked while future appointments exist)

## Core data entities

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

## Technical constraints

- Staff use the system on tablets at the desk, so it must work well on a small touch screen. — you specified this
- the clinic's existing patient records system holds each patient's identity and contact details; this product must look up and display a patient's name and contact details from it and must never change anything there — you specified this
- our messaging service for text and email; reminders and confirmations must be sent through it, and the product should record whether each message was sent — you specified this
- the clinic's billing system; when a visit is complete, the product must pass the visit summary code and date to it, and must not read anything back except a confirmation that it was received — you specified this
- the clinicians' shared calendar; the product must show clinic appointments in it so clinicians keep one view, and it must never take bookings from that calendar — you specified this
- Reminder confirm/cancel actions are implemented via a unique tokenized link per message, not by parsing free-text replies. — we proposed this; you left this choice to whoever builds the product

Origin says who asked for a constraint, not whether it works. This service reviews the specification and does not assess feasibility or compatibility, so nothing above has been validated against any environment.

## Milestone summary

M1: Accounts & Access — practice manager creates staff accounts with roles; receptionists look up patients in the records system and invite them; role-scoped permissions are enforced everywhere.
M2: Core Scheduling & Configuration — practice manager configures hours, rooms, types, durations, and summary codes; patients and receptionists book, reschedule, and cancel with room/clinician double-booking prevented.
M3: Reminders & Confirmations — automated reminders send with confirm/cancel links; patients receive confirmations for booking, move, and cancellation events.
M4: Intake & Check-In — intake completes ahead of time or on the front-desk tablet; receptionists check patients in; nurses triage readiness; clinicians see readiness on their schedule.
M5: Visit Completion & Billing — clinicians complete visits with a selected summary code; the code and date transmit automatically to billing; the billing clerk reviews and marks visits sent.
M6: No-Show & Absence Handling — grace-period no-shows and the rolling three-no-show flag apply automatically; clinician-absence cancellation and rebooking with intake carry-forward work end to end; late arrivals check in with a flag.
M7: Reporting & Audit — practice manager views the monthly per-clinician report and full audit log; staff deactivation preserves history; completed visits and intake forms are permanently retained.
M8: Calendar Integration & Tablet Optimization — appointment data writes one-way into the existing shared calendar; all front-desk and tablet screens operate on small touch-screen viewports.

## Acceptance expectations

34 requirements across 8 milestones carry 79 pass/fail acceptance criteria. The full verbatim checklist ships as `ACCEPTANCE.md`.

## Non-goals

- Online payment processing — deferred to a later version (DEC-030).
- A patient portal for viewing test results — deferred to a later version (DEC-031).
- Telephone-call reminders — deferred to a later version (DEC-032).
- Waiting-list management — deferred to a later version (DEC-033).
- Clinical note-taking of any kind — deferred to a later version (DEC-034).
- Staff-directory integration for automatic account provisioning — excluded from v1; staff accounts remain manually created by the practice manager.

## Unresolved product decisions

None. The approved brief was frozen before Master generation; every discovery outcome is recorded in `DECISIONS.md`.

This section covers **product** decisions only — what the product should do. It says nothing about implementation assessments, which remain the implementer's: any technical constraint listed above is recorded as the client stated it and has not been validated by this service, so its feasibility in your environment is still an open question to settle before building against it.

## Authority

In any conflict the Master controls: `elm-street-clinic-front-desk-r2-PRD.md` is the authoritative document, and its approved-scope citations decide disputes. This handoff and `ACCEPTANCE.md` are projections of that document.