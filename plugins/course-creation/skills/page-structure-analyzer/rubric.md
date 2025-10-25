# Page Structure Evaluation Rubric

This rubric is used by the page-structure-analyzer skill to evaluate e-learning content pages.

## Scoring System (0-20 points total)

### 1. Clear Learning Objective (0-2 points)

| Score | Criteria |
|-------|----------|
| 2 pts | Learning objective explicitly stated at start (what learner will know/do after this section) |
| 1 pt  | Objective implied but not explicitly stated |
| 0 pts | No clear objective |

**Examples:**
- ✅ 2 pts: "In this section, you'll learn how AI identifies patterns in data and why this matters for your daily work."
- ⚠️ 1 pt: "Let's explore how AI works..." (implies learning but not specific)
- ❌ 0 pts: Jumps straight into content without framing

---

### 2. Logical Structure (0-3 points)

| Score | Criteria |
|-------|----------|
| 3 pts | Clear intro → body → conclusion/summary structure; each part serves distinct purpose |
| 2 pts | Has structure but lacks clear intro or conclusion |
| 1 pt  | Some structure but flow is unclear |
| 0 pts | No discernible structure; content feels random |

**What to look for:**
- **Intro**: Sets up what's coming, provides context
- **Body**: Delivers main content in logical chunks
- **Conclusion/Summary**: Wraps up, transitions to next section

---

### 3. Appropriate Length (0-2 points)

**Target**: 300-600 words per section (3-5 minute reading time)
**Calculation**: ~200 words per minute reading speed for non-technical content

| Score | Criteria |
|-------|----------|
| 2 pts | 300-600 words (optimal cognitive load) |
| 1 pt  | 250-300 or 600-700 words (acceptable but not ideal) |
| 0 pts | <250 words (feels incomplete) OR >700 words (cognitive overload) |

**Rationale:**
- **Too short**: Learner doesn't get enough depth
- **Too long**: Working memory overload, learner fatigue
- **Just right**: Matches microlearning best practices

---

### 4. Information Chunking (0-3 points)

**Based on**: Cognitive Load Theory (working memory holds ~7 chunks, works on ~4)

| Score | Criteria |
|-------|----------|
| 3 pts | Content broken into 3-4 clear chunks with headings/subheadings; one concept per chunk |
| 2 pts | Some chunking (5-6 chunks) but could be clearer |
| 1 pt  | Minimal chunking; mostly walls of text with few breaks |
| 0 pts | No chunking; overwhelming single block |

**What good chunking looks like:**
```markdown
## Main Concept 1
[2-3 paragraphs]

## Main Concept 2
[2-3 paragraphs]

## Main Concept 3
[2-3 paragraphs]
```

---

### 5. Visual Scannability (0-2 points)

**Adult learners scan before reading** - make it easy!

| Score | Criteria |
|-------|----------|
| 2 pts | Uses headings, short paragraphs (<5 sentences), bullet points/lists, white space effectively |
| 1 pt  | Some formatting but inconsistent or insufficient |
| 0 pts | Dense blocks of text with no visual aids |

**Scannable elements:**
- Headings/subheadings
- Bullet points or numbered lists
- Short paragraphs (3-5 sentences)
- Bold/emphasis on key terms
- White space between sections

---

### 6. Progression/Flow (0-3 points)

**Good content builds like stairs**, not jumps around.

| Score | Criteria |
|-------|----------|
| 3 pts | Ideas build logically; clear transitions; intro previews what's coming; learner always knows "where am I in this?" |
| 2 pts | Generally logical but some abrupt jumps between ideas |
| 1 pt  | Flow is confusing; ideas feel disconnected |
| 0 pts | No discernible progression; random order |

**Typical good progression:**
1. **Foundation** → Establish basic concept
2. **Details** → Add depth and nuance
3. **Application** → Show how it applies to learner
4. **Transition** → Bridge to next section

---

### 7. Examples/Application (0-2 points)

**Abstract concepts need concrete anchors** for non-technical learners.

| Score | Criteria |
|-------|----------|
| 2 pts | Includes concrete examples that relate to learner's context (work tasks, familiar tools) |
| 1 pt  | Has examples but they feel generic/abstract |
| 0 pts | No examples; purely theoretical/definitional |

**Good example characteristics:**
- Specific (not "AI can help with work" but "AI can sort your inbox so urgent emails surface first")
- Relatable (from learner's world, not AI researcher's world)
- Illustrative (clarifies the concept, not just decoration)

---

### 8. Cognitive Load Management (0-3 points)

**Respects working memory limitations** and reduces mental strain.

| Score | Criteria |
|-------|----------|
| 3 pts | New concepts introduced one at a time; builds on prior knowledge; minimal jargon; clear definitions when technical terms necessary |
| 2 pts | Mostly manageable but some dense sections or unexplained jargon |
| 1 pt  | Introduces too many concepts too quickly; assumes too much |
| 0 pts | Overwhelming; feels like reading a research paper |

**Cognitive load reducers:**
- Introduce one new concept per chunk
- Reference previously explained concepts
- Define technical terms on first use
- Use analogies from learner's world
- Keep sentence structure simple

---

## Interpretation Guide

### Total Score: 0-20 points

| Range | Rating | Interpretation |
|-------|--------|----------------|
| 18-20 | Excellent | Publication-ready; minor tweaks at most |
| 15-17 | Good | Solid content; some improvements will elevate quality |
| 12-14 | Acceptable | Usable but needs work in multiple areas |
| 9-11  | Needs Work | Significant issues; requires revision |
| 0-8   | Major Revision | Fundamental restructuring needed |

### What to Prioritize

If score is <15, focus on lowest-scoring dimensions first:
- **Structure (dim 2) low?** → Reorganize before fixing details
- **Chunking (dim 4) low?** → Break apart before wordsmithing
- **Examples (dim 7) low?** → Add concrete cases to abstract concepts
- **Cognitive load (dim 8) low?** → Simplify before expanding

---

## Context-Specific Adjustments

### For AI4E Course:
- **Target audience**: Non-technical employees, anxious about AI
- **Tone**: Professional-Direct (see `courses/{COURSE_NAME}/docs/style-guide.md`)
- **Total course time**: ~50 minutes across 5 modules
- **Module context matters**:
  - Module 1 (intro): Can be shorter, sets expectations
  - Module 2 (foundations): Richer, more detailed
  - Module 3 (application): Practical, example-heavy
  - Module 4 (personalized): Variable length
  - Module 5 (summary): Intentionally brief

Apply rubric with course context in mind.
