#!/usr/bin/env python3
"""Convert a PROJECT_WORKBENCH Master PRD into an Azure Boards CSV import file.

One Epic for the product, one Feature per milestone, one User Story per
requirement. Standard library only. The output depends only on the input
file, so running it twice gives the same bytes.

Usage:
    python3 tools/ado-export/prd_to_ado.py \
        sample/elm-street-clinic-front-desk-r2-PRD.md \
        sample/ado/elm-street-backlog.csv
"""

import csv
import html
import io
import re
import sys
from pathlib import Path

TITLE_LIMIT = 120
COLUMNS = [
    "Work Item Type",
    "Title 1",
    "Title 2",
    "Title 3",
    "Description",
    "Acceptance Criteria",
    "Tags",
]


def section(text, heading):
    """Return the body of a '## heading' section, up to the next '## '."""
    match = re.search(
        rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", text, re.M | re.S
    )
    if not match:
        sys.exit(f"PRD has no '## {heading}' section")
    return match.group(1)


def product_name(text):
    """The product name is the H1 without its ' ... Master PRD' suffix."""
    h1 = re.search(r"^# (.+)$", text, re.M).group(1)
    return re.split(r"\s+\u2014\s+Master PRD$", h1)[0].strip()


def parse_requirements(text):
    body = section(text, "Requirements")
    parts = re.split(r"^### (REQ-\d{3})\n", body, flags=re.M)[1:]
    reqs = []
    for req_id, block in zip(parts[0::2], parts[1::2]):
        statement = block.strip().split("\n\n", 1)[0].strip()
        sources = re.search(r"^\*\*Approved sources:\*\* (.+)$", block, re.M)
        milestone = re.search(r"^\*\*Milestone:\*\* (.+)$", block, re.M)
        criteria = re.findall(r"^- \[ \] (.+)$", block, re.M)
        if not (sources and milestone and criteria):
            sys.exit(f"{req_id}: missing sources, milestone or criteria")
        reqs.append(
            {
                "id": req_id,
                "statement": statement,
                "sources": [s.strip() for s in sources.group(1).split(",")],
                "milestone": milestone.group(1).strip(),
                "criteria": criteria,
            }
        )
    return reqs


def roadmap(text):
    """(milestone name, summary) pairs in the order the PRD's Roadmap lists them."""
    body = section(text, "Roadmap")
    entries = []
    for line in re.findall(r"^- (.+)$", body, re.M):
        parts = re.split(r"\s+\u2014\s+", line, maxsplit=1)
        summary = parts[1].strip() if len(parts) == 2 else ""
        entries.append((parts[0].strip(), summary))
    return entries


def short_title(req):
    """REQ id plus the statement up to its first semicolon.

    Longer than TITLE_LIMIT characters, it is cut at a word boundary and
    ends in "...".

    The PRD gives requirements no titles, so the title is taken from the
    requirement's own words and never paraphrased.
    """
    clause = req["statement"].split(";", 1)[0].rstrip(".")
    if len(clause) > TITLE_LIMIT:
        clause = clause[:TITLE_LIMIT].rsplit(" ", 1)[0].rstrip(",") + "..."
    return f"{req['id']} {clause}"


def description_html(req):
    sources = ", ".join(req["sources"])
    return (
        f"<p>{html.escape(req['statement'], quote=False)}</p>"
        f"<p>Approved sources: {html.escape(sources, quote=False)}</p>"
    )


def criteria_html(req):
    items = "".join(f"<li>{html.escape(c, quote=False)}</li>" for c in req["criteria"])
    return f"<ul>{items}</ul>"


def build_rows(text):
    reqs = parse_requirements(text)
    order = roadmap(text)
    used = {r["milestone"] for r in reqs}
    unknown = used - {name for name, _ in order}
    if unknown:
        sys.exit(f"milestones missing from Roadmap: {sorted(unknown)}")

    rows = [["Epic", product_name(text), "", "", "", "", ""]]
    for milestone, summary in order:
        stories = [r for r in reqs if r["milestone"] == milestone]
        if not stories:
            continue
        feature_description = f"<p>{html.escape(summary, quote=False)}</p>" if summary else ""
        rows.append(["Feature", "", milestone, "", feature_description, "", ""])
        for req in stories:
            rows.append(
                [
                    "User Story",
                    "",
                    "",
                    short_title(req),
                    description_html(req),
                    criteria_html(req),
                    "; ".join([req["id"], *req["sources"]]),
                ]
            )
    return rows


def main(argv):
    if len(argv) != 3:
        sys.exit(__doc__)
    src, dest = Path(argv[1]), Path(argv[2])
    rows = build_rows(src.read_text(encoding="utf-8"))
    out = io.StringIO()
    writer = csv.writer(out, quoting=csv.QUOTE_ALL, lineterminator="\r\n")
    writer.writerow(COLUMNS)
    writer.writerows(rows)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(out.getvalue().encode("utf-8"))
    counts = {}
    for row in rows:
        counts[row[0]] = counts.get(row[0], 0) + 1
    summary = ", ".join(f"{k}: {v}" for k, v in counts.items())
    print(f"wrote {dest} ({summary})")


if __name__ == "__main__":
    main(sys.argv)
