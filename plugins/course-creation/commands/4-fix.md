---
description: Fix issues identified in content-review report by launching parallel editor-agents
---

Launch multiple **editor-agent** instances in parallel to fix issues identified in a content review report.

## Prerequisites

You must have recently run `/content-review` which generated a report. This command reads that report and fixes the issues.

## How It Works

1. **Reads the review report** - Identifies all HIGH priority issues
2. **Groups issues by file** - Organizes what needs fixing in each file
3. **Launches parallel editor-agents** - One agent per file, all running simultaneously
4. **Applies fixes** - Each agent fixes its assigned issues
5. **Reports results** - Summary of all changes made

## What Gets Fixed

**HIGH Priority issues only:**
- Citation formatting (adding numbered citations [1], [2], etc.)
- Singapore English spelling corrections (recognize→recognise, analyze→analyse)
- Time estimate updates
- Critical structural issues
- Duplicate content removal

**MEDIUM/LOW Priority issues:**
- Not fixed automatically (require more judgment/context)
- You can run `/edit-detailed` separately for these

## Task for You (Main Claude)

When the user runs `/fix-from-review`, you should:

### Step 1: Locate the Review Report

**Option A: User specifies report path**
```
/fix-from-review .claude/temp/module_2_content_review_report.md
```

**Option B: Auto-detect most recent report**
```
/fix-from-review
```
Look for the most recent file matching:
- `.claude/temp/*review_report.md`
- `.claude/temp/module_*_content_review_report.md`

Sort by modification time, use the newest.

**Option C: Ask user which report**
If multiple reports exist and no path specified, show list:
```
Found multiple review reports:
1. module_2_content_review_report.md (Oct 23, 4:58 PM)
2. module_3_content_review_report.md (Oct 22, 2:30 PM)

Which report should I use to fix issues?
```

If no report found, tell user: "No review report found. Run `/content-review [scope]` first to generate a report."

### Step 2: Parse HIGH Priority Issues

Extract from the report:
- Which files need fixes
- What specific issues per file
- Line numbers if available

Example parsing:
```
Section 3 (content/2_3_speech_to_text.md):
- Add numbered citations [1-5] to research claims
- Correct 3 Singapore English spelling errors
- Update time estimate from 2 min to 4 min
- Shorten bias explanation (lines 65-73)

Section 4 (content/2_4_understanding_bias.md):
- Add numbered citations [1-7] to research claims
- Correct 5 Singapore English spelling errors
- Add section headers for topic shifts (lines 37, 53)
```

### Step 3: Check for Style Guide

**Before launching editor-agents, check if a style guide exists:**

Look for: `docs/style-guide.md`

**If style guide EXISTS:**
- Include instruction to read and follow the style guide in ALL agent prompts
- Agents should align all fixes with documented style patterns

**If style guide DOES NOT exist:**
- Agents will use default Professional-Direct tone guidelines
- Consider recommending user run `Skill style-extractor` after fixes complete

---

### Step 4: Launch Parallel Editor-Agents

**IMPORTANT:** Launch ALL agents in a SINGLE message using multiple Task tool calls.

For each file with HIGH priority issues, launch one editor-agent:

```
Task tool with subagent_type=editor-agent, prompt:

"You are fixing HIGH priority issues in [filename] identified during content review.

**FILE:** [full file path]

**ISSUES TO FIX:**
1. [Issue 1 with specific instructions]
2. [Issue 2 with specific instructions]
3. [Issue 3 with specific instructions]

**IMPORTANT INSTRUCTIONS:**

- This is EDIT MODE - make actual file changes using Edit tool
- Fix ONLY the issues listed above
- **STYLE GUIDE:** Read docs/style-guide.md if it exists and ensure all fixes align with documented style patterns
- Follow Professional-Direct tone (clear, factual, respectful)
- Use Singapore English spelling throughout
- Preserve all existing content structure unless specifically instructed
- For citation fixes:
  - Add numbered in-text citations [1], [2], etc.
  - Format references at bottom as:
    ---
    **References**
    [1] Source, "Title", Year. URL
    [2] Source, "Title", Year. URL

**VERIFICATION:**
After making changes, report:
1. What you fixed
2. How many edits you made
3. Any issues you couldn't fix (with reasons)

Begin fixing now."
```

### Step 5: Collect Results

After all agents complete, synthesize their reports into a summary:

```
✅ FIX-FROM-REVIEW COMPLETE

FILES MODIFIED: [count]

---

📝 CHANGES MADE:

**[filename]:**
- ✅ Added numbered citations (5 citations)
- ✅ Corrected Singapore English spelling (3 changes)
- ✅ Updated time estimate
- ⚠️ Could not shorten bias explanation (needs human judgment)

**[filename]:**
- ✅ Added numbered citations (7 citations)
- ✅ Corrected Singapore English spelling (5 changes)
- ✅ Added section headers

---

⏱️ TIME SAVED: [estimate based on manual effort]

---

⚠️ REMAINING ISSUES (require manual review):

**MEDIUM Priority:**
- [File]: [Issue requiring judgment]
- [File]: [Issue requiring judgment]

**Recommendation:** Run `/edit-detailed [file]` for these items.

---

🎯 NEXT STEPS:
1. Review the changes made (use git diff if in a repo)
2. Test/verify the content still reads well
3. Address remaining MEDIUM priority issues if needed
```

## Safety Guardrails

**⚠️ LARGE CHANGE ALERT:** Multiple files will be edited simultaneously.

Before launching agents:
1. **Show the user which files will be modified**
2. **Show how many edits per file (approximate)**
3. **Ask for confirmation if editing >3 files**

Example:
```
⚠️ About to launch parallel editor-agents to fix HIGH priority issues:

Files to modify:
- content/2_3_speech_to_text.md (~8 edits)
- content/2_4_understanding_bias.md (~12 edits)
- content/2_5_agi_vs_narrow.md (~5 edits)
- content/2_6_ai_domains.md (~4 edits)

Total: 4 files, ~29 edits

Proceed with parallel fixes? [Yes/No]
```

## Edge Cases

**If report is old (>1 hour):**
- Warn user that content may have changed
- Suggest re-running `/content-review` first

**If too many files (>5):**
- Batch into groups to avoid overwhelming parallelization
- Process high-impact files first

**If file was modified since review:**
- Warn user about potential conflicts
- Offer to re-review that specific file first

## Usage Examples

**Standard usage:**
```
/content-review module 2
[Review report generated]

/fix-from-review
[All HIGH priority issues fixed in parallel]
```

**After manual edits:**
```
/content-review content/2_3_speech_to_text.md
[Review finds 5 issues]

/fix-from-review
[Single file fixed]
```

**IMPORTANT:**
- Always show clear signals (⚠️🛑✅) for user awareness
- Confirm before large multi-file edits
- Preserve educational context in explanations
