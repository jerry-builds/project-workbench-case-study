# Elm Street Clinic Front Desk

Status: Final client delivery

## Contents
- elm-street-clinic-front-desk-r2-PRD.md
- PRODUCT-SPEC.md
- AGENTS.md
- CLAUDE.md
- lovable-project-knowledge.txt
- replit.md
- DEVELOPER-HANDOFF.md
- ACCEPTANCE.md
- DECISIONS.md
- diagrams/scope-map.svg
- diagrams/scope-map.png
- diagrams/role-matrix.svg
- diagrams/role-matrix.png
- diagrams/traceability.svg
- diagrams/traceability.png
- diagrams/traceability-map.html
- diagrams/flow-01-patient-self-booking.svg
- diagrams/flow-01-patient-self-booking.png
- diagrams/flow-02-reminder-confirm-or-cancel.svg
- diagrams/flow-02-reminder-confirm-or-cancel.png
- diagrams/flow-03-check-in-through-visit-completion.svg
- diagrams/flow-03-check-in-through-visit-completion.png
- diagrams/flow-04-no-show-marking-and-flag-recalculation.svg
- diagrams/flow-04-no-show-marking-and-flag-recalculation.png
- diagrams/flow-05-clinician-absence-handling.svg
- diagrams/flow-05-clinician-absence-handling.png
- diagrams/flow-06-staff-and-patient-account-provisioning.svg
- diagrams/flow-06-staff-and-patient-account-provisioning.png
- diagrams/flow-07-clinic-configuration.svg
- diagrams/flow-07-clinic-configuration.png
- assumptions-and-open-questions.md
- revision-changelog.md
- delivery-message.txt
- manifest.json

Use the PRD as the source of truth and place companion instruction files at the project root or in the named platform knowledge field. Companion files are derivatives: if any file conflicts with the certified Master, the Master controls. PRODUCT-SPEC.md is a stable alias of the certified Master (elm-street-clinic-front-desk-r2-PRD.md), so AI agents can reference one unchanging filename across revisions. DEVELOPER-HANDOFF.md, ACCEPTANCE.md, and DECISIONS.md are derived views computed from the frozen Master: if you need them changed, request a revision rather than editing them, and we reissue the package. The diagrams/ folder holds the Visual Pack: diagrams drawn from this revision's specification, each as SVG (opens in any browser or vector editor) and as PNG (for chat, documents and slides). They are derived views like the derived files above. traceability-map.html is an interactive version of the traceability diagram; open it in any browser, no connection needed.

## Start here

1. Read PRODUCT-SPEC.md — it is the product specification and it governs.
2. Read DEVELOPER-HANDOFF.md for scope, what depends on you, and what is still open.
3. Put the companion files where your tool reads them: AGENTS.md, CLAUDE.md, lovable-project-knowledge.txt, replit.md at the root of your project, or pasted into your tool's project-knowledge field if it has one.
4. Give your tool this first instruction:

> Read PRODUCT-SPEC.md and AGENTS.md and CLAUDE.md and lovable-project-knowledge.txt and replit.md. Do not write any code yet. Tell me what you would need to inspect in this environment before starting, and list anything in the specification you cannot act on without a decision from me.

**No repository yet?** That is expected — this package is a specification, not a codebase. Step 4 still works in an empty folder: put these files in it and open your tool there. The companion asks your tool to inspect what exists, and "nothing exists yet" is a valid answer that shapes what it proposes.