---
name: gsc-quick-wins
description: >
  Squeeze more traffic from pages Google already ranks you for — without writing a single new article.
  Use this skill whenever the user wants to improve existing rankings using Google Search Console data,
  find keywords sitting in positions 4–20, boost pages from page 2 to page 1, improve CTR on ranked pages,
  or optimise already-indexed content for quick SEO gains. Trigger on phrases like "quick SEO wins",
  "improve existing rankings", "GSC position 4-20", "low-hanging SEO", "move keyword up", "boost my rankings",
  "pages already ranking", "why is my page stuck at position 8", "CTR is low on GSC", "optimise ranked pages",
  or any time the user shares a GSC export (queries, pages, impressions, CTR, position) and wants to grow traffic.
  Also trigger when the user says "I don't want to write new content" but still wants SEO growth — this skill
  is exactly for that. Always prefer this over generic SEO advice when GSC data is available or the user
  is focused on existing pages.
---

# GSC Quick Wins

You are an expert SEO strategist. Your job is to help the user extract maximum traffic from pages Google
already believes deserve to rank — by targeting keywords in positions 4–20 and systematically improving
the confidence Google has in those pages.

> **Core insight**: Moving a keyword from position #8 → #3 is often worth more traffic than publishing
> 10 new articles. The easiest SEO wins are hiding between positions 4 and 20.

---

## Step 1: Understand What the User Has

Before starting, figure out what data the user is working with. Ask if you don't know:

- Do they have a **GSC export** (CSV or pasted data)? → Go to Step 2
- Are they describing a **specific page or keyword** they want to improve? → Go to Step 3
- Do they just want to **learn the process**? → Walk them through the full workflow below

---

## Step 2: Analyse the GSC Data

If the user provides GSC data (CSV, table, or pasted rows), extract and filter:

> **Fast path (when you can run code):** this skill ships a zero-dependency helper that does the
> filtering, CTR-gap check and scoring below in one pass. Run it on the user's CSV and use its table
> as the starting point for Steps 3–5:
>
> ```bash
> python3 scripts/find_quick_wins.py path/to/Queries.csv --top 15
> ```
>
> It accepts the standard GSC Performance export (`Queries.csv` / `Pages.csv`) or any export with
> query + page columns. Flags: `--min-impressions`, `--min-pos`, `--max-pos`, `--format md|csv|json`.
> If you can't run code, apply the same rules manually.

**No export yet?** Tell the user: Search Console → Performance → Search results → set date range to
the last 3 months → Export → Download CSV. Use `Queries.csv` (and `Pages.csv` to map queries to URLs).

### Filter Criteria
| Criterion | Rule |
|---|---|
| Position | Keep only rows where **position is between 4 and 20** |
| Impressions | Sort descending — highest impressions = highest opportunity |
| Ignore | Positions 1–3 (already ranking well) |
| Ignore | Positions 21+ (too far to move quickly) |
| Priority | Keywords with **high impressions + weak CTR** are the biggest wins |

### Opportunity Scoring (mental model)
Score each keyword by combining:
- **Impressions** (how many people search this)
- **Position gap** (how far from top 3)
- **CTR gap** (how low is CTR vs expected for that position)

Expected CTR benchmarks by position:
- Position 1: ~28–35%
- Position 2: ~15–20%
- Position 3: ~10–13%
- Position 4–5: ~6–9%
- Position 6–10: ~2–5%
- Position 11–20: ~1–2%

If a page at position 5 has 0.8% CTR, the title tag is broken — flag it.

### Output: Priority Keyword Table
Present the top 10–15 opportunities in this format:

| Keyword | Page | Position | Impressions | CTR | Issue | Action |
|---|---|---|---|---|---|---|
| keyword here | /page-slug | 7 | 4,200 | 1.2% | Low CTR + content gap | Rewrite H2, update title |

---

## Step 3: Diagnose Each Priority Page

For each priority keyword, diagnose the likely reason it's stuck. Check against these patterns:

### 🔍 Content Gaps
- Does the page have a **dedicated section** that directly answers the query?
- Is the keyword (or close variant) in an **H2 or H3 heading**?
- Does the page cover **adjacent questions** users likely have?
- Are there **entities, examples, stats, FAQs** that build topical authority?

### 📉 CTR Problems
- Is the **title tag compelling** for the keyword?
- Does the **meta description** include a benefit or hook?
- Is there **schema markup** that could unlock rich results (FAQ, HowTo, Article)?

### 🔗 Authority Problems
- How many **internal links** point to this page?
- Are the anchor texts relevant to the target keyword?
- Are there related pages that should link here but don't?

---

## Step 4: Generate an Action Plan

For each priority page, produce a **specific, actionable improvement plan**:

### Content Actions
- [ ] Add a dedicated H2 section titled: _[exact or near-exact keyword]_
- [ ] Answer these adjacent questions in new subsections: _[list 3–5 PAA-style questions]_
- [ ] Add supporting entities: _[brand names, locations, statistics, tools relevant to the topic]_
- [ ] Add an FAQ section with questions: _[list 3–5 questions]_
- [ ] Include 1–2 statistics or data points with citations
- [ ] Expand thin sections (under 100 words) to be more comprehensive

### Title & Meta Actions
- [ ] Current title: _[show current]_
- [ ] Suggested title: _[write a better version — include keyword near the front, add a hook]_
- [ ] Suggested meta description: _[write one — 150–160 chars, include keyword + benefit]_

### Internal Link Actions
- [ ] Pages that should link here: _[list 2–4 related pages on their site if known]_
- [ ] Suggested anchor text: _[exact keyword or variant]_

### Schema Actions
- [ ] Add FAQ schema if the page has Q&A sections
- [ ] Add HowTo schema if the page explains a process
- [ ] Add Article schema with dateModified if it's a blog post

### Post-Update Actions
- [ ] Re-submit URL in GSC: Search Console → URL Inspection → Request Indexing
- [ ] Note the date of update — check rankings again in 2–4 weeks

---

## Step 5: Prioritise the Work

Help the user decide where to start. Use this prioritisation framework:

**Do first (highest ROI):**
- Position 4–7 + high impressions + low CTR → title/meta fix is probably enough
- Position 8–12 + high impressions + content gap → add a dedicated section

**Do second:**
- Position 13–20 + high impressions → content expansion + internal links

**Do last (or skip for now):**
- Low impressions at any position → not enough search volume to move the needle

---

## Tone & Output Style

- Be **specific**, not generic. Don't say "improve your content" — say "Add an H2 titled 'How to X' and answer Y and Z below it."
- Show the user **exactly what to write or change**, not just what category of thing to fix.
- If you can draft the improved title tag, H2, or FAQ — **do it**. Don't just describe it.
- Keep the action plan **scannable** — use tables and checklists so the user can execute directly.

---

## Quick Reference: The Full Process

```
GSC → Search Results
  ↓ Filter: Position 4–20
  ↓ Sort: Impressions (highest first)
  ↓ Ignore: positions 1–3 and 21+

For each priority keyword:
  → Open the ranking page
  → Add a dedicated section answering the exact query
  → Include keyword in a heading (when natural)
  → Expand topical depth (adjacent questions, entities, stats, FAQs)
  → Improve internal links pointing to that page
  → Update title tag if CTR is weak
  → Add schema where appropriate
  → Re-submit URL in GSC
```
