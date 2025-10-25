# Style Extractor Skill

**Purpose:** Learn writing style from your example texts and generate a custom style guide.

---

## Quick Start

### **1. Add Example Files**

**Good Examples** (required - what you WANT):
```bash
# Add 3-10 text files showing your desired writing style
# Place in: .claude/skills/style-extractor/examples/good/

.claude/skills/style-extractor/examples/good/
├── example1.md
├── example2.txt
├── example3.md
└── ...
```

**Bad Examples** (optional - what you DON'T want):
```bash
# Add 2-5 text files showing styles to AVOID
# Place in: .claude/skills/style-extractor/examples/bad/

.claude/skills/style-extractor/examples/bad/
├── too_casual.txt
├── too_formal.md
└── ...
```

---

### **2. Run the Skill**

```bash
# In your conversation with Claude:
Skill style-extractor
```

Or from a command/agent:
```markdown
Use the `style-extractor` skill to analyze examples and generate a style guide.
```

---

### **3. Get Your Style Guide**

Output saved to:
```
courses/{COURSE_NAME}/docs/style-guide.md
```

This guide includes:
- ✅ Tone & voice guidelines with examples
- ✅ Sentence structure patterns
- ✅ Word choice do's and don'ts
- ✅ Formatting standards
- ✅ Content organization patterns
- ✅ Quick reference checklist
- ✅ Before/after examples

---

## What Gets Analyzed

The skill examines your examples across 7 dimensions:

| Dimension | What It Looks For |
|-----------|------------------|
| **Tone & Voice** | Formal vs casual, direct vs conversational, emotional temperature |
| **Sentence Structure** | Length, complexity, active/passive voice, variety |
| **Word Choice** | Vocabulary level, technical terms, common phrases, words to avoid |
| **Formatting** | Headers, paragraphs, lists, bold/italic usage, white space |
| **Content Organization** | Information sequencing, opening/closing patterns, transitions |
| **Rhetorical Techniques** | Questions, examples, metaphors, parallel structure |
| **Audience Adaptation** | Assumed knowledge, explanation depth, respect for reader |

---

## Example Usage

### **For AI4E Course:**

**Goal:** Ensure all new content matches existing Module 2 style

**Step 1:** Gather good examples
```bash
# Copy existing good content to examples/good/
cp content/2_2_what_is_ai_section_2.md .claude/skills/style-extractor/examples/good/
cp content/2_3_what_is_ai_section_3.md .claude/skills/style-extractor/examples/good/
```

**Step 2:** (Optional) Add bad examples
```bash
# Add blog posts, casual content, or overly academic writing
echo "Your problematic example text" > .claude/skills/style-extractor/examples/bad/too_casual.txt
```

**Step 3:** Generate guide
```bash
Skill style-extractor
```

**Step 4:** Use in content development
- Reference guide when running `/build-module`
- Check new content with `/edit-quick` against style guide
- Include in editor-agent instructions

---

## Tips for Best Results

### **Good Examples Should:**
✅ Be complete pieces (not fragments)
✅ Be representative of your desired style
✅ Cover different topics in same style
✅ Be your actual best work
✅ Number 3-10 files (more is better up to ~10)

### **Bad Examples Should:**
✅ Show clear problems you want to avoid
✅ Be different types of "bad" (too casual, too formal, too jargon-heavy)
✅ Number 2-5 files (less is fine, this is optional)

### **File Formats:**
- `.md` (Markdown) - preferred
- `.txt` (Plain text) - works fine
- Any text file the skill can read

---

## What You Get

The generated style guide includes:

### **1. Overview Section**
- Style summary
- Target audience
- Primary goal

### **2. For Each Dimension (7 total):**
- ✅ **Do This** - Guidelines with good examples
- ❌ **Don't Do This** - Anti-patterns with bad examples
- 💡 **Why It Matters** - Explanations

### **3. Quick Reference Checklist**
Easy checklist for writers/editors to use during work

### **4. Comparison Examples**
Side-by-side good vs bad for clarity

### **5. Analysis Appendix**
Details about what was analyzed and pattern confidence

---

## Advanced Usage

### **Mode 1: Generate Style Guide** (Default)
Analyzes examples → Generates comprehensive guide

**Command:**
```
Skill style-extractor
```

---

### **Mode 2: Check Style Compliance**
Compares new text against learned style

**Command:**
```
Use style-extractor skill in Mode 2 to check if [filename] matches the style guide
```

**Output:** Compliance report with:
- Overall score (X/10)
- What matches ✅
- What doesn't match ❌
- Specific line-by-line issues
- Suggested fixes

---

## Updating Your Style Guide

As your style evolves:

1. **Add new good examples** to `examples/good/`
2. **Re-run the skill**
3. **Review changes** in updated guide
4. **Archive old guide** (automatic - gets timestamped)

The skill learns from ALL examples, so adding more refines the guide.

---

## Integration with Other Commands

### **With `/build-module`:**
```bash
/build-module 3

# In the agent prompt, reference:
"Follow the style guide in courses/{COURSE_NAME}/docs/style-guide.md"
```

### **With `/edit-detailed` or `/edit-quick`:**
```bash
/edit-detailed content/3_2_section.md "Match the style guide from style-extractor output"
```

### **With `/content-review`:**
```bash
/content-review module 3

# After review, check against style:
Skill style-extractor (Mode 2) on content/3_2_section.md
```

---

## Folder Structure

```
.claude/skills/style-extractor/
├── SKILL.md                     # Skill prompt (analyzes examples)
├── README.md                    # This file (usage instructions)
├── examples/
│   ├── good/                    # ← Put desired style examples here
│   │   ├── example1.md
│   │   ├── example2.txt
│   │   └── ...
│   └── bad/                     # ← Put undesired style examples here (optional)
│       ├── too_casual.txt
│       └── ...
└── output/
    └── (skill generates courses/{COURSE_NAME}/docs/style-guide.md)
```

---

## Frequently Asked Questions

**Q: How many examples do I need?**
A: Minimum 3 good examples. Ideal: 5-10 good, 2-5 bad (optional).

**Q: Can I use existing course content as examples?**
A: Yes! Copy your best sections to `examples/good/`.

**Q: What if examples are inconsistent?**
A: The skill will note "low confidence" patterns. Add more consistent examples or refine existing ones.

**Q: Do bad examples have to be terrible?**
A: No. They can be "acceptable but not our style" - helps define boundaries.

**Q: Can I update the guide later?**
A: Yes! Add more examples and re-run. The old guide gets archived automatically.

**Q: How do I use the guide with automated tools?**
A: Reference it in agent prompts for `/build-module`, `/edit-detailed`, etc.

**Q: Can this work for technical documentation? Marketing copy? Casual blogs?**
A: Yes! It learns whatever style your examples demonstrate.

---

## Example Workflow

**Scenario:** You want all Module 4 content to match Module 2's style

**Step 1:** Extract good examples
```bash
cp content/2_2_what_is_ai_section_2.md .claude/skills/style-extractor/examples/good/section_2_2.md
cp content/2_3_what_is_ai_section_3.md .claude/skills/style-extractor/examples/good/section_2_3.md
cp content/2_6_what_is_ai_section_6.md .claude/skills/style-extractor/examples/good/section_2_6.md
```

**Step 2:** Add counter-examples (optional)
```bash
# Find a blog post that's too casual
# Save to: .claude/skills/style-extractor/examples/bad/casual_blog.txt
```

**Step 3:** Generate guide
```
Skill style-extractor
```

**Step 4:** Build Module 4 with style guide
```bash
/build-module 4
# Agent will draft content

# Then check compliance:
Skill style-extractor (Mode 2) on content/4_1_intro.md
# Get compliance report, fix issues
```

**Step 5:** Polish with style in mind
```bash
/edit-quick content/4_2_section.md "Fix style mismatches identified in compliance report"
```

---

## Troubleshooting

**Problem:** Generated guide is too vague
**Solution:** Add more good examples (aim for 7-10)

**Problem:** Guide contradicts itself
**Solution:** Your examples may be inconsistent. Review examples for alignment.

**Problem:** Can't tell if new content matches style
**Solution:** Use Mode 2 (Style Compliance Check) to get objective report

**Problem:** Want to emphasize certain patterns more
**Solution:** Add more examples demonstrating those patterns

**Problem:** Guide doesn't capture subtle nuances
**Solution:** Add examples specifically showing those nuances

---

## Next Steps

1. **Add your example files** to `examples/good/` (and optionally `examples/bad/`)
2. **Run the skill:** `Skill style-extractor`
3. **Review the generated guide** in `courses/{COURSE_NAME}/docs/style-guide.md`
4. **Use the guide** when creating or editing content
5. **Update as needed** by adding examples and regenerating

---

**Ready to create your custom style guide?**

Start by adding example files to `.claude/skills/style-extractor/examples/good/`
