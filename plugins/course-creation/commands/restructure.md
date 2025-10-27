---
description: Restructure course organization (split/merge/reorder modules)
---

Launch a **general-purpose agent** to modify the course syllabus based on your feedback, validate changes, and update all affected files.

## Prerequisites

Extract the course name from the user's input:
- Example: `/refine-syllabus my-ai-course "Split module 2"` → Course is "my-ai-course"
- If course name missing, ask: "Which course syllabus would you like to refine?"

You should have:
- Existing course syllabus in `courses/{COURSE_NAME}/docs/course-syllabus.md`
- Module outlines in `courses/{COURSE_NAME}/docs/module-outlines/`

## How It Works

The agent will:
1. **Read current syllabus** and module outlines
2. **Parse your feedback** to understand what needs changing
3. **Propose changes** with before/after comparison
4. **Validate with module-progression-analyzer** to ensure coherence
5. **Apply changes** if you approve
6. **Update all affected files** (syllabus, module outlines)

## Task for the Agent

When the user runs `/refine-syllabus [feedback]`, you (the general-purpose agent) should update the course syllabus based on their input.

### Step 1: Read Current Syllabus

Read these files:
- `courses/{COURSE_NAME}/docs/course-syllabus.md` (main syllabus)
- All files in `courses/{COURSE_NAME}/docs/module-outlines/` (module details)
- `courses/{COURSE_NAME}/docs/course-structure.md` (if exists - overall structure notes)

If syllabus doesn't exist, inform user:
```
❌ No syllabus found. Please run /design-course first to create course structure.
```

Extract current structure:
- Module titles, durations, objectives
- Section breakdowns
- Total time allocation
- Learning progression
- Dependencies

---

### Step 2: Parse User Feedback

User feedback can take many forms:

**Examples of feedback types:**

**A. Reordering Modules**
```
"Move Module 3 before Module 2"
"Swap Modules 4 and 5"
"Bias discussion should come earlier"
```

**B. Splitting Modules**
```
"Module 2 is too long, split it into 2A and 2B"
"Break Module 4 into two modules: basics and advanced"
```

**C. Merging Modules**
```
"Modules 5 and 6 overlap, combine them"
"Merge the summary sections"
```

**D. Adjusting Time**
```
"Reduce total time to 40 minutes"
"Module 3 needs more time, maybe 15 minutes instead of 10"
"Make all modules roughly equal length"
```

**E. Adding Content**
```
"Add a module on prompt engineering"
"Include more examples in Module 2"
"Need a section on ethics"
```

**F. Removing Content**
```
"Remove Module 5, it's not essential"
"Cut the AGI discussion"
"Too much theory, reduce conceptual content"
```

**G. Changing Focus**
```
"Module 3 is too theoretical, make it more applied"
"Need more Singapore examples"
"Less history, more practice"
```

**H. Multiple Changes**
```
"Split Module 2, move bias to Module 1, reduce total time to 45 minutes"
```

Parse the feedback to identify:
- What type of change is requested
- Which modules are affected
- What the desired outcome is
- Any constraints mentioned

---

### Step 3: Propose Changes

Create a detailed before/after comparison:

