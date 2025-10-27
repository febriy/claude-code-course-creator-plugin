---
description: Edit course content based on your comments or review reports
---

# Unified Content Editing Workflow

Edit course content in two ways:
1. **Your inline comments** - Add comments to files showing what needs to change
2. **Review report fixes** - Automatically fix issues from `/content-review` reports

## How to Use

### Mode 1: Edit Based on Your Comments (Default)
```bash
/edit my-ai-course courses/my-ai-course/content/3_1_ai_in_workplace.md
```
Provide a file with your comments, and I'll extract them, log them for learning, and make the edits.

### Mode 2: Fix Issues from Review Report
```bash
/edit my-ai-course --from-review
```
Automatically fix HIGH priority issues identified in the most recent `/content-review` report.

### Mode 3: Both!
```bash
/edit my-ai-course courses/my-ai-course/content/3_1_ai_in_workplace.md --from-review
```
Fix both your comments AND issues from the review report.

---

## Comment Formats Supported

You can use any of these formats for your comments:

### 1. HTML Comments (Recommended)
```markdown
This is some content.
<!-- EDIT: Make this more concise -->

Another paragraph here.
<!-- FIX: This tone is too casual -->
```

### 2. Inline Brackets
```markdown
This is some content. [EDIT: Make this more concise]

Another paragraph here. [FIX: This tone is too casual]
```

### 3. Comment Blocks at Top
```markdown
<!--
EDITS NEEDED:
- Line 15: Make more concise
- Line 23: Tone too casual
- Line 45: Add citation
-->

[Rest of content...]
```

**Note:** Any format that clearly marks your feedback works - I'll extract them all!

---

## Step-by-Step Workflow

### STEP 0: Determine Edit Mode

**Check for `--from-review` flag:**
- If present → MODE 2 or MODE 3 (include review report fixes)
- If absent → MODE 1 (only your comments)

### STEP 1: Extract Course Name
- Parse course name from the file path or command
- Example: `courses/my-ai-course/content/...` → Course is "my-ai-course"
- If missing, ask user for course name

### STEP 2A: Read Your Comments (MODE 1 or 3)
**If file path provided:**
- Read the provided file completely
- Extract ALL comments/feedback using pattern matching
- Identify which lines/sections each comment refers to

### STEP 2B: Read Review Report (MODE 2 or 3)
**If `--from-review` flag present:**

1. **Locate the review report:**
   - Look for most recent: `.claude/temp/{COURSE_NAME}_*review_report.md`
   - Sort by modification time, use newest
   - If not found, tell user: "No review report found. Run `/content-review` first."

2. **Parse HIGH priority issues from report:**
   - Extract which files need fixes
   - Identify specific issues per file
   - Group by file for parallel editing

3. **Show what will be fixed:**
   ```
   📋 HIGH Priority Issues from Review Report:

   File: courses/{COURSE}/content/2_3_speech.md
   - Add numbered citations (5 claims)
   - Fix Singapore English spelling (3 errors)
   - Update time estimate

   File: courses/{COURSE}/content/2_4_bias.md
   - Add numbered citations (7 claims)
   - Fix Singapore English spelling (5 errors)
   - Add section headers
   ```

### STEP 2C: Combine Feedback Sources (MODE 3)
**If both comments AND review report:**
- Merge your comments with review report issues
- Prioritize your comments (you know best!)
- Add review issues as supplementary fixes

### STEP 3: Load Comment History & Style Guide
**This is where I LEARN from past edits!**

1. **Read comment log** (if exists): `courses/{COURSE_NAME}/.edit-history/comments-log.jsonl`
   - This shows me your past editing preferences
   - I'll understand patterns in what you typically ask for

2. **Read style guide** (if exists): `courses/{COURSE_NAME}/docs/style-guide.md`
   - This is the formal documented style

3. **Synthesize understanding**: Combine both sources to understand:
   - Your tone preferences (from comment history)
   - Your common pain points (from comment patterns)
   - Your structural preferences (from past feedback)
   - Any recurring issues I should watch for

**If comment log exists**, I'll show you:
```
📊 Learning from your past {N} edit comments:
- Common requests: [Most frequent edit types]
- Tone preferences: [Patterns I've noticed]
- Recurring issues: [Things you often flag]
```

