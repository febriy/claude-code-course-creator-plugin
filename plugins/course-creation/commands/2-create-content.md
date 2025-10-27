---
description: Write complete module content from your course design
---

Launch a **general-purpose agent** to research, design structure options, and draft all content for a specific module.

## Prerequisites

You should have:
- Completed course syllabus (from `/design-course {COURSE_NAME}`)
- Module outline in `courses/{COURSE_NAME}/docs/module-outlines/module_[N]_outline.md`

## How It Works

The agent will:
1. **Read module outline** to understand requirements
2. **Check style preferences** and remind you about style-extractor skill
3. **Research specific topics** for this module
4. **Generate 2-3 structural options** for you to compare
5. **Draft ONE sample section** for your approval
6. **Iterate on sample** until you're happy with style/tone/depth
7. **Draft all remaining sections** using approved sample as template
8. **Save content files** to `courses/{COURSE_NAME}/content/` directory
9. **Present for final review**

## Task for the Agent

When the user runs `/build-module {COURSE_NAME} [N]`, you (the general-purpose agent) should develop complete content for that module.

**Extract the course name from the user's input:**
- Example: `/build-module my-ai-course 2` → Course name is "my-ai-course", Module number is 2
- If course name missing, ask: "Which course are you building this module for?"

### Step 1: Read Module Outline

Read the module outline file:
- `courses/{COURSE_NAME}/docs/module-outlines/module_[N]_outline.md`

Extract:
- Module title and duration
- Learning objectives
- Section breakdown
- Key concepts to cover
- Examples needed
- Citations needed
- Prerequisites (what learners know from previous modules)

