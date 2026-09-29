# Sample run — /gsc-quick-wins

**Input:** `examples/sample-Queries.csv` (a fictional running-shoe blog, last 3 months)
**Prompt:** "/gsc-quick-wins — here's my Queries.csv. Find my quick wins."

---

## Priority keywords

| Keyword | Position | Impressions | CTR | Issue | Action |
|---|---|---|---|---|---|
| how to clean white sneakers | 5.3 | 12,400 | 0.77% | CTR is ~10× below benchmark for #5 | Rewrite title + meta |
| marathon training plan for beginners | 11.4 | 15,600 | 0.77% | No dedicated plan section; page 2 | Add H2 + week-by-week table |
| running shoes vs walking shoes | 7.8 | 8,900 | 3.48% | CTR is fine — content depth is the gap | Add comparison section + FAQ |
| trail running shoes waterproof | 9.2 | 3,900 | 1.15% | Weak title + thin section | Add section, fix title |

Skipped: `best running shoes for flat feet` (already #2), `running shoe size guide` (#24.8, too far), `sneaker cleaning kit` (90 impressions — not enough volume).

---

## 1. "how to clean white sneakers" — position 5.3

**Diagnosis:** A #5 result should get ~6–9% CTR; this gets 0.77%. The page ranks — searchers just aren't choosing it. That's a title/snippet problem, not a content problem.

**Title & meta**
- Current title: *Sneaker Care Tips | RunBlog*
- Suggested title: **How to Clean White Sneakers (5 Steps, No Yellowing)**
- Suggested meta: *Get white sneakers bright again in 20 minutes with things already in your kitchen. Step-by-step for canvas, leather and mesh — plus what never to use.* (153 chars)

**Schema**
- [ ] Add `HowTo` schema for the 5 steps — can unlock a rich result on this query

**Post-update**
- [ ] URL Inspection → Request Indexing · re-check CTR in 2–3 weeks

---

## 2. "marathon training plan for beginners" — position 11.4

**Diagnosis:** Highest-volume row in the window. The page talks *about* training but has no actual plan, so Google hedges at #11.

**Content**
- [ ] Add H2: **Marathon Training Plan for Beginners (16 Weeks)**
- [ ] Under it, a week-by-week table: week, long run, total mileage, key workout
- [ ] Answer adjacent questions as H3s:
  - How many weeks do you need to train for a first marathon?
  - How many miles a week should a beginner run?
  - Can you walk during a marathon training plan?
  - What should you eat the week before a marathon?
- [ ] Add entities: taper, long run, easy pace, cross-training, carb loading

**Internal links**
- [ ] From *how long do running shoes last* → anchor "beginner marathon training plan"
- [ ] From *couch to 5k app* → anchor "your next step: a marathon plan"

**Title:** *Marathon Training Plan for Beginners: Free 16-Week Schedule*

---

## Where to start

**This week:** #1 (title/meta only — 15 minutes) and #2 (biggest upside).
**Next week:** #3 and #4.
**Later:** positions 13–20 once the first batch has been re-crawled.