### STEP 4: Save All Feedback to Log
**This builds my learning dataset!**

Append to: `courses/{COURSE_NAME}/.edit-history/comments-log.jsonl`

Each entry includes:
- Your manual comments (if MODE 1 or 3)
- Review report issues being fixed (if MODE 2 or 3)
- Source of feedback (manual vs automated)

```json
{
  "timestamp": "2025-10-27T16:45:00Z",
  "file": "courses/my-ai-course/content/3_1_ai_in_workplace.md",
  "mode": "manual",
  "comments": [
    {
      "line": 15,
      "comment": "Make this more concise",
      "context": "This is some content that needs to be more concise and clear.",
      "type": "clarity",
      "source": "manual"
    },
    {
      "line": 23,
      "comment": "This tone is too casual",
      "context": "Hey there! Let's talk about AI.",
      "type": "tone",
      "source": "manual"
    }
  ]
}
```

**For review report fixes:**
```json
{
  "timestamp": "2025-10-27T17:00:00Z",
  "files": ["content/2_3_speech.md", "content/2_4_bias.md"],
  "mode": "from-review",
  "review_report": ".claude/temp/my-ai-course_module_2_review_report.md",
  "issues_fixed": [
    {
      "file": "content/2_3_speech.md",
      "type": "citations",
      "count": 5,
      "source": "review-report"
    },
    {
      "file": "content/2_3_speech.md",
      "type": "spelling",
      "count": 3,
      "source": "review-report"
    }
  ]
}
```

**Why JSONL format?**
- Each line is a separate JSON object (one edit session = one line)
- Easy to append new sessions without parsing entire file
- Easy to analyze patterns across all sessions
- Can grow indefinitely without performance issues

### STEP 5: Present Edit Plan
Show the user:

```markdown
# EDIT PLAN FOR: {filename}

## Comments Found ({N} total):

### 1. Line {X}: {Comment text}
**Context:** "{surrounding text}"
**Type:** {tone/clarity/structure/citations/flow}
**My understanding:** {What I plan to change and why}

### 2. Line {Y}: {Comment text}
**Context:** "{surrounding text}"
**Type:** {tone/clarity/structure/citations/flow}
**My understanding:** {What I plan to change and why}

[...continue for all comments...]

---

## Learning Insights (from past {N} comments):
- You often ask for: {common patterns}
- You prefer: {style preferences I've noticed}
- I'll be extra careful with: {recurring pain points}

---

## Editing Approach:
I will use the **editor-agent** to:
1. {First priority based on comments}
2. {Second priority}
3. {Third priority}

⚠️ Does this plan match your intent? Please confirm before I proceed.
```

**WAIT FOR USER APPROVAL** before proceeding.

### STEP 6: Execute Edits Using editor-agent

Once approved, use the **editor-agent** subagent to make edits:

1. Pass the file and ALL extracted comments to editor-agent
2. Editor-agent will:
   - Use appropriate skills based on comment types
   - Make comprehensive edits addressing all feedback
   - Apply learnings from comment history
   - Present edited version with detailed changelog

3. The editor-agent will show:
   - Before/after for each change
   - Why each change was made
   - Reference to which comment it addresses

### STEP 7: Present Edited Version

```markdown
# EDITED VERSION: {filename}

## Changes Made ({N} total)

### Addressing Your Comments:

**Comment 1 (Line {X}): "{original comment}"**
- **Original:** {original text}
- **Edited:** {new text}
- **Rationale:** {why this change addresses your feedback}

**Comment 2 (Line {Y}): "{original comment}"**
- **Original:** {original text}
- **Edited:** {new text}
- **Rationale:** {why this change addresses your feedback}

[...continue for all comments...]

---

## Additional Improvements Made:
[Any edits made to maintain consistency or quality beyond your specific comments]

---

## EDITED CONTENT

```markdown
{Full edited file content}
```

---

⚠️ APPROVAL REQUIRED

Please review the edited version above.

Options:
1. ✅ **Approve & Save** - Save edited version and update comment log
2. 🔄 **Request Changes** - Add more comments or clarify
3. ❌ **Reject** - Keep original, but still save comments to log for learning
4. 💾 **Save Comments Only** - Don't edit yet, but log my feedback for future reference

What would you like to do?
```