```markdown
## SYLLABUS REFINEMENT PROPOSAL

**Your Feedback:** "[User's original feedback]"

**Changes Proposed:**
[List of specific changes]

---

### BEFORE → AFTER COMPARISON

#### **CURRENT STRUCTURE:**

**Total Duration:** [X] minutes

| Module | Title | Duration | Key Topics |
|--------|-------|----------|------------|
| 1 | [Title] | [X] min | [Topics] |
| 2 | [Title] | [X] min | [Topics] |
| 3 | [Title] | [X] min | [Topics] |
| 4 | [Title] | [X] min | [Topics] |

---

#### **PROPOSED STRUCTURE:**

**Total Duration:** [Y] minutes

| Module | Title | Duration | Key Topics |
|--------|-------|----------|------------|
| 1 | [Title] | [X] min | [Topics] |
| 2 | [New/Modified Title] | [X] min | [Topics] |
| 3 | [New/Modified Title] | [X] min | [Topics] |
| 4 | [Title] | [X] min | [Topics] |
| [5] | [New Module if added] | [X] min | [Topics] |

**Changes Made:**
1. ✏️ [Change 1: e.g., "Split Module 2 into 2A (10 min) and 2B (8 min)"]
   - **Rationale:** [Why this addresses feedback]

2. ✏️ [Change 2: e.g., "Moved bias discussion from Module 3 to Module 2A"]
   - **Rationale:** [Why this makes sense]

3. ✏️ [Change 3: e.g., "Reduced total time from 50 to 45 minutes"]
   - **Rationale:** [How time was redistributed]

---

### DETAILED CHANGES

#### **Module [N]: [Title]**

**BEFORE:**
- Duration: [X] minutes
- Objectives:
  - [Objective 1]
  - [Objective 2]
- Sections:
  - Section [N].1: [Title]
  - Section [N].2: [Title]

**AFTER:**
- Duration: [Y] minutes
- Objectives:
  - [Modified Objective 1]
  - [New Objective 2]
- Sections:
  - Section [N].1: [Modified Title]
  - Section [N].2: [Modified Title]
  - Section [N].3: [New Section]

**Changes:**
- [Specific change 1]
- [Specific change 2]

**Impact:**
- [How this affects learners]
- [How this affects development]

---

[Repeat for each affected module]

---

### TIME ALLOCATION ANALYSIS

**Before:**
| Module | Duration | % of Total |
|--------|----------|------------|
| 1 | [X] min | [Y]% |
| 2 | [X] min | [Y]% |
| 3 | [X] min | [Y]% |
| 4 | [X] min | [Y]% |
| **Total** | **[X] min** | **100%** |

**After:**
| Module | Duration | % of Total |
|--------|----------|------------|
| 1 | [X] min | [Y]% |
| 2A | [X] min | [Y]% |
| 2B | [X] min | [Y]% |
| 3 | [X] min | [Y]% |
| 4 | [X] min | [Y]% |
| **Total** | **[X] min** | **100%** |

**Time Changes:**
- [Description of how time was redistributed]
- [Any modules that grew/shrunk significantly]
```

---

### Step 4: Validate with module-progression-analyzer

Run the `module-progression-analyzer` skill on the proposed new structure.

Check:
- Do modules still flow logically?
- Are there new dependency issues?
- Is time allocation balanced?
- Any gaps or redundancies introduced?
- Does progression pattern still make sense?

If validation finds issues:
```markdown
---

### ⚠️ VALIDATION FINDINGS

Running module-progression-analyzer on proposed structure...

**Flow Quality:** [Excellent/Good/Needs Work/Poor]

**Issues Found:**

1. **[Issue type]** - [Priority: HIGH/MEDIUM/LOW]
   - Problem: [Description]
   - Suggested fix: [How to address]

2. **[Issue type]** - [Priority: HIGH/MEDIUM/LOW]
   - Problem: [Description]
   - Suggested fix: [How to address]

**Recommendations:**
- [Recommendation 1: Additional change needed to fix validation issue]
- [Recommendation 2]

---

### REVISED PROPOSAL

Based on validation findings, I recommend these additional adjustments:

[Modified proposal that addresses validation issues]
```

Keep iterating until validation shows "Good" or "Excellent" flow quality.

---

### Step 5: Present for Approval

```markdown
---

## ✅ PROPOSAL READY FOR YOUR REVIEW

**Summary of Changes:**
1. [Change 1]
2. [Change 2]
3. [Change 3]

**Validation Status:** ✅ Module progression validated - Flow quality: [rating]

**Impact Assessment:**

**Development Impact:**
- Modules with content already written: [List - these need updates]
- New modules requiring content: [List]
- Estimated additional development time: [X hours]

**Learner Impact:**
- [How this improves learning experience]
- [Any trade-offs]

---

**Do you approve these changes?**
- Type "Yes" to apply changes
- Type "Revise [specific feedback]" to adjust proposal
- Type "No" to cancel and keep current syllabus
```

Wait for user response.

---

### Step 6: Apply Changes

If user approves, update all affected files:

#### **A. Update `courses/{COURSE_NAME}/docs/course-syllabus.md`**

Rewrite the syllabus file with:
- New module structure
- Updated time allocations
- Modified objectives
- Add version history:
  ```markdown
  **Version History:**
  - v1.0 ([Date]): Initial syllabus
  - v1.1 ([Date]): [Summary of changes made]
  ```

#### **B. Update Module Outlines**

