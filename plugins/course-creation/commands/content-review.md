---
description: Review course content quality using editor-agent (structure, flow, clarity, citations)
---

Use the **editor-agent** subagent to perform a comprehensive review of the specified content.

## Scope Handling

First, determine the scope:
- **Single file**: If a file path is provided (e.g., `content/2_3_what_is_ai_section_3.md`)
- **Module**: If "module X" is specified (e.g., "module 2" means all files matching `content/2_*.md`)
- **All**: If "all" is specified (means all files in `content/` directory)

## Task for the Subagent

The editor-agent subagent should:

1. **Determine scope** based on arguments provided
2. **Run in REVIEW MODE** (diagnostic only, no editing)
3. **Use available skills** to analyze content quality
4. **Present a comprehensive report** (see format below)

**IMPORTANT - When to use section-progression-analyzer:**
- **Single file review:** Do NOT use section-progression-analyzer
- **Module review (3+ sections):** ALWAYS use section-progression-analyzer to check section-to-section flow
- **Multi-module review:** Use section-progression-analyzer for EACH module separately

The subagent has access to these skills (which it will invoke as needed):
- `section-progression-analyzer` - **[USE FOR MODULE REVIEWS]** Analyzes section-to-section flow across a module to ensure logical learning progression
- `page-structure-analyzer` - Evaluates page structure and readability
- `paragraph-flow-analyzer` - Analyzes idea flow and transitions within pages
- `sentence-clarity-checker` - Checks tone, clarity, and spelling
- `citation-formatter` - Verifies citations
- `duplicate-content-detector` - Finds redundant content (multi-file)

## Output Format

Present a HIGH-LEVEL SUMMARY REPORT:

```
📊 CONTENT REVIEW REPORT

SCOPE: [files reviewed]

OVERALL ASSESSMENT: [Excellent/Good/Needs Work/Major Revision]

---

📄 PAGE STRUCTURE (Average: X/20)
- Files scoring 18-20: [list]
- Files scoring 15-17: [list]
- Files scoring <15: [list - NEEDS ATTENTION]

Top issues:
- [Issue 1 with file reference]
- [Issue 2 with file reference]

---

📝 PARAGRAPH FLOW
Quality: [Excellent/Good/Needs Work]

Top issues:
- [File]: [Flow issue]
- [File]: [Flow issue]

---

✍️ SENTENCE CLARITY (Average: X/10)
Tone violations: [count]
Clarity issues: [count]
Singapore English errors: [count]

Top issues:
- [File]: [Issue type and example]
- [File]: [Issue type and example]

---

📚 CITATIONS (Average: X/10)
Properly cited: [count]
Missing citations: [count]
Format issues: [count]

Uncited claims found in:
- [File]: [claim]
- [File]: [claim]

---

🔍 DUPLICATE CONTENT (if multi-file review)
Duplicates found: [count]
- Exact duplicates: [count]
- Semantic duplicates: [count]
- Redundant explanations: [count]

Priority duplicates to fix:
1. [Description with file references]
2. [Description with file references]

---

📚 SECTION PROGRESSION (if module review with 3+ sections)
Overall flow quality: [Excellent/Good/Needs Work/Poor]

Top issues:
- [Issue 1: e.g., "Section 5 breaks narrative flow"]
- [Issue 2: e.g., "Missing transitions between Sections 3-4"]
- [Issue 3: e.g., "Concept used before defined"]

Strengths:
- [What's working well in the progression]

---

🎯 PRIORITY ISSUES (Top 10)
Fix these first for maximum impact:

1. [HIGH] [File]: [Issue]
2. [HIGH] [File]: [Issue]
3. [MEDIUM] [File]: [Issue]
...

---

📈 RECOMMENDED NEXT STEPS:
- [Specific action based on findings]
- [Specific action based on findings]
```

**IMPORTANT:**
- This is a DIAGNOSTIC ONLY - make NO edits to files
- Provide specific file names and line numbers when flagging issues
- Prioritize issues by impact (structure problems > minor tone tweaks)
- Be constructive - highlight strengths as well as issues

**Usage examples:**
- `/review content/2_3_what_is_ai_section_3.md` → Review single file
- `/review module 2` → Review all Module 2 files
- `/review all` → Review entire course
