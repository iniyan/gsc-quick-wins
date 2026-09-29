#!/usr/bin/env python3
"""
find_quick_wins.py — rank Google Search Console rows sitting in positions 4–20.

Works with the standard GSC Performance export (Queries.csv or Pages.csv from the
"Export → Download CSV" zip) and with API / Looker Studio style exports that carry
both query and page columns. Standard library only — no pip install needed.

Usage:
    python3 find_quick_wins.py Queries.csv
    python3 find_quick_wins.py Queries.csv --top 25 --min-impressions 200
    python3 find_quick_wins.py export.csv --format csv > wins.csv
    python3 find_quick_wins.py export.csv --format json
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

# Expected CTR by position (midpoint of the benchmark ranges in SKILL.md)
EXPECTED_CTR = [
    (1, 0.315), (2, 0.175), (3, 0.115), (5, 0.075),
    (10, 0.035), (20, 0.015),
]

ALIASES = {
    "query": ["top queries", "query", "queries", "search query", "keyword"],
    "page": ["top pages", "page", "pages", "url", "landing page", "address"],
    "clicks": ["clicks", "url clicks"],
    "impressions": ["impressions"],
    "ctr": ["ctr", "url ctr", "site ctr"],
    "position": ["position", "average position", "avg. position", "avg position"],
}


def expected_ctr(pos: float) -> float:
    pos = round(pos)  # GSC averages: 5.3 behaves like position 5
    for ceiling, ctr in EXPECTED_CTR:
        if pos <= ceiling:
            return ctr
    return 0.01


def to_float(value: str) -> float:
    v = (value or "").strip().replace(",", "")
    if not v:
        return 0.0
    if v.endswith("%"):
        return float(v[:-1]) / 100
    return float(v)


def map_columns(header: list[str]) -> dict[str, int]:
    norm = [h.strip().lower().lstrip("\ufeff") for h in header]
    found: dict[str, int] = {}
    for key, names in ALIASES.items():
        for i, h in enumerate(norm):
            if h in names:
                found[key] = i
                break
    missing = {"impressions", "position"} - found.keys()
    if missing:
        sys.exit(f"Could not find column(s): {', '.join(sorted(missing))}. Header was: {header}")
    if "query" not in found and "page" not in found:
        sys.exit("Need a query column (Top queries) or a page column (Top pages).")
    return found


def diagnose(pos: float, ctr: float, exp: float) -> tuple[str, str]:
    weak_ctr = ctr < exp * 0.6
    if pos <= 7 and weak_ctr:
        return "Low CTR for position", "Rewrite title + meta description"
    if pos <= 7:
        return "Close to top 3", "Add dedicated H2 + FAQ, internal links"
    if pos <= 12:
        issue = "Content gap" + (" + low CTR" if weak_ctr else "")
        return issue, "Add dedicated section answering the query" + (", fix title" if weak_ctr else "")
    return "Thin topical depth", "Expand content + add internal links"


def tier(pos: float, impressions: float, min_impr: float) -> str:
    if impressions < min_impr * 2:
        return "Later"
    if pos <= 12:
        return "Do first"
    return "Do second"


def analyse(path: Path, lo: float, hi: float, min_impr: float) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.reader(fh)
        header = next(reader)
        cols = map_columns(header)
        rows = []
        for raw in reader:
            if not raw or all(not c.strip() for c in raw):
                continue
            try:
                pos = to_float(raw[cols["position"]])
                impr = to_float(raw[cols["impressions"]])
            except (ValueError, IndexError):
                continue
            if not (lo <= pos <= hi) or impr < min_impr:
                continue
            clicks = to_float(raw[cols["clicks"]]) if "clicks" in cols else 0.0
            if "ctr" in cols and raw[cols["ctr"]].strip():
                ctr = to_float(raw[cols["ctr"]])
                if ctr > 1:  # some exports give 3.2 meaning 3.2%
                    ctr /= 100
            else:
                ctr = clicks / impr if impr else 0.0
            exp = expected_ctr(pos)
            # Clicks you would gain if this row reached position 3 at benchmark CTR
            upside = max(impr * expected_ctr(3) - clicks, 0)
            # Easier to move rows closer to the top: weight by proximity
            proximity = (hi + 1 - pos) / (hi + 1 - lo)
            score = upside * (0.5 + proximity)
            issue, action = diagnose(pos, ctr, exp)
            rows.append({
                "query": raw[cols["query"]].strip() if "query" in cols else "",
                "page": raw[cols["page"]].strip() if "page" in cols else "",
                "position": round(pos, 1),
                "impressions": int(impr),
                "clicks": int(clicks),
                "ctr": round(ctr * 100, 2),
                "expected_ctr": round(exp * 100, 1),
                "click_upside": int(upside),
                "score": round(score, 1),
                "tier": tier(pos, impr, min_impr),
                "issue": issue,
                "action": action,
            })
    rows.sort(key=lambda r: r["score"], reverse=True)
    return rows


def print_markdown(rows: list[dict]) -> None:
    has_q = any(r["query"] for r in rows)
    has_p = any(r["page"] for r in rows)
    head = (["Keyword"] if has_q else []) + (["Page"] if has_p else []) + [
        "Pos", "Impr.", "CTR", "Exp. CTR", "+Clicks @#3", "Tier", "Issue", "Action"]
    print("| " + " | ".join(head) + " |")
    print("|" + "---|" * len(head))
    for r in rows:
        cells = ([r["query"]] if has_q else []) + ([r["page"]] if has_p else []) + [
            str(r["position"]), f'{r["impressions"]:,}', f'{r["ctr"]}%',
            f'{r["expected_ctr"]}%', f'{r["click_upside"]:,}', r["tier"],
            r["issue"], r["action"]]
        print("| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |")


def main() -> None:
    ap = argparse.ArgumentParser(description="Find GSC quick wins (positions 4–20).")
    ap.add_argument("csv", type=Path, help="GSC export CSV (Queries.csv, Pages.csv, or query+page)")
    ap.add_argument("--top", type=int, default=15, help="rows to show (default 15)")
    ap.add_argument("--min-impressions", type=float, default=100,
                    help="ignore rows below this many impressions (default 100)")
    ap.add_argument("--min-pos", type=float, default=4)
    ap.add_argument("--max-pos", type=float, default=20)
    ap.add_argument("--format", choices=["md", "csv", "json"], default="md")
    args = ap.parse_args()

    if not args.csv.exists():
        sys.exit(f"File not found: {args.csv}")

    rows = analyse(args.csv, args.min_pos, args.max_pos, args.min_impressions)
    if not rows:
        sys.exit("No rows in the position window with enough impressions. "
                 "Try --min-impressions 20 or a longer date range in GSC.")
    rows = rows[: args.top]

    if args.format == "json":
        json.dump(rows, sys.stdout, indent=2, ensure_ascii=False)
        print()
    elif args.format == "csv":
        w = csv.DictWriter(sys.stdout, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    else:
        print_markdown(rows)


if __name__ == "__main__":
    main()