For each affected module:

**If module was modified:**
- Update `courses/{COURSE_NAME}/docs/module-outlines/module_[N]_outline.md`
- Change title, duration, objectives, sections as needed
- Add note at top:
  ```markdown
  **Last Updated:** [Date]
  **Changes:** [Summary of what changed]
  ```

**If module was split:**
- Create new outline files (e.g., module_2A_outline.md, module_2B_outline.md)
- Distribute content from original module between new modules
- Maintain consistency with original objectives

**If module was merged:**
- Combine into single outline file
- Ensure all content from both modules is preserved
- Update module numbering for subsequent modules

**If module was added:**
- Create new `courses/{COURSE_NAME}/docs/module-outlines/module_[N]_outline.md`
- Populate with structure based on user requirements
- Mark sections needing development:
  ```markdown
  **Development Status:** Not yet written - needs `/build-module [N]`
  ```

**If module was removed:**
- Rename file to `module_[N]_outline_ARCHIVED.md`
- Don't delete (preserve for reference)
- Update subsequent module numbering

#### **C. Update Development Plan** (if exists)

Update `.claude/temp/development_plan.md` to reflect:
- New modules requiring content
- Existing modules needing updates
- Revised time estimates

#### **D. Create Change Log**

Create or append to `courses/{COURSE_NAME}/docs/syllabus-changelog.md`:
```markdown
## [Date] - Version 1.1

**Changes Made:**
- [Change 1]
- [Change 2]
- [Change 3]

**Rationale:**
[User's feedback that prompted changes]

**Validation:**
- Module progression: [rating]
- Flow quality: [rating]

**Impact:**
- Modules affected: [List]
- Content requiring update: [List]

**Developer Notes:**
[Any notes for content development]
```

---

### Step 7: Confirm Completion

```markdown
✅ SYLLABUS REFINEMENT COMPLETE

**Files Updated:**
- ✅ `courses/{COURSE_NAME}/docs/course-syllabus.md` (version 1.1)
- ✅ `courses/{COURSE_NAME}/docs/module-outlines/module_[N]_outline.md` ([count] files)
- ✅ `courses/{COURSE_NAME}/docs/syllabus-changelog.md` (change logged)
- ✅ `.claude/temp/development_plan.md` (development plan updated)

---

**NEW COURSE STRUCTURE:**

| Module | Title | Duration | Status |
|--------|-------|----------|--------|
| 1 | [Title] | [X] min | ✅ Content exists |
| 2 | [Title] | [X] min | ⚠️ Needs update |
| 3 | [Title] | [X] min | ❌ Not yet written |
| 4 | [Title] | [X] min | ✅ Content exists |

**Total Duration:** [X] minutes

---

**NEXT STEPS:**

**For modules needing updates:**
```bash
/build-module 2  # Regenerate with new structure
```

**For new modules:**
```bash
/build-module 3  # Create content from scratch
```

**For existing modules:**
```bash
/content-review module 1  # Verify still aligned with new structure
```

**To further refine:**
```bash
/refine-syllabus "your additional feedback"
```

---

**Summary:** [1-2 sentences describing how the course structure has improved based on your feedback]
```

---

## Handling Edge Cases

### **Multiple Conflicting Changes**
User says: "Reduce time to 40 minutes but add a new module on ethics"

Response:
```markdown
⚠️ I see two conflicting requirements:
1. Reduce total time (requires cutting content)
2. Add new module (requires adding content)

Here are options:

**Option A:** Add ethics module (10 min), reduce other modules proportionally
- Module 1: 15 min → 12 min
- Module 2: 20 min → 16 min
- Module 3: 15 min → 12 min
- New Module: Ethics (10 min)
- **Total: 50 minutes** (exceeds target)

**Option B:** Add ethics module (8 min), remove Module 4 entirely
- Module 1: 15 min
- Module 2: 20 min
- Module 3: 12 min
- New Module: Ethics (8 min)
- **Total: 45 minutes** (within target but loses Module 4 content)

**Option C:** Integrate ethics into existing modules instead of separate module
- Module 1: 15 min (add ethics dimension)
- Module 2: 20 min (add ethics examples)
- Module 3: 15 min
- **Total: 50 minutes** (no time increase)

Which approach do you prefer?
```

---

