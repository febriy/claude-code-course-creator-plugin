---
description: Research and design a complete course curriculum from initial concept (course architect)
---

Launch a **general-purpose agent** to research, design, and propose a complete course curriculum from your initial concept.

## Prerequisites

You should have a rough idea of:
- What topic you want to teach
- Who the target audience is
- What learners should achieve
- Time constraints (if any)

## How It Works

The agent will:
1. **Gather requirements** through interactive Q&A or from your description
2. **Research extensively** using web search for best practices, existing curricula, learning science
3. **Synthesize findings** into a coherent course design
4. **Validate structure** using module-progression-analyzer skill
5. **Present proposal** with research sources and rationale
6. **Iterate** based on your feedback
7. **Save final syllabus** and supporting documents

## Task for the Agent

When the user runs `/design-course`, you (the general-purpose agent) should design a complete course curriculum from scratch.

### Step 1: Gather Requirements

**If user provides full description:**
```
/design-course "AI literacy for non-technical employees, 50 minutes total, mandatory training, must result in practical application within 1 week"
```
Parse it and proceed to Step 2.

**If user provides minimal info:**
```
/design-course
```

Ask these questions:
1. **What is the course topic/subject?**
   - Example: "AI literacy for general workforce"

2. **Who is the target audience?**
   - Role/level: (e.g., "non-technical employees, individual contributors")
   - Prior knowledge: (e.g., "0-2 years AI experience, anxious about AI")
   - Size: (e.g., "company-wide, 500+ employees")

3. **What should learners be able to DO after completing this course?**
   - Specific, measurable outcomes
   - Focus on application, not just knowledge
   - Example: "Identify one AI tool to use in their work this week"

4. **How much time do you have?**
   - Total duration: (e.g., "50 minutes")
   - Format: (e.g., "self-paced virtual", "live instructor-led")
   - Constraints: (e.g., "must be completable in one sitting")

5. **Any other constraints or requirements?**
   - Mandatory or optional?
   - Assessment requirements?
   - Existing tools/systems to integrate?
   - Organizational culture considerations?

---

### Step 2: Research Phase

Use **WebSearch** extensively to gather information. Aim for 10-15 high-quality sources.

#### **A. Topic Research**
Search for:
- "best practices teaching [topic]"
- "[topic] curriculum design"
- "[topic] training for [audience type]"
- "how to teach [topic] to beginners"
- "[topic] learning objectives"
- "common misconceptions about [topic]"

**Source filtering:**
- ✅ Academia: University research, educational journals, learning science papers
- ✅ Industry: McKinsey, BCG, Deloitte, World Economic Forum reports
- ✅ Government: Singapore government, IMDA, national education agencies
- ✅ Reputable institutions: Stanford HAI, MIT Media Lab, tech company research labs
- ❌ Avoid: Personal blogs, forums, unverified sources

**Geography:**
- Prioritize Singapore/SEA sources when relevant to audience
- Don't force local examples if global examples are stronger
- Consider: Is this course for Singapore audience? (If yes, seek local context)

#### **B. Audience Research**
Search for:
- "[audience type] learning challenges"
- "teaching [topic] to [audience]"
- "[audience] professional development needs"
- "adult learning best practices"
- "motivating [audience] to learn [topic]"

Look for:
- What does this audience typically struggle with?
- What motivates them?
- What are their time constraints?
- What's their existing knowledge level?

#### **C. Competitive Analysis**
Search for:
- Existing courses on this topic
- Industry training programs
- Certification curricula
- Bootcamp structures

Analyze:
- What do they cover?
- How long are they?
- What works well? (from reviews/feedback)
- What's missing?
- How can your course be better/different?

#### **D. Learning Science Research**
Search for:
- "optimal module length adult learners"
- "instructional design for [topic]"
- "assessment strategies [topic]"
- "effective examples for teaching [topic]"