Also read for context:
- `courses/{COURSE_NAME}/docs/course-syllabus.md` (understand where this module fits)
- `courses/{COURSE_NAME}/docs/style-guide.md` (style and tone requirements)
- `courses/{COURSE_NAME}/docs/target-audience.md` (who you're writing for)

If outline file doesn't exist, inform user:
```
❌ Module outline not found. Please run /design-course {COURSE_NAME} first to create course structure.
```

---

### Step 2: Style Selection & Guide Check

Before proceeding, check what style the user wants to follow.

**Present this to the user:**

```markdown
## 📝 STYLE SELECTION

Before building Module [N], let's confirm the writing style to use.

---

### **Option 1: Use Existing Style Guide**

**Check if style guide exists:**
- Looking for: `courses/{COURSE_NAME}/docs/style-guide.md`

**If style guide EXISTS:**
```
✅ Found existing style guide!

**Style Guide Summary:**
- Generated: [Date from guide]
- Based on: [X good examples, Y bad examples]
- Key characteristics: [Brief summary from guide]

**Use this style guide for Module [N]?**
- Type "Yes" to use existing style guide
- Type "Update" to regenerate style guide with new examples
- Type "No" to use a different approach
```

**If style guide DOES NOT exist:**
```
🛑 **PAUSE: No style guide found**

For consistent, high-quality content, you should create a style guide first.

---

## ⚡ **Quick Setup (5 minutes):**

### **Step 1: Add Example Text**
Add 3-10 examples of writing you like:
- Copy text files to: `.claude/skills/style-extractor/examples/good/`
- Can be: previous courses, articles you wrote, documentation you like
- More examples = better style matching

**Don't have examples?** You can:
- Use this course's outline as an example
- Copy text from other courses you admire
- Skip for now and build Module 1 first (use it as example later)

### **Step 2: Run Style Extractor**
In a new message, type:
```
Skill style-extractor
```

This will analyze your examples and create `courses/{COURSE_NAME}/docs/style-guide.md`

### **Step 3: Come Back Here**
After the style guide is created, re-run:
```
/course-creation:build-module {COURSE_NAME} [N]
```

---

## 🎯 **Ready to Continue?**

**Option A: Create Style Guide Now (RECOMMENDED)**
- Type **"pause"** - I'll wait while you add examples and run the skill
- Takes 5 minutes, ensures all modules match your style

**Option B: Skip for Now**
- Type **"skip"** - I'll use default Professional-Direct guidelines
- You can create a style guide later and rebuild

**Option C: Describe Your Style**
- Type **"describe"** - Tell me your preferred style in words
- Less consistent than Option A, but faster

---

**What would you like to do?** (Type: "pause", "skip", or "describe")
```

---

**If user chooses "skip" (no style guide):**
```
✅ **Proceeding with default guidelines**

**Style I'll use:**
- Tone: Professional-Direct (clear, factual, respectful)
- Audience: [From target-audience.md]
- Structure: Standard educational format
- Singapore English spelling

**Note:** You can create a style guide anytime and rebuild modules to match.

**Proceeding to structural options...**
```

---

**If user chooses "describe" (custom verbal description):**
```
📝 **Describe Your Desired Style**

Tell me your style preferences. For example:
- "Short paragraphs, conversational tone, lots of examples"
- "Academic but accessible, with clear definitions"
- "Practical and actionable, minimal theory"

**Your style description:**
[Wait for user input]

---

✅ **Got it! I'll write using:**
[User's description]

**Note:** For consistency across all modules, consider:
1. Let me draft Module [N] using this style
2. If you like it, add Module [N] to `examples/good/`
3. Run `Skill style-extractor` to create reusable guide

**Proceeding to structural options...**
```

---

**Wait for user decision before proceeding.**

**Record style choice:**
- If using style guide: Note path to guide file (`courses/{COURSE_NAME}/docs/style-guide.md`)
- If using default: Note reliance on standard Professional-Direct guidelines
- If using description: Save user's style description

This will be referenced throughout content generation.
```

---

### Step 3: Research Specific Topics

Based on the module outline, conduct targeted research:

#### **A. Content Research**
For each section in the module, search for:
- Detailed explanations of key concepts
- Statistics and data points
- Real-world examples (prioritize Singapore/SEA when relevant)
- Case studies
- Common misconceptions
- Best practices

**Source quality:**
- ✅ Academia, industry research, government data, reputable institutions
- ❌ Blogs, forums, unverified sources

#### **B. Example Research**
Module outline specifies "Examples Needed" - find:
- Concrete, specific scenarios
- Real company examples (verify authenticity)
- Local context (Singapore/SEA) when available
- Relatable to target audience

#### **C. Citation Research**
Module outline specifies "Citations Needed" - find:
- Original sources for research claims
- Full citation details (author, title, year, URL)
- Multiple sources for important claims
- Recent sources (last 2-3 years for current topics)

#### **D. Gap Identification**
If outline is vague or missing details:
- Note what additional research is needed
- Flag any unclear requirements
- Identify potential challenges

---

### Step 3: Generate Structural Options

Before drafting content, create 2-3 alternative structural approaches for the user to compare.

Each option should specify:
- **Teaching approach** (concept-first, example-driven, problem-based, etc.)
- **Content organization** (how sections flow)
- **Example density** (heavy examples vs more theory)
- **Depth level** (introductory vs comprehensive)
- **Pros and cons** of this approach

#### **Example Output:**

```markdown
## STRUCTURAL OPTIONS FOR MODULE [N]

Based on the module outline and research, here are 3 approaches to structure this module:

---

### **Option A: Example-Driven Structure** 📚

**Approach:**
- Start each concept with a concrete workplace scenario
- Build theory from example
- Heavy on real-world applications
- "Show, then explain" pattern

**Organization:**
- Section [N].1: [Title]
  - Open with scenario: [Specific example]
  - Extract concept from example
  - Generalize to broader principle

- Section [N].2: [Title]
  - Another scenario: [Different example]
  - Show pattern across examples
  - Connect to previous section

**Estimated Characteristics:**
- Word count: ~[X] words
- Example:theory ratio: 60:40
- Depth: Intermediate - practical focus
- Tone: Highly concrete, relatable

**Pros:**
✅ Very accessible for non-technical learners
✅ Immediate relevance clear
✅ Easy to remember (stories stick)
✅ Low cognitive load

**Cons:**
❌ May feel repetitive if too many examples
❌ Less comprehensive theoretical grounding
❌ Might miss edge cases

**Best for:** Learners who are skeptical, time-pressured, need immediate applicability

---

### **Option B: Concept-First Structure** 🧠

**Approach:**
- Define concepts clearly upfront
- Build understanding systematically
- Then apply to examples
- "Explain, then show" pattern

**Organization:**
- Section [N].1: [Title]
  - Clear definition of [concept]
  - How it works (mechanism)
  - Then demonstrate with example

- Section [N].2: [Title]
  - Build on [concept] from Section 1
  - Extend to [related concept]
  - Examples at the end

**Estimated Characteristics:**
- Word count: ~[X] words
- Example:theory ratio: 40:60
- Depth: Deeper - stronger foundation
- Tone: More authoritative, structured

**Pros:**
✅ Comprehensive understanding
✅ Strong theoretical foundation
✅ Better for complex topics
✅ Easier to reference later

**Cons:**
❌ Higher cognitive load initially
❌ Relevance not immediately obvious
❌ May lose impatient learners
❌ Needs stronger writing to stay engaging

**Best for:** Learners who want thorough understanding, have time, are analytically minded

---

### **Option C: Hybrid Structure** ⚖️

**Approach:**
- Quick hook example to establish relevance
- Then concept definition
- Multiple examples to demonstrate range
- "Hook → Explain → Show variations" pattern

**Organization:**
- Section [N].1: [Title]
  - Opening hook: Brief scenario (2-3 sentences)
  - "This is [concept]" - definition
  - How it works
  - Extended example demonstrating concept

- Section [N].2: [Title]
  - Reference back to Section 1 concept
  - Introduce [related concept]
  - 2-3 shorter examples showing variations

**Estimated Characteristics:**
- Word count: ~[X] words
- Example:theory ratio: 50:50
- Depth: Balanced - breadth and depth
- Tone: Professional but accessible

**Pros:**
✅ Balances engagement and rigor
✅ Works for diverse learning styles
✅ Maintains interest while building knowledge
✅ Flexible approach

**Cons:**
❌ Less distinctive than A or B
❌ May feel "safe" rather than optimized
❌ Harder to execute well (requires balance)

**Best for:** Mixed audience, standard corporate training, when unsure of learner preferences

---

## RECOMMENDATION

Based on your target audience ([describe audience]), I recommend **Option [A/B/C]** because:
- [Rationale 1]
- [Rationale 2]

However, [other option] would work if [condition].

**Which structure would you like me to use?**
- Type "A" for Example-Driven
- Type "B" for Concept-First
- Type "C" for Hybrid
- Or describe your own preferred approach
```

Wait for user selection before proceeding.

---

### Step 4: Create Sample Section for Approval

**IMPORTANT:** Before drafting the entire module, create ONE sample section to get user feedback on style and approach.

**Why this matters:**
- Ensures style matches user's expectations
- Allows early course correction before investing time in full module
- User can give feedback on tone, depth, examples before you write all sections
- Prevents need to rewrite entire module if style is off

---

#### **A. Select Sample Section**

Choose the **first substantive section** (usually Section [N].1 or [N].2) as the sample.

**Present to user:**
```markdown
## 📄 SAMPLE SECTION DRAFT

Before building the full module, I'll draft **Section [N].[X]: [Title]** as a sample for your review.

**This section will demonstrate:**
- The [chosen structure] approach
- Tone and voice from [style guide/default/your description]
- Example style and depth
- Formatting and structure

**Section Details:**
- Topic: [What this section covers]
- Target length: [X] words (~[Y] minutes)
- Key concepts: [List]

**Drafting sample section now...**
```

---

#### **B. Draft the Sample Section**

Write the complete sample section following:
- Chosen structural approach (A/B/C)
- Selected style guide or tone guide
- Module outline requirements
- All writing guidelines from Step 5 below

**Complete draft with:**
- Full content (not abbreviated)
- Citations [numbered or placeholders]
- Examples (concrete and specific)
- Proper formatting (headers, paragraphs, lists)
- Singapore English spelling

---

#### **C. Present Sample for Feedback**

```markdown
## ✅ SAMPLE SECTION COMPLETE

### Section [N].[X]: [Title]

[FULL CONTENT OF SAMPLE SECTION]

---

**References**

[1] [Citation]
[2] [Citation]

---

## 📊 SAMPLE CHARACTERISTICS

**Word Count:** [X] words (~[Y] min reading time)
**Structure:** [Description of how it's organized]
**Tone:** [Tone assessment]
**Examples:** [X] concrete examples included
**Citations:** [X] sources cited

---

## 🔍 REVIEW QUESTIONS

Please review this sample section and provide feedback:

**1. Style & Tone:**
- Does this match your desired style?
- Is the tone appropriate (not too casual/formal/technical)?
- Any phrases or language that feel off?

**2. Structure & Flow:**
- Does the organization make sense?
- Are transitions smooth?
- Is it easy to follow?

**3. Depth & Detail:**
- Right level of detail, or too shallow/deep?
- Examples helpful and relevant?
- Explanations clear?

**4. Formatting:**
- Paragraphs right length?
- Headers helpful?
- Good use of bold/lists?

**5. Overall:**
- Would you be happy if all sections looked like this?
- Any specific changes needed?

---

## 🎯 NEXT STEPS

**Option A: Approve**
```
Type "Approve" - I'll proceed to draft all remaining sections in this style
```

**Option B: Revise Sample**
```
Tell me what to change:
- "Make it less formal"
- "Add more examples"
- "Simplify the technical explanations"
- "Use shorter paragraphs"
- etc.

I'll revise this section and show you again.
```

**Option C: Try Different Structure**
```
Type "Try Option B" (or A/C) - I'll rewrite this section using a different structural approach
```

**Option D: Update Style**
```
Type "Update style guide" - Pause to update style guide, then regenerate sample
```

---

**What would you like to do?**
```

Wait for user feedback before proceeding.

---

#### **D. Iterate on Sample if Needed**

If user requests changes:
1. **Parse feedback** - Understand what needs changing
2. **Revise sample section** - Apply changes
3. **Present revised version** - Show updated sample
4. **Ask for approval again** - Repeat until user approves

**Track changes:**
- Note what was adjusted (tone, depth, examples, structure)
- Apply same adjustments to remaining sections
- Use approved sample as the template for consistency

**Only proceed to Step 5 after user approves the sample section.**

---

### Step 5: Draft All Remaining Sections

Once user approves the sample section, draft ALL remaining sections for the module.

#### **Writing Guidelines:**

**A. Follow Style Guide**
- Read and strictly follow `courses/{COURSE_NAME}/docs/style-guide.md`
- Professional-Direct tone (not casual, not condescending)
- Clear, factual, respectful of learner intelligence
- No excessive enthusiasm or motivational language

**B. Structure Each Section**
Standard section format:
```markdown
Module [N]: [Module Title]
Section [N].[X]: [Section Title] ([Y] minutes)

[Opening paragraph - establish relevance/context]

## [Main Header 1]

[Content paragraph]

[Content paragraph]

## [Main Header 2]

[Content paragraph]

**[Bold subpoint if needed]** [Explanation]

[Example or scenario]

## [Main Header 3]

[Content paragraph]

[Continue section]
```

**C. Add Citations**
- Use numbered in-text citations: [1], [2], [3]
- Add references section at bottom of each section file
- Format:
  ```markdown
  ---

  **References**

  [1] Source Name, "Article Title", Year. https://url
  [2] Source Name, "Article Title", Year. https://url
  ```
- If research incomplete, use placeholder:
  ```markdown
  [RESEARCH NEEDED: Citation for claim about X]
  ```

**D. Include Examples**
- Concrete, specific scenarios (not vague)
- Relevant to target audience
- Singapore/SEA context when available
- Numbers and details (builds credibility)

**E. Time Estimate**
- Section header should show estimated reading time
- Based on word count: 200-250 words/minute
- Account for cognitive processing (+15-20%)

**F. No Customization Markers**
- DO NOT add customization markers automatically
- User will add them manually later
- Just write standard content

**G. Word Count Target**
- Module outline specifies total duration
- Work backward: [Duration in min] × 225 words/min = target word count
- Distribute across sections proportionally

---

#### **Section File Naming:**

Save each section as:
```
courses/{COURSE_NAME}/content/[MODULE]_[SECTION]_[description].md
```

Examples (for course "my-ai-course"):
- `courses/my-ai-course/content/4_1_intro.md`
- `courses/my-ai-course/content/4_2_prompt_basics.md`
- `courses/my-ai-course/content/4_3_use_cases.md`

---

### Step 5: Quality Self-Check

Before presenting to user, verify:

**Tone Compliance:**
- ✅ Professional-Direct throughout
- ✅ No casual language ("basically", "pretty much", "let's dive in")
- ✅ No condescension ("don't worry", "even you can")
- ✅ No excessive enthusiasm ("amazing!", "revolutionary!")

**Structure:**
- ✅ Logical flow within each section
- ✅ Sections build on each other
- ✅ Smooth transitions between sections
- ✅ Clear headers and formatting

**Citations:**
- ✅ All research claims cited
- ✅ Citations properly formatted
- ✅ References section at bottom of each file

**Examples:**
- ✅ Concrete and specific
- ✅ Relevant to audience
- ✅ Multiple examples where appropriate

**Time:**
- ✅ Total word count matches duration target ±10%
- ✅ Sections are balanced (no one section 2x another without reason)

**Singapore English:**
- ✅ British spelling (organise, recognise, analyse)
- ✅ Consistent throughout

---

### Step 6: Present to User

Show summary of what was created:

```markdown
✅ MODULE [N] DRAFT COMPLETE

**Module:** [Title]
**Target Duration:** [X] minutes
**Structure Used:** [Option A/B/C]
**Total Word Count:** [Y] words (≈ [Z] min reading time)

---

## FILES CREATED

1. `courses/{COURSE_NAME}/content/[N]_1_[description].md` ([W] words, ≈ [T] min)
   - [Brief summary of what this section covers]

2. `courses/{COURSE_NAME}/content/[N]_2_[description].md` ([W] words, ≈ [T] min)
   - [Brief summary]

3. `courses/{COURSE_NAME}/content/[N]_3_[description].md` ([W] words, ≈ [T] min)
   - [Brief summary]

[List all sections]

---

## CONTENT SUMMARY

**Key Concepts Covered:**
- [Concept 1]
- [Concept 2]
- [Concept 3]

**Examples Included:**
- [Example 1: brief description]
- [Example 2: brief description]

**Citations Added:** [Count] references

**Research Placeholders:** [Count] items marked [RESEARCH NEEDED]

---

## QUALITY CHECK

✅ Tone: Professional-Direct throughout
✅ Structure: Logical flow, smooth transitions
✅ Citations: [X] claims cited, [Y] need research
✅ Examples: [X] concrete scenarios included
✅ Time: Target [A] min, Actual [B] min (within range)
✅ Singapore English: Verified

---

## NEXT STEPS

**Option 1: Approve and Continue**
- Files are saved and ready for review
- Run `/content-review {COURSE_NAME}` to check quality
- Proceed to next module with `/build-module {COURSE_NAME} [N+1]`

**Option 2: Edit Specific Sections**
- Tell me which section needs changes and what to adjust
- I can regenerate individual sections

**Option 3: Try Different Structure**
- Regenerate entire module with different structural option
- Useful if you want to compare outcomes

**What would you like to do?**
```

Wait for user feedback.

---

### Step 7: Handle Feedback

User might say:

**"Looks good, approved"**
→ Confirm files saved, suggest next steps

**"Section [X] is too technical, simplify it"**
→ Regenerate that specific section with simpler language

**"Add more examples to Section [Y]"**
→ Research additional examples, update that section

**"This doesn't match the style guide"**
→ Review style guide again, revise problematic sections

**"Too long, reduce by 200 words"**
→ Identify least critical content, trim while preserving key points

**"Regenerate with Option B instead"**
→ Start over using different structural approach

Handle iteratively until user is satisfied.

---

## Important Guidelines

### Research Quality
- **Specific to module:** Don't reuse generic research, dive deep into module topics
- **Verify claims:** Check statistics and facts against original sources
- **Local context:** Include Singapore/SEA examples when available and relevant
- **Recency:** Prefer recent sources for current topics

### Writing Quality
- **Consistency:** All sections should feel like they're from the same course
- **Progressive:** Each section should build on previous
- **Concrete:** Prefer specific examples over abstract explanations
- **Accessible:** Non-technical audience, avoid jargon or define it

### Structure
- **Coherent:** Module should have clear narrative arc
- **Balanced:** Sections should be roughly similar length unless there's a reason
- **Practical:** Focus on application, not just theory
- **Scannable:** Use headers, bold text, lists to aid scanning

### Citations
- **Comprehensive:** Cite all research claims, statistics, studies
- **Proper format:** [Number] in text, full citation in References section
- **Traceable:** Include URLs where possible
- **Honest:** Use [RESEARCH NEEDED] if source not yet found

### User Experience
- **Give options:** Present structural choices before committing
- **Show work:** Explain what you included and why
- **Enable iteration:** Easy to revise specific sections
- **Quality gates:** Self-check before presenting

---

## Example Usage

**Standard usage:**
```bash
/build-module my-ai-course 2
```
Agent reads Module 2 outline for "my-ai-course", researches, presents 3 structural options, user selects, agent drafts all sections.

**After feedback:**
```
User: "Section 2.3 is too long, reduce by 150 words"
Agent: Trims Section 2.3 while preserving key concepts, presents updated version.
```

**Trying different structure:**
```
User: "Actually, let's try Option A instead of Option C"
Agent: Regenerates all sections using Example-Driven structure.
```

---

## Success Criteria

This command succeeds when:
- ✅ All sections drafted and saved to `courses/{COURSE_NAME}/content/` directory
- ✅ Content follows tone guide and structure patterns
- ✅ Citations added (or [RESEARCH NEEDED] placeholders)
- ✅ Word count matches duration target ±10%
- ✅ Singapore English spelling throughout
- ✅ User approves the content
- ✅ Module ready for quality review via `/content-review {COURSE_NAME}`

The module is now ready for review and refinement.
