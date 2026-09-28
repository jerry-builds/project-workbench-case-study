# ado-export

Turns a PROJECT_WORKBENCH Master PRD into a CSV file that Azure Boards can import.

```
python3 tools/ado-export/prd_to_ado.py \
    sample/elm-street-clinic-front-desk-r2-PRD.md \
    sample/ado/elm-street-backlog.csv
```

Python 3 standard library only. The output depends only on the PRD, so running it again gives the same bytes.

## What maps to what

| PRD | Azure Boards |
| --- | --- |
| Product name (the H1) | one Epic (`Title 1`) |
| Each milestone, in Roadmap order | one Feature (`Title 2`) |
| Each requirement (`REQ-###`) | one User Story (`Title 3`) under its milestone |
| Requirement statement and its approved sources | Description (HTML `<p>`) |
| The requirement's acceptance criteria | Acceptance Criteria (HTML `<ul>`) |
| REQ id and approved sources (`DEC-`, `ASM-`, `BR-`) | Tags, separated by `; ` |

The PRD gives requirements no titles. A story title is the REQ id plus the requirement's own words up to the first semicolon. Past 120 characters it is cut at a word boundary and ends in "...". Nothing is paraphrased.

## Importing

Use a project on the Agile process, so User Story has an Acceptance Criteria field. In the project, open **Boards > Queries > Import work items**, choose the CSV, check the preview, then **Save items**. Items import in the New state. The file has no ID column because every row is a new item. Microsoft's reference: https://learn.microsoft.com/en-us/azure/devops/boards/queries/import-work-items-from-csv

The script checks what it reads. It stops if a requirement has no sources, milestone or criteria, or cites a milestone the Roadmap does not list.
