---
description: Reverse-engineer course documentation from existing content (course analyzer)
---

Launch a **general-purpose agent** to analyze your existing course content and generate formal documentation (syllabus, module outlines, research brief).

## Prerequisites

Extract the course name from the user's input:
- Example: `/analyze my-ai-course` → Course is "my-ai-course"
- If course name missing, ask: "Which course would you like to analyze?"

You should have:
- Existing content files in `courses/{COURSE_NAME}/content/` directory
- Some content already written (even if incomplete)

## Use Case

**When to use this command:**
- ✅ You have existing course content but no formal syllabus
- ✅ You want to improve/rebuild existing course systematically
- ✅ You need to extract structure from legacy content
- ✅ You want to go through design workflow with existing content as starting point

**When NOT to use:**
- ❌ Starting from scratch → Use `/design-course` instead

## How It Works

The agent will:
1. **Scan existing content** in `courses/{COURSE_NAME}/content/` directory
2. **Extract course structure** (modules, topics, objectives)
3. **Analyze citations** to build research brief
4. **Reverse-engineer module outlines** from content
5. **Generate syllabus** matching existing structure
6. **Present documentation** for your review
7. **Save to `courses/{COURSE_NAME}/docs/`** for future workflow

## Task for the Agent

When the user runs `/analyze {COURSE_NAME}`, you (the general-purpose agent) should analyze existing content and generate course documentation.

---

### Step 1: Scan Existing Content

**Read all content files:**
```bash
# Find all markdown files in courses/{COURSE_NAME}/content/
courses/{COURSE_NAME}/content/*.md
```

