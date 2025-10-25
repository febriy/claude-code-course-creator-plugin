---
description: Detailed page-by-page, line-by-line editing with duplicate detection first
---

Use the **editor-agent** subagent to perform detailed editing of content.

This is the most thorough editing mode - the subagent will use all available skills to comprehensively improve content quality.

## Prerequisites

Extract the course name from the user's input:
- Example: `/edit-detailed my-ai-course module 2` → Course is "my-ai-course"
- If course name missing, ask: "Which course would you like to edit?"

## Scope Handling

First, determine the scope:
- **Single file**: If a file path is provided (e.g., `courses/{COURSE_NAME}/content/2_3_what_is_ai_section_3.md`)
- **Module**: If "module X" is specified (e.g., "module 2" means all files matching `courses/{COURSE_NAME}/content/2_*.md`)
- **Multiple modules**: If "module X Y" is specified (e.g., "module 3 4")

## STEP 1: Check for Style Guide

**Before any editing, check if a style guide exists:**

Look for: `courses/{COURSE_NAME}/docs/style-guide.md`

**If style guide EXISTS:**
1. Read it thoroughly
2. Extract key tone patterns, vocabulary preferences, and structural guidelines
3. Use the style guide as the PRIMARY reference for all editing decisions
4. All edits must align with the documented style patterns

**If style guide DOES NOT exist:**
1. Proceed with default editor standards from skills
2. **Recommend to user:** Consider running `Skill style-extractor` to create a style guide from your best existing content

---

## STEP 2: Duplicate Detection (if multiple files)

**If scope includes 2+ files:**

1. Use `duplicate-content-detector` skill to scan all files
2. Present findings:
   - List of duplicates (exact, semantic, redundant explanations)
   - Restructuring recommendations (what to keep, what to reference)
   - Priority order for fixes
3. **WAIT FOR USER APPROVAL** on how to handle duplicates
4. Fix approved duplicates BEFORE proceeding to detailed editing

**Rationale:** No point editing content that will be removed/merged.

---

## STEP 3: Detailed Editing (for each file)

The editor-agent subagent will perform comprehensive editing using all available skills:

- **page-structure-analyzer** - Evaluate overall structure, recommend reorganization if needed
- **paragraph-flow-analyzer** - Analyze paragraph flow, suggest reordering and transitions
- **sentence-clarity-checker** - Fix tone, clarity, complexity, and spelling issues line-by-line
- **citation-formatter** - Format citations and flag uncited claims

The subagent will:
1. Analyze using each skill
2. Make comprehensive edits across all dimensions
3. Present edited version with detailed change log
4. Wait for your approval before saving

---

## STEP 4: Present Edited Version

For each file, present:

```markdown
# EDITED FILE: [filename]

## CHANGES MADE

### Structure Changes
- [What was reorganized and why]

### Paragraph Changes
- [What was reordered/split/merged]
- [Transitions added]

### Sentence Changes (line-by-line)
- Line X: [Original] → [Edited] (Reason: [tone/clarity/spelling])
- Line Y: [Original] → [Edited] (Reason: [tone/clarity/spelling])
- [Continue for all changes...]

### Citation Changes
- [Citations formatted]
- [Uncited claims flagged]

---

## EDITED CONTENT

[Full edited file content here]

---

## QUALITY SCORES (After Editing)
- Page Structure: X/20 (was Y/20)
- Paragraph Flow: [Excellent/Good] (was [rating])
- Sentence Clarity: X/10 (was Y/10)
- Citations: X/10 (was Y/10)

---

⚠️ APPROVAL REQUIRED

Please review the edited version above.

Options:
1. ✅ **Approve & Save** - Save the edited version to `courses/{COURSE_NAME}/content/[filename]`
2. 🔄 **Request Changes** - Tell me what to adjust
3. ❌ **Reject** - Keep original, no changes
4. ⏭️ **Skip** - Move to next file (if multi-file edit)

What would you like to do?
```

**WAIT FOR USER RESPONSE** before saving or moving to next file.

---

## Important Notes

- **Module 2 Protection**: Be extra careful with citations in Module 2 - only reformat, never change content
- **Customization Markers**: Don't edit content inside `<!-- CUSTOM:... -->` markers
- **Educational Approach**: Explain WHY each change improves the content
- **Incremental Approval**: User approves each file individually
- **Backup Exists**: Original V1 is safe in `content_v1_backup/`

---

**Usage examples:**
- `/edit-detailed my-ai-course courses/my-ai-course/content/2_3_what_is_ai_section_3.md` → Edit one file thoroughly
- `/edit-detailed my-ai-course module 2` → Edit all Module 2 files (with duplicate check)
- `/edit-detailed my-ai-course module 3 4` → Edit Modules 3 & 4 (duplicate check across both)