### **Changes Affect Already-Written Content**
User wants to split Module 2, but Module 2 content already exists.

Response:
```markdown
⚠️ CONTENT IMPACT ALERT

Module 2 content already exists in:
- courses/{COURSE_NAME}/content/2_1_intro.md
- courses/{COURSE_NAME}/content/2_2_ml_concepts.md
- courses/{COURSE_NAME}/content/2_3_speech_example.md
- courses/{COURSE_NAME}/content/2_4_bias.md

**Proposed Split:**
- Module 2A: Sections 2.1, 2.2 (10 min)
- Module 2B: Sections 2.3, 2.4 (12 min)

**Required Actions:**
1. Rename files:
   - courses/{COURSE_NAME}/content/2_1_intro.md → content/2A_1_intro.md
   - courses/{COURSE_NAME}/content/2_2_ml_concepts.md → content/2A_2_ml_concepts.md
   - courses/{COURSE_NAME}/content/2_3_speech_example.md → content/2B_1_speech_example.md
   - courses/{COURSE_NAME}/content/2_4_bias.md → content/2B_2_bias.md

2. Renumber subsequent modules:
   - Module 3 → Module 4
   - Module 4 → Module 5

3. Add bridging content between 2A and 2B
4. Update all cross-references

**Estimated effort:** 2-3 hours

**Do you want to proceed?**
```

---

### **Validation Fails Badly**
Proposed changes create severe dependency issues.

Response:
```markdown
❌ VALIDATION FAILED - SEVERE ISSUES

The proposed changes create these problems:

**HIGH Priority Issues:**
1. **Broken Dependency:** Module 3 now requires concepts from Module 4 (which comes after)
2. **Time Imbalance:** Module 1 is 5 minutes, Module 2 is 35 minutes (severely unbalanced)
3. **Missing Objective:** Course objective "Evaluate AI tools" no longer covered by any module

**I cannot proceed with these changes as-is.**

**Suggested Alternatives:**

**Alternative A:** [Modified proposal that fixes issues]
- [Change 1]
- [Change 2]

**Alternative B:** [Different approach]
- [Change 1]
- [Change 2]

**Alternative C:** Make partial changes only
- Apply changes that don't break structure
- Defer problematic changes for separate refinement

Which would you prefer?
```

---

## Important Guidelines

### Validation is Critical
- **ALWAYS run module-progression-analyzer** before presenting proposal
- **Fix structural issues** before asking user to approve
- **Don't break dependencies** - reorder modules if needed to maintain prerequisites
- **Maintain coherent progression** - ensure changes preserve learning flow

### Communication
- **Show before/after clearly** - make it easy to see what's changing
- **Explain rationale** - why each change makes sense
- **Highlight impacts** - especially on already-written content
- **Offer alternatives** - if conflicts arise, present options

### File Management
- **Update ALL affected files** - syllabus, module outlines, development plan
- **Preserve history** - version numbers, change logs, archived files
- **Don't break references** - update cross-references when renumbering modules

### User Experience
- **Iterative refinement** - user can call this command multiple times
- **Clear status** - show what's written, what needs updates, what's new
- **Actionable next steps** - tell user exactly what commands to run next

---

## Example Usage

**Example 1: Split a module**
```bash
/refine-syllabus "Module 2 is too long, split it into 2A and 2B"
```
Agent proposes split, validates flow, updates all files.

**Example 2: Reorder modules**
```bash
/refine-syllabus "Move bias discussion from Module 3 to Module 2"
```
Agent restructures, validates dependencies still work, applies changes.

**Example 3: Adjust time**
```bash
/refine-syllabus "Reduce total time to 40 minutes"
```
Agent proposes time redistribution across modules, ensures balance maintained.

**Example 4: Multiple changes**
```bash
/refine-syllabus "Split Module 2, reduce total time to 45 minutes, add more examples"
```
Agent handles all changes together, validates combined impact, presents unified proposal.

---

## Success Criteria

This command succeeds when:
- ✅ User feedback accurately parsed and understood
- ✅ Changes proposed with clear before/after comparison
- ✅ Validation performed with module-progression-analyzer
- ✅ Flow quality maintained or improved
- ✅ All affected files updated correctly
- ✅ Change history logged
- ✅ User approves changes
- ✅ Next steps clearly communicated

The syllabus is now refined and ready for continued development.