**For each file, extract:**
- File name pattern (module number, section number, topic)
- Module title (from header)
- Section title (from header)
- Time estimate (if present in header)
- Word count (approximate reading time)
- Main headers (topics covered)
- Learning concepts (what's being taught)
- Examples used (concrete scenarios)
- Citations (numbered references)
- Customization markers (if any)

**Organize findings by module:**
```
Module 1:
  - Sections found: [list]
  - Topics covered: [list]
  - Total word count: [X]

Module 2:
  - Sections found: [list]
  - Topics covered: [list]
  - Total word count: [X]

...
```

---

### Step 2: Analyze Course Structure

**Determine overall course structure:**

**A. Identify Modules**
- Count distinct modules (based on file naming)
- Determine module sequence (1, 2, 3...)
- Note any gaps (missing modules)

**B. Extract Module Characteristics**
For each module:
- Module title (from content)
- Number of sections
- Topics covered (from headers)
- Estimated duration (from word counts: ~200-250 words/min)
- Instructional approach (concept-first, example-driven, etc.)

**C. Infer Learning Objectives**
Based on content, determine what learners should achieve:
- Look for patterns: "You will learn...", "By the end..."
- Analyze what's actually taught
- Identify key takeaways from each module
- Formulate as measurable objectives

**Example:**
```
Module 2 teaches:
- AI definition → Objective: "Define AI and distinguish it from traditional software"
- Training data concepts → Objective: "Explain how AI learns from training data"
- Bias examples → Objective: "Identify potential bias in AI systems"
```

**D. Identify Course Goals**
Synthesize overall course objectives:
- What's the big picture?
- What should learners be able to do after completing ALL modules?
- What's the primary outcome?

---

### Step 3: Extract Citations & Research

**Scan all content for citations:**

**A. Find All References**
- Look for numbered citations: [1], [2], [3]
- Look for reference sections at bottom of files
- Extract full citation details

**B. Categorize Sources**
Group by type:
- Academic (universities, research institutions)
- Industry (McKinsey, BCG, company reports)
- Government (Singapore govt, IMDA, etc.)
- Technical (AI company research, whitepapers)

**C. Note Research Gaps**
- Claims without citations
- Placeholders like [RESEARCH NEEDED]
- Statistics without sources

**D. Identify Research Themes**
What topics were researched:
- AI definitions and concepts
- Bias in AI systems
- Industry applications
- Singapore/SEA context
- Learning science (if applicable)

---

### Step 4: Reverse-Engineer Module Outlines

For each module, create detailed outline:

**Template:**
```markdown
# Module [N]: [Title]

**Duration:** [X] minutes (based on [Y] words)
**Position in Course:** Module [N] of [Total]

## Learning Objectives

- [Objective 1 - inferred from content]
- [Objective 2 - inferred from content]
- [Objective 3 - inferred from content]

## Prerequisites

- [What learners should know from previous modules]
- [If Module 1: No prerequisites]

## Content Structure

### Section [N].1: [Title]
**Purpose:** [What this section achieves - inferred]
**Key Concepts:**
- [Concept 1 - from headers/content]
- [Concept 2 - from headers/content]

**Examples Present:**
- [Example 1 - extracted from content]
- [Example 2 - extracted from content]

**Citations Used:**
- [Citation 1]
- [Citation 2]

---

### Section [N].2: [Title]
[Same structure]

---

## Assessment

**Type:** [Identified from content, if present]
**Format:** [Identified from content]

## Success Criteria

This module succeeds when learners can:
- [Outcome 1 - based on content taught]
- [Outcome 2 - based on content taught]

## Development Notes

**Existing Content Status:**
- ✅ All sections written
- OR
- ⚠️ Section [X] incomplete
- ❌ Section [Y] missing

**Content Quality:**
- Word count: [X] words
- Time estimate: [Y] minutes
- Citations: [Z] sources
- Examples: [A] concrete scenarios

**Identified Gaps:**
- [Gap 1: Missing content]
- [Gap 2: Needs more examples]
- [Gap 3: Citation needed for claim X]

**Strengths:**
- [Strength 1: What works well]
- [Strength 2: Good examples/structure]
```

---

### Step 5: Generate Course Syllabus

Create comprehensive syllabus matching existing content:

```markdown
# [Course Title] - Course Syllabus

**Version:** 1.0 (Reverse-Engineered from Existing Content)
**Generated:** [Date]
**Total Duration:** [X] minutes
**Status:** Existing content analyzed, formal documentation created

---

## GENERATION NOTE

This syllabus was reverse-engineered from existing course content in `courses/{COURSE_NAME}/content/` directory.
- Analyzed [X] modules, [Y] sections
- Extracted [Z] learning objectives
- Identified [A] citations
- Total content: [B] words

**Next Steps:**
1. Review this syllabus for accuracy
2. Refine with `/refine-syllabus` if needed
3. Use `/build-module` to improve/rebuild modules
4. Use `style-extractor` to create style guide from existing content

---

## Course Overview

**Topic:** [Inferred from content]
**Target Audience:** [From target-audience.md if exists, else infer]
**Delivery Format:** [Self-paced / Inferred]
**Learning Outcomes:** [Synthesized from modules]

---

## Learning Objectives

By the end of this course, learners will be able to:

1. [Objective 1 - synthesized from Module 1-2]
2. [Objective 2 - synthesized from Module 2-3]
3. [Objective 3 - synthesized from all modules]
4. [Objective 4 - overall outcome]

---

## Course Structure

### Module 1: [Title]
**Duration:** [X] minutes
**Sections:** [N] sections
**Topics:**
- [Topic 1]
- [Topic 2]

**Learning Objectives:**
- [Objective 1]
- [Objective 2]

**Status:** ✅ Content exists ([X] words)

---

### Module 2: [Title]
**Duration:** [X] minutes
**Sections:** [N] sections
**Topics:**
- [Topic 1]
- [Topic 2]

**Learning Objectives:**
- [Objective 1]
- [Objective 2]

**Status:** ✅ Content exists ([X] words)

---

### Module [N]: [Title]
[Same structure for all identified modules]

---

## Time Allocation

| Module | Sections | Word Count | Est. Duration | % of Total |
|--------|----------|------------|---------------|------------|
| 1 | [X] | [Y] words | [Z] min | [%] |
| 2 | [X] | [Y] words | [Z] min | [%] |
| ... | ... | ... | ... | ... |
| **Total** | **[X]** | **[Y] words** | **[Z] min** | **100%** |

---

## Content Analysis

### Strengths Identified:
- [Strength 1: From content analysis]
- [Strength 2: Good examples/structure]
- [Strength 3: Strong research backing]

### Gaps Identified:
- [Gap 1: Missing module]
- [Gap 2: Incomplete section]
- [Gap 3: Needs more citations]

### Recommendations:
1. [Recommendation 1: What to improve]
2. [Recommendation 2: What to add]
3. [Recommendation 3: What to refine]

---

## Pedagogical Approach

**Identified Pattern:** [Concept-first / Example-driven / Hybrid]

**Instructional Strategy:**
- [How content is structured]
- [How concepts are introduced]
- [How examples are used]

**Content Flow:**
- [Module 1-2: Foundation]
- [Module 3-4: Application]
- [Module 5: Practice/Summary]

---

## Citation Summary

**Total Sources:** [X]
- Academic: [X]
- Industry: [X]
- Government: [X]
- Technical: [X]

**Research Coverage:**
- [Topic 1: X citations]
- [Topic 2: X citations]

**Research Gaps:**
- [Area needing more sources]

---

## Next Steps

### Immediate Actions:

1. **Review this syllabus**
   - Confirm structure matches your intent
   - Verify learning objectives are accurate
   - Check time allocations

2. **Create style guide** (if not exists)
   ```bash
   # Copy best existing sections as examples
   cp courses/{COURSE_NAME}/content/2_*.md .claude/skills/style-extractor/examples/{COURSE_NAME}/good/

   # Generate style guide
   Skill style-extractor
   ```

3. **Refine syllabus** (if needed)
   ```bash
   /refine-syllabus "Your adjustments"
   ```

### Development Actions:

4. **Rebuild modules** using formal structure
   ```bash
   /build-module 1  # Rebuild with style guide + module outline
   /build-module 2  # Rebuild with research + standards
   ```

5. **Fill gaps**
   - Add missing modules
   - Complete incomplete sections
   - Add missing citations

6. **Quality review**
   ```bash
   /content-review module 1
   /fix-from-review
   ```

---

**End of Syllabus**
```

---

### Step 6: Generate Research Brief

Create research documentation from existing citations:

```markdown
# Research Brief - [Course Title]

**Generated:** [Date]
**Source:** Reverse-engineered from existing content citations
**Total Sources Identified:** [X]

---

## GENERATION NOTE

This research brief was extracted from citations in existing course content.
It represents research ALREADY USED in the course.

**For comprehensive course redesign:**
- Review these sources
- Identify research gaps
- Conduct additional research as needed
- Update with `/design-course` or manual additions

---

## Citations by Module

### Module 1: [Title]
**Sources Used:** [X]

1. [Citation 1 with full details]
2. [Citation 2 with full details]

**Topics Researched:**
- [Topic 1: What these sources cover]
- [Topic 2]

---

### Module 2: [Title]
**Sources Used:** [X]

[Same structure]

---

## Citations by Category

### Academic Sources ([X] total)
1. [Citation]
2. [Citation]

### Industry Research ([X] total)
1. [Citation]
2. [Citation]

### Government/Institutional ([X] total)
1. [Citation]
2. [Citation]

### Technical/Company Research ([X] total)
1. [Citation]
2. [Citation]

---

## Research Coverage Analysis

### Well-Researched Topics:
- [Topic 1: X sources]
- [Topic 2: X sources]

### Under-Researched Topics:
- [Topic 1: Only X sources, needs more]
- [Topic 2: No sources found]

### Missing Research:
- [Area 1: No citations for claims about X]
- [Area 2: Statistics unsourced]

---

## Singapore/SEA Context

**Regional Sources Used:** [X]
- [Singapore source 1]
- [SEA source 2]

**Regional Examples Present:**
- [Example 1: DBS Bank]
- [Example 2: Changi Airport]

**Opportunities:**
- [Where more regional context would help]

---

## Key Findings (Inferred from Content)

### [Topic Area 1]
**Finding:** [What content teaches based on research]
**Sources:** [Citations used]
**Application:** [How applied in course]

### [Topic Area 2]
[Same structure]

---

## Research Quality Assessment

**Strengths:**
- [Strength 1: Credible sources]
- [Strength 2: Recent research]
- [Strength 3: Diverse source types]

**Gaps:**
- [Gap 1: Missing sources for topic X]
- [Gap 2: Old sources that need updating]
- [Gap 3: Lack of regional sources]

**Recommendations:**
1. [Add research for topic X]
2. [Update outdated sources]
3. [Find more Singapore/SEA examples]

---

## Additional Research Needed

To strengthen course:
1. **[Topic 1]**
   - Current: [X] sources
   - Recommended: [Y] sources
   - Focus: [What to research]

2. **[Topic 2]**
   [Same structure]

---

**End of Research Brief**
```

---

### Step 7: Present Analysis to User

Show comprehensive analysis:

```markdown
## ✅ EXISTING COURSE ANALYZED

**Content Scanned:** [X] files in `courses/{COURSE_NAME}/content/` directory

---

### 📊 COURSE STRUCTURE IDENTIFIED

**Modules Found:** [X] modules
**Total Sections:** [Y] sections
**Total Content:** [Z] words (~[A] minutes)

**Module Breakdown:**
| Module | Title | Sections | Word Count | Est. Time | Status |
|--------|-------|----------|------------|-----------|--------|
| 1 | [Title] | [X] | [Y] words | [Z] min | ✅ Complete |
| 2 | [Title] | [X] | [Y] words | [Z] min | ✅ Complete |
| 3 | [Title] | [X] | [Y] words | [Z] min | ⚠️ Incomplete |
| 4 | [Title] | [X] | [Y] words | [Z] min | ❌ Missing |

---

### 📚 RESEARCH IDENTIFIED

**Citations Found:** [X] total
- Academic: [X]
- Industry: [X]
- Government: [X]
- Singapore/SEA: [X]

**Well-Cited Topics:**
- [Topic 1: X citations]
- [Topic 2: X citations]

**Research Gaps:**
- [Topic needing more sources]
- [Unsourced claims found]

---

### 🎯 LEARNING OBJECTIVES EXTRACTED

**Course-Level Objectives:**
1. [Objective 1 - what learners achieve overall]
2. [Objective 2]
3. [Objective 3]

**Module-Level Objectives:**
- Module 1: [Objectives]
- Module 2: [Objectives]
- Module 3: [Objectives]

---

### ✅ STRENGTHS IDENTIFIED

1. **[Strength 1]**
   - [Details from analysis]

2. **[Strength 2]**
   - [Details from analysis]

3. **[Strength 3]**
   - [Details from analysis]

---

### ⚠️ GAPS IDENTIFIED

1. **[Gap 1: e.g., Missing Module 4]**
   - Impact: [How this affects course]
   - Recommendation: [What to do]

2. **[Gap 2: e.g., Incomplete Section 3.2]**
   - Impact: [How this affects learning]
   - Recommendation: [What to do]

3. **[Gap 3: e.g., Limited citations in Module 1]**
   - Impact: [Credibility issue]
   - Recommendation: [Research needed]

---

### 📄 DOCUMENTATION GENERATED

I've created formal course documentation based on your existing content:

**✅ Created:**
- `courses/{COURSE_NAME}/docs/course-syllabus.md` - Reverse-engineered course structure
- `courses/{COURSE_NAME}/docs/module-outlines/module_[N]_outline.md` - One per module found
- `courses/{COURSE_NAME}/docs/research-brief.md` - Compiled from existing citations

**These files now exist in `courses/{COURSE_NAME}/docs/` for easy review.**

---

### 🎯 RECOMMENDED NEXT STEPS

**1. Review Generated Documentation**
```bash
# Check reverse-engineered syllabus
cat courses/{COURSE_NAME}/docs/course-syllabus.md

# Check module outlines
ls courses/{COURSE_NAME}/docs/module-outlines/

# Check research brief
cat courses/{COURSE_NAME}/docs/research-brief.md
```

**2. Create Style Guide** (if not exists)
```bash
# Use existing content as examples
cp courses/{COURSE_NAME}/content/2_2_*.md .claude/skills/style-extractor/examples/{COURSE_NAME}/good/
cp courses/{COURSE_NAME}/content/2_3_*.md .claude/skills/style-extractor/examples/{COURSE_NAME}/good/

# Generate style guide
Skill style-extractor

# Output: courses/{COURSE_NAME}/docs/style-guide.md
```

**3. Refine Syllabus** (optional)
```bash
# Adjust structure based on analysis
/refine-syllabus "Split Module 2, add Module 5 on ethics"
```

**4. Rebuild/Improve Modules**
```bash
# Rebuild with formal structure + style guide + research
/build-module 1  # Improved version
/build-module 2  # Improved version
/build-module 3  # Complete the incomplete one
/build-module 4  # Build the missing one
```

**5. Quality Review**
```bash
/content-review module 1
/fix-from-review
```

---

### 💡 WHAT YOU NOW HAVE

**Before `/analyze-existing-course`:**
- ✅ Content files
- ❌ No formal syllabus
- ❌ No module outlines
- ❌ No research brief
- ❌ No style guide

**After `/analyze-existing-course`:**
- ✅ Content files (same)
- ✅ Formal syllabus (generated)
- ✅ Module outlines (generated)
- ✅ Research brief (generated)
- ⏭️ Style guide (next step: run `style-extractor`)

**You can now:**
- Use full design workflow to improve course
- Rebuild modules systematically with style guide
- Fill identified gaps
- Strengthen research backing

---

**Ready to review the generated documentation?**
```bash
cat courses/{COURSE_NAME}/docs/course-syllabus.md
```

Or would you like me to refine any part of the analysis?
```

Wait for user feedback.

---

## Important Guidelines

### Content Analysis
- **Read thoroughly** - Don't just scan file names, read actual content
- **Infer intelligently** - Extract learning objectives from what's taught
- **Identify patterns** - Recognize instructional approach used
- **Note quality** - Flag strengths and gaps

### Documentation Generation
- **Match existing structure** - Don't redesign, reverse-engineer
- **Preserve content** - Don't lose what's already there
- **Add formality** - Create proper syllabus/outlines from informal content
- **Enable workflow** - Generated docs should plug into existing commands

### Presentation
- **Be thorough** - Show all findings
- **Be honest** - Highlight gaps and weaknesses
- **Be constructive** - Frame gaps as opportunities
- **Give clear next steps** - Tell user exactly what to do next

### File Management
- **Save to `courses/{COURSE_NAME}/docs/`** - All generated documentation goes here
- **Don't overwrite content** - Content files stay untouched
- **Create module outlines** - One file per module
- **Format consistently** - Match format of `/design-course` output

---

## Success Criteria

This command succeeds when:
- ✅ All existing content analyzed
- ✅ Course structure accurately extracted
- ✅ Learning objectives intelligently inferred
- ✅ Citations compiled into research brief
- ✅ Module outlines created for each module
- ✅ Formal syllabus generated
- ✅ All files saved to `courses/{COURSE_NAME}/docs/`
- ✅ User can now use full workflow to improve course

The course now has formal documentation and can be systematically improved using existing commands.
