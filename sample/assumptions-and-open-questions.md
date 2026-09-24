# Assumptions
- Any active clinician can be scheduled for any appointment type; the practice manager is not required to restrict specific types to specific clinicians in v1.
- The no-show grace period and the patient self-service cut-off are single clinic-wide values, not configured separately per appointment type, in v1.
- The clinic operates from a single site; multi-location scheduling is not required.
- The monthly report is viewed on demand inside the product by the practice manager; it is not emailed automatically.
- The practice manager does not book, reschedule, or check in patients directly; those actions are performed by receptionists, consistent with the manager's stated scope of configuration and reporting.
- Only scheduling-relevant fields — patient name, appointment time, duration, room, clinician, and appointment type — are written to the external shared calendar feed; intake form contents, visit summary codes, and billing information are never included in that feed.
- The clinician permission restriction limiting visibility to a clinician's own patients applies only within the product's own interface; the external shared calendar kept per the client's Q-01 decision retains its pre-existing shared, clinic-wide visibility across all clinicians and is not restricted by in-product role permissions.
- When a clinician-absence cancellation triggers a rebooking, the product automatically copies the patient's already-submitted intake form onto the new appointment rather than requiring resubmission; the original form instance remains attached to the cancelled appointment as an unchanged historical record, and the patient may edit the copy before the new visit.
- The three-no-shows-in-six-months flag is evaluated dynamically against a rolling six-month window from the current date; the flag lifts automatically once fewer than three no-shows remain within the trailing six months, with no manual unflag action required from staff.

# Questions
- The intake says the existing shared calendar 'will be replaced,' but also requires the product to show appointments inside 'the clinicians' shared calendar' so clinicians keep one view. Should the old shared calendar be fully retired, or should it continue to exist as a read-only display target the product feeds into?
  - Answer: Keep the existing shared calendar as the source clinicians already trust, and have the product write into it while never reading bookings from it.
- Where do visit summary codes come from when a clinician completes a visit: a fixed list the practice manager maintains, or free text the clinician types?
  - Answer: Practice manager maintains a fixed list of visit summary codes; clinicians select from that list when completing a visit.