**WAIT FOR USER RESPONSE** before saving.

### STEP 8: Save and Update
When user approves:
1. ✅ Save edited file to original location
2. ✅ Update comment log with resolution status
3. ✅ Show confirmation with path

---

## Special Features

### 🧠 Learning from Comment History
Every time you run `/edit`, I get smarter by:
- **Analyzing past comments** to understand your preferences
- **Identifying patterns** in what you typically request
- **Anticipating issues** you commonly flag
- **Improving the style guide** based on your feedback

### 📊 Comment Analytics (Optional)
At any time, you can ask me to analyze your comment history:
- "What do I usually ask for in edits?"
- "What are my most common edits?"
- "Update the style guide based on my edit history"

I can read `courses/{COURSE_NAME}/.edit-history/comments-log.jsonl` and show patterns.

### 🎯 Iterative Editing
You can run `/edit` multiple times:
1. First pass: Address major issues
2. Second pass: Fine-tune remaining items
3. Each session adds to the learning history

---

## Important Notes

### Module 2 Protection
- Module 2 has extensive research citations
- ONLY reformat citations, NEVER change content
- Flag any citation issues for your review

### Customization Markers
- Don't edit content inside `<!-- CUSTOM:... -->` markers
- These are protected personalization zones

### Backup Safety
- Original V1 content is safe in `content_v1_backup/`
- Each edit creates a timestamped backup

### File Organization
```
courses/
  my-ai-course/
    content/              # Your course content files
    docs/                 # Style guides, audience profiles
    .edit-history/        # LEARNING HISTORY (new!)
      comments-log.jsonl  # All your past comments
      backups/            # Timestamped backups before each edit
```

---

## Examples

### Example 1: Single file with HTML comments
```bash
/edit my-ai-course courses/my-ai-course/content/3_1_intro.md
```

The file contains:
```markdown
# Introduction to AI

AI is a thing that does stuff. <!-- EDIT: Too vague, be specific -->

It's super cool! <!-- FIX: Tone too casual -->
```

I will:
1. Extract 2 comments
2. Log them to `.edit-history/comments-log.jsonl`
3. Show you my edit plan
4. Execute edits after approval
5. Learn from these comments for next time

### Example 2: Fix issues from review report
```bash
/review my-ai-course module 2
# Review report generated with HIGH priority issues

/edit my-ai-course --from-review
# Automatically fixes all HIGH priority issues from report
```

Files fixed:
- Added numbered citations (12 total)
- Fixed Singapore English spelling (8 errors)
- Updated time estimates (3 files)

### Example 3: Combine both approaches
```bash
# Add your own comments to a file
/edit my-ai-course courses/my-ai-course/content/3_1_intro.md --from-review
```

This will:
1. Extract YOUR comments from the file
2. Pull HIGH priority issues from review report for that file
3. Fix both in one pass!

### Example 4: Multiple edits building knowledge
**First edit:**
```bash
/edit my-ai-course courses/my-ai-course/content/module1/intro.md
```
Comments: "Too casual", "Add citation", "Make concise"

**Second edit (days later):**
```bash
/edit my-ai-course courses/my-ai-course/content/module2/section1.md
```
Now I know from history that you:
- Prefer formal tone
- Want citations for claims
- Value conciseness

I'll proactively address these even if not explicitly commented!

---

## Benefits of This Approach

✅ **One unified command** - Handles manual comments AND automated review fixes
✅ **Three modes** - Your comments, review reports, or both combined
✅ **Your feedback drives it** - You show me exactly what to change
✅ **I learn over time** - Each edit makes me smarter about your preferences
✅ **Full transparency** - You see the plan before I execute
✅ **Audit trail** - Complete history of all feedback and changes
✅ **Iterative improvement** - Style guide evolves based on real feedback
✅ **Replaces old /fix command** - No need for separate fix-from-review command

---

## Getting Started

1. **Add comments to your file** using any format (HTML comments recommended)
2. **Run the command**: `/edit {course-name} {file-path}`
3. **Review the plan** I present
4. **Approve edits** and I'll execute them
5. **Repeat** - I get better each time!

Your comments become my training data for improving the style guide and editing process. 🎓