Look for:
- Recommended time per module
- Effective teaching strategies for this topic
- Assessment approaches that work
- Common pitfalls to avoid

---

### Step 3: Synthesize & Design

Based on research, create a draft course syllabus:

#### **A. Define Learning Objectives**
- Start with end goals (what learners will DO)
- Work backward to identify prerequisite knowledge
- Ensure objectives are:
  - Specific (not vague)
  - Measurable (observable)
  - Achievable (within time constraints)
  - Relevant (to learner's real work)
  - Time-bound (within course duration)

#### **B. Create Module Structure**
**Principles:**
- Foundation before application
- Simple before complex
- Awareness before skill
- Each module builds on previous

**Typical patterns:**
- **Foundation → Application → Advanced**
  - Module 1: What is [topic]?
  - Module 2: [Topic] in practice
  - Module 3: Advanced [topic] techniques

- **Awareness → Knowledge → Skill → Mastery**
  - Module 1: Why [topic] matters
  - Module 2: How [topic] works
  - Module 3: Using [topic]
  - Module 4: Mastering [topic]

- **Problem → Solution → Practice**
  - Module 1: The challenge
  - Module 2: How [solution] works
  - Module 3: Applying [solution]

**For each module, specify:**
- Title (clear, descriptive)
- Duration (realistic based on content)
- Learning objectives (what learner will achieve)
- Key concepts to cover
- Examples needed (concrete, relevant)
- Assessment approach (if any)

#### **C. Allocate Time**
**Guidelines:**
- Adult learners: 10-20 minutes per module optimal
- Foundational modules may need more time
- Total should match constraints ±5 minutes
- Balance: No module should be 2x another without reason
- Reading speed: ~200-250 words/minute for non-technical content

**Example time allocation (50-minute course):**
- Module 1 (Foundation): 12 min (25%)
- Module 2 (Application): 15 min (30%)
- Module 3 (Deep Dive): 13 min (26%)
- Module 4 (Practice): 10 min (19%)

#### **D. Identify Content Requirements**
For each module, note:
- What examples are needed? (concrete scenarios)
- What research/citations required? (statistics, studies)
- What visuals would help? (diagrams, tables)
- What interactive elements? (activities, scenarios)
- What customization opportunities? (personalization points)

---

### Step 4: Validate with module-progression-analyzer

Use the `module-progression-analyzer` skill to check:
- Do modules flow logically?
- Are there dependency issues? (Module 3 needs knowledge from Module 5?)
- Is time allocation balanced?
- Are there gaps in objective coverage?
- Is there redundancy between modules?

If issues found:
- Reorder modules
- Split oversized modules
- Merge undersized modules
- Redistribute time
- Add missing modules
- Remove redundant content

Run the skill again until flow quality is "Good" or "Excellent."

---

### Step 5: Present Proposal

Create a comprehensive proposal document:

```markdown
# COURSE DESIGN PROPOSAL: [Course Title]

**Designed:** [Date]
**Target Audience:** [Description]
**Duration:** [Total time]
**Delivery Format:** [Self-paced / Instructor-led / Hybrid]

---

## EXECUTIVE SUMMARY

[2-3 paragraphs explaining:
- What this course teaches
- Why it's designed this way
- How it differs from alternatives
- Expected learner outcomes]

---

## LEARNING OBJECTIVES

By the end of this course, learners will be able to:

1. [Objective 1 - specific, measurable, action-oriented]
2. [Objective 2]
3. [Objective 3]
4. [Objective 4]

**Validation:** [How you'll measure achievement]

---

## TARGET AUDIENCE

**Primary Audience:**
- Role: [e.g., Non-technical employees, individual contributors]
- Experience: [e.g., 0-2 years with AI, comfortable with basic technology]
- Motivation: [e.g., Mandatory training, seeking practical skills]

**Learning Context:**
- Setting: [e.g., Virtual, self-paced via LMS]
- Constraints: [e.g., Must complete during work hours, interruptions likely]
- Mindset: [e.g., Skeptical but pragmatic, time-pressured]

**Prerequisites:**
- [What learners need to know beforehand]

---

## COURSE SYLLABUS

### Module 1: [Title] ([X] minutes)

**Learning Objectives:**
- [Objective 1]
- [Objective 2]

**Content Outline:**
1. Section 1.1: [Topic] ([Y] min)
   - [What it covers]
   - Key concepts: [list]

2. Section 1.2: [Topic] ([Y] min)
   - [What it covers]
   - Key concepts: [list]

**Key Examples Needed:**
- [Example 1: specific scenario]
- [Example 2: specific scenario]

**Assessment:** [Type - quiz, scenario, reflection]

**Critical Success Factors:**
- [What makes this module effective]

---

### Module 2: [Title] ([X] minutes)

[Same structure as Module 1]

---

[Continue for all modules]

---

## INSTRUCTIONAL STRATEGY

**Pedagogical Approach:**
[e.g., Problem-based learning, Example-driven, Concept-first, etc.]

**Content Structure Pattern:**
[e.g., Concept → Example → Practice → Application]

**Engagement Mechanisms:**
- [How you'll keep learners engaged]
- [Interactive elements]
- [Real-world connections]

**Assessment Strategy:**
- [How learning will be measured]
- [Low-stakes vs high-stakes]
- [Formative vs summative]

**Customization Approach:**
- [Where personalization adds value]
- [What can be adapted to learner context]

---

## TIME ALLOCATION ANALYSIS

**Total Allocated:** [X] minutes
**Target Duration:** [Y] minutes
**Buffer:** [Z] minutes (for variability in reading speed)

| Module | Duration | % of Total | Rationale |
|--------|----------|------------|-----------|
| Module 1 | [X] min | [Y]% | [Why this allocation] |
| Module 2 | [X] min | [Y]% | [Why this allocation] |
| Module 3 | [X] min | [Y]% | [Why this allocation] |
| **Total** | **[X] min** | **100%** | |

**Time Validation:**
- Average reading speed: 200-250 words/minute
- Interactive elements: +20% time
- Cognitive processing: +15% time

---

## MODULE PROGRESSION VALIDATION

[Insert output from module-progression-analyzer skill]

**Flow Quality:** [Excellent/Good/Needs Work]

**Key Strengths:**
- [How modules build on each other]
- [Logical progression]

**Addressed Issues:**
- [Any issues found and how you fixed them]

---

## RESEARCH FOUNDATION

This course design is informed by:

**Academic Sources:**
1. [Source 1: Citation]
2. [Source 2: Citation]

**Industry Research:**
3. [Source 3: Citation]
4. [Source 4: Citation]

**Government/Institutional:**
5. [Source 5: Citation]

**Learning Science:**
6. [Source 6: Citation]

[List all 10-15 sources with full citations]

**Key Findings Applied:**
- [Finding 1 from research and how it influenced design]
- [Finding 2 from research and how it influenced design]

---

## CUSTOMIZATION OPPORTUNITIES

**Identified Personalization Points:**

1. **[Customization area 1]**
   - Where: [Module X, Section Y]
   - What varies: [Industry examples, role-specific scenarios, etc.]
   - Why it matters: [Increases relevance for learner]

2. **[Customization area 2]**
   [Same structure]

**Implementation Approach:**
- [How customization markers will be added]
- [How intake form will collect learner data]

---

## DEVELOPMENT ROADMAP

**Phase 1: Module 1 Development**
- Research specific topics for Module 1
- Draft all sections
- Add examples and citations
- Review and refine
- **Estimated time:** [X hours]

**Phase 2: Module 2 Development**
- [Same structure]
- **Estimated time:** [X hours]

**Phase 3: Module 3 Development**
- [Same structure]
- **Estimated time:** [X hours]

**Total Estimated Development Time:** [X hours]

---

## ALTERNATIVE APPROACHES CONSIDERED

**Alternative A: [Different structure]**
- Approach: [Description]
- Pros: [Benefits]
- Cons: [Trade-offs]
- Why not chosen: [Rationale]

**Alternative B: [Different approach]**
- Approach: [Description]
- Pros: [Benefits]
- Cons: [Trade-offs]
- Why not chosen: [Rationale]

**Why the proposed design is better:**
[Clear explanation of why this design best meets learner needs and objectives]

---

## SUCCESS METRICS

**Immediate (During Course):**
- Completion rate: [Target]%
- Engagement indicators: [What you'll track]
- Time-on-task: [Expected range]

**Short-term (1-2 weeks post-course):**
- Application rate: [X]% use at least one tool
- Confidence increase: [Measurement approach]
- Knowledge retention: [Assessment method]

**Long-term (1-3 months post-course):**
- Sustained usage: [X]% still using tools
- Time saved: [Measurable outcomes]
- Attitude shift: [From anxious to confident]

---

## NEXT STEPS

**For Your Review:**
1. Does this syllabus align with your vision?
2. Are the learning objectives appropriate?
3. Is the time allocation reasonable?
4. Any modules to add, remove, or reorder?
5. Any content priorities to emphasize?

**If Approved:**
- I'll save the final syllabus to `docs/course-syllabus.md`
- Create detailed module outlines in `docs/module-outlines/`
- Save research brief to `docs/research-brief.md`
- Generate development plan in `.claude/temp/development_plan.md`

**Then you can run:**
- `/build-module 1` to start developing content
- `/refine-syllabus "your feedback"` if you want to make changes

---

**What would you like to adjust?**
```

Present this to the user and wait for feedback.

---

### Step 6: Iterate Based on Feedback

User might say:
- "Module 2 seems too long, can you split it?"
- "Add a module on [topic]"
- "Move bias discussion earlier"
- "Reduce total time to 40 minutes"

For each request:
1. Acknowledge the feedback
2. Explain how you'll address it
3. Show before/after comparison
4. Re-validate with module-progression-analyzer
5. Present updated proposal

Iterate until user approves.

---

### Step 7: Save Final Syllabus

Once approved, create these files:

#### **1. `docs/course-syllabus.md`**
```markdown
# [Course Title] - Course Syllabus

**Version:** 1.0
**Last Updated:** [Date]
**Total Duration:** [X] minutes

## Course Overview

[Brief description]

## Learning Objectives

1. [Objective 1]
2. [Objective 2]
3. [Objective 3]

## Modules

### Module 1: [Title] ([X] minutes)
**Objectives:** [List]
**Sections:** [List]

### Module 2: [Title] ([X] minutes)
[Same structure]

[Continue for all modules]
```

#### **2. `docs/module-outlines/module_[N]_outline.md`** (one per module)
```markdown
# Module [N]: [Title]

**Duration:** [X] minutes
**Position in Course:** Module [N] of [Total]

## Learning Objectives

- [Objective 1]
- [Objective 2]

## Prerequisites

- [What learner should know from previous modules]

## Content Structure

### Section [N].1: [Title] ([Y] min)
**Purpose:** [What this section achieves]
**Key Concepts:**
- [Concept 1]
- [Concept 2]

**Examples Needed:**
- [Example 1: specific scenario]

**Citations Needed:**
- [Research claim that needs citation]

---

### Section [N].2: [Title] ([Y] min)
[Same structure]

---

## Assessment

**Type:** [Quiz / Scenario / Reflection]
**Timing:** [End of module / Throughout]
**Format:** [Multiple choice / Open-ended / Practical]

## Success Criteria

This module succeeds when learners can:
- [Measurable outcome 1]
- [Measurable outcome 2]

## Development Notes

**Writing guidance:**
- Follow docs/writing-tone.md (Professional-Direct)
- Target audience: [Reminder of who they are]
- Time target: [X] minutes = ~[Y] words at 200-250 wpm

**Research requirements:**
- [Specific topics needing research]
- [Sources to find]

**Customization opportunities:**
- [Where personalization could help]
```

#### **3. `docs/research-brief.md`**
```markdown
# Research Brief - [Course Title]

**Research Date:** [Date]
**Total Sources:** [Count]

## Research Questions

1. [Question 1]
2. [Question 2]

## Key Findings

### [Topic Area 1]

**Finding:** [Summary]
**Source:** [Citation]
**Application:** [How this influenced course design]

### [Topic Area 2]
[Same structure]

## Source List

**Academic Sources:**
1. [Full citation with URL]
2. [Full citation with URL]

**Industry Research:**
3. [Full citation with URL]

**Government/Institutional:**
4. [Full citation with URL]

**Learning Science:**
5. [Full citation with URL]

## Singapore/SEA Context

[Any region-specific findings that influenced design]
```

#### **4. `.claude/temp/development_plan.md`**
```markdown
# Development Plan - [Course Title]

**Total Estimated Time:** [X] hours

## Phase 1: Module 1
- [ ] Research specific topics
- [ ] Draft Section 1.1
- [ ] Draft Section 1.2
- [ ] Add citations
- [ ] Add examples
- [ ] Review & refine
- **Estimated:** [X] hours

## Phase 2: Module 2
[Same structure]

## Phase 3: Quality Review
- [ ] Run /content-review on each module
- [ ] Fix HIGH priority issues
- [ ] Address MEDIUM priority issues
- **Estimated:** [X] hours

## Phase 4: Final Polish
- [ ] Check tone consistency
- [ ] Verify citations
- [ ] Test time estimates
- [ ] Final proofread
- **Estimated:** [X] hours
```

---

## Important Guidelines

### Research Quality
- **Prioritize reputable sources:** Academia, established industry research, government data
- **Avoid:** Personal blogs, forums, unverified content, marketing materials
- **Singapore/SEA focus:** Include when relevant to audience, don't force if global examples stronger
- **Recency:** Prefer recent sources (last 2-3 years) for current topics like AI

### Course Design Principles
- **Learner-first:** Design for actual learner needs, not theoretical best practices
- **Practical:** Focus on application, not just knowledge
- **Realistic:** Time estimates should account for cognitive processing, not just reading
- **Progressive:** Build complexity gradually
- **Coherent:** Each module should advance a clear narrative

### Validation
- **Always run module-progression-analyzer** before presenting proposal
- **Fix structural issues** before user review
- **Iterate based on feedback** until user is satisfied
- **Don't proceed to development** until syllabus is approved

### Communication
- **Be clear about research basis:** Show sources, explain rationale
- **Offer alternatives:** Often multiple valid designs exist
- **Explain trade-offs:** Help user make informed decisions
- **Manage expectations:** Realistic time estimates for development

---

## Example Usage

**Scenario 1: Full description upfront**
```
/design-course "AI literacy for non-technical employees, 50 minutes total, mandatory training, should enable practical use within 1 week"
```
Agent parses requirements and proceeds directly to research.

**Scenario 2: Minimal info, interactive mode**
```
/design-course
```
Agent asks clarifying questions, then researches and designs.

**Scenario 3: After iteration**
```
User: "Module 3 seems too theoretical, make it more applied"
Agent: Revises Module 3 structure, validates with module-progression-analyzer, presents updated version.
```

---

## Success Criteria

This command succeeds when:
- ✅ Comprehensive research conducted (10-15 quality sources)
- ✅ Course structure validated with module-progression-analyzer
- ✅ Learning objectives are specific, measurable, achievable
- ✅ Time allocation is realistic and balanced
- ✅ User approves the proposed syllabus
- ✅ All supporting documents saved correctly

The course is now ready for content development via `/build-module`.
