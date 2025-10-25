---
description: Quick focused edit on a specific issue (tone, citations, flow, etc.)
---

Use the editor-agent for QUICK TARGETED EDITING of a specific issue.

Instead of running all skills, focus on ONE specific problem you've identified.

**AVAILABLE FOCUS AREAS:**

1. **`tone`** → Fix tone violations only (use sentence-clarity-checker for tone)
2. **`clarity`** → Simplify complex sentences (use sentence-clarity-checker for clarity)
3. **`spelling`** → Convert to Singapore English only
4. **`citations`** → Format citations and find uncited claims only
5. **`flow`** → Fix paragraph transitions and ordering only
6. **`structure`** → Reorganize page structure only

**WORKFLOW:**
1. Run the specific skill for the focus area
2. Make ONLY those types of changes
3. Present edited version
4. Wait for approval

**This is the FASTEST editing mode** - use when you've already reviewed content and know exactly what needs fixing.

**Usage examples:**
- `/edit-quick my-ai-course tone courses/my-ai-course/content/3_1_ai_in_workplace_1.md` → Fix only tone issues
- `/edit-quick my-ai-course citations module 2` → Format all citations in Module 2
- `/edit-quick my-ai-course flow courses/my-ai-course/content/2_3_what_is_ai_section_3.md` → Fix paragraph flow only
- `/edit-quick my-ai-course spelling all` → Convert entire course to Singapore English

**WHEN TO USE:**
- After `/review` identifies specific issue types
- When you need one dimension fixed quickly
- When you've already done detailed editing but spotted one more issue
