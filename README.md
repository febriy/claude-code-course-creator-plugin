# Course Creation Plugin for Claude Code

A comprehensive Claude Code plugin for creating, editing, and reviewing educational course content. This plugin provides specialized commands, skills, and agents to help you design courses, write modules, and ensure high-quality educational materials.

## 🎯 What Does This Plugin Do?

This plugin transforms Claude Code into a powerful course development assistant. It helps you:

- **Design complete courses** from initial concept to full curriculum
- **Build engaging modules** with proper structure and flow
- **Review and improve** existing content for quality and clarity
- **Edit based on your comments** with learning from your feedback patterns
- **Extract documentation** from existing course content
- **Restructure courses** by splitting, merging, or reordering modules
- **Analyze learning progression** across modules and sections
- **Format citations** consistently throughout your materials
- **Detect duplicate content** to keep your courses concise

---

## 📦 Two Main Workflows

### Workflow 1: Create from Scratch (PRIMARY)

The numbered sequence (1→2→3→4) guides you through building a new course:

```
1. Design Course → 2. Create Content → 3. Review → 4. Edit
```

### Workflow 2: Work with Existing Content

Extract documentation from existing content, then use the same quality control tools:

```
Extract Course Info → Review → Edit
```

---

## 🚀 Installation

### Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- Basic familiarity with the Claude Code plugin system

### Steps

1. **Clone or download this repository** to your local machine

2. **Copy the plugin folder** to your Claude Code plugins directory:
   ```bash
   cp -r plugins/course-creation ~/.claude/plugins/
   ```

3. **Restart Claude Code** or reload your configuration

4. **Verify installation** by typing `/course-creation:` in Claude Code - you should see available commands

---

## 💡 Commands Reference

### Main Workflow Commands (Numbered 1-4)

#### 1️⃣ `/design-course` - Design Your Course
**Purpose:** Research and design a complete course curriculum from scratch

**When to use:** Starting a brand new course

**What it does:**
- Researches the topic
- Proposes learning objectives
- Creates module structure
- Generates syllabus and outlines

**Example:**
```bash
/course-creation:design-course my-ai-course "AI literacy for employees"
```

---

#### 2️⃣ `/create-content` - Write Module Content
**Purpose:** Write complete module content from your course design

**When to use:** After designing your course, to build each module

**What it does:**
- Reads module outline
- Researches content
- Writes all sections
- Adds citations
- Creates engaging examples

**Example:**
```bash
/course-creation:create-content my-ai-course module 1
/course-creation:create-content my-ai-course module 2
```

---

#### 3️⃣ `/review` - Review Content Quality
**Purpose:** Check content quality and generate a comprehensive review report

**When to use:** After writing content to check for issues

**What it does:**
- Analyzes page structure
- Checks paragraph flow
- Reviews sentence clarity
- Validates citations
- Detects duplicate content
- Generates priority-ranked issues list

**Scope options:**
- Single file: `/review my-ai-course courses/my-ai-course/content/2_3_section.md`
- Single module: `/review my-ai-course module 2`
- All content: `/review my-ai-course all`

**Example:**
```bash
/course-creation:review my-ai-course module 1
```

---

#### 4️⃣ `/edit` - Fix Issues
**Purpose:** Edit content based on your comments OR review reports OR both

**When to use:** To fix issues found in review, or to make changes based on your feedback

**Three modes:**

**Mode 1: Your inline comments**
```bash
# Add comments to your file:
<!-- EDIT: Make this more concise -->
<!-- FIX: Tone too casual -->

# Then run:
/course-creation:edit my-ai-course courses/my-ai-course/content/3_1_intro.md
```

**Mode 2: Auto-fix from review report**
```bash
# After running /review, automatically fix HIGH priority issues:
/course-creation:edit my-ai-course --from-review
```

**Mode 3: Both combined**
```bash
# Fix your comments AND review issues:
/course-creation:edit my-ai-course courses/my-ai-course/content/3_1_intro.md --from-review
```

**What it does:**
- Extracts your comments from files
- Reads review reports for issues
- Logs all feedback for learning
- Shows edit plan for approval
- Makes comprehensive edits
- Learns your preferences over time

---

### Supporting Commands

#### `/extract-course-info` - Analyze Existing Content
**Purpose:** Extract structure, tone, and documentation from existing course content

**When to use:** You have existing course content but no formal documentation

**What it does:**
- Scans all existing content files
- Extracts module structure
- Identifies topics and themes
- Analyzes current tone and style
- Generates syllabus from content
- Creates module outlines
- Builds research brief from citations

**Example:**
```bash
/course-creation:extract-course-info my-ai-course
```

---

#### `/restructure` - Reorganize Course Structure
**Purpose:** Change course organization (split, merge, or reorder modules)

**When to use:** Need to reorganize your course structure

**What it does:**
- Reads current syllabus
- Proposes structural changes
- Validates with progression analyzer
- Updates all affected files
- Maintains content consistency

**Examples:**
```bash
# Split a module
/course-creation:restructure my-ai-course "split module 2 into 2A and 2B"

# Reorder modules
/course-creation:restructure my-ai-course "move module 3 before module 2"

# Adjust time
/course-creation:restructure my-ai-course "reduce total time to 40 minutes"
```

---

#### `/improve-workflow` - Meta Process Improvement
**Purpose:** Analyze and improve your course creation workflow

**When to use:** Want to optimize your plugin usage

**What it does:**
- Analyzes how you use commands
- Reviews skill effectiveness
- Identifies bottlenecks
- Proposes workflow improvements
- Suggests better practices

**Example:**
```bash
/course-creation:improve-workflow
```

---

## 📝 Complete Workflow Examples

### Example 1: Creating a New Course from Scratch

```bash
# Step 1: Design the course
/course-creation:design-course my-ai-course "AI literacy for employees"

# Step 2: Create content for each module
/course-creation:create-content my-ai-course module 1
/course-creation:create-content my-ai-course module 2
/course-creation:create-content my-ai-course module 3

# Step 3: Review quality
/course-creation:review my-ai-course all

# Step 4: Fix issues automatically
/course-creation:edit my-ai-course --from-review

# Optional: Restructure if needed
/course-creation:restructure my-ai-course "split module 2"
```

---

### Example 2: Working with Existing Content

```bash
# Step 1: Extract documentation from existing content
/course-creation:extract-course-info legacy-course

# Step 2: Review the content
/course-creation:review legacy-course all

# Step 3: Fix issues
/course-creation:edit legacy-course --from-review

# Step 4: Make custom edits
# Add your comments to files, then:
/course-creation:edit legacy-course courses/legacy-course/content/section1.md
```

---

### Example 3: Iterative Editing with Learning

```bash
# First round: Add comments to a file
<!-- EDIT: Too technical, simplify -->
<!-- FIX: Add real-world example -->

/course-creation:edit my-ai-course courses/my-ai-course/content/module1.md

# Second round: Different file, but plugin remembers your preferences
/course-creation:edit my-ai-course courses/my-ai-course/content/module2.md
# Plugin now knows you prefer simpler language and real-world examples!
```

---

## 🧰 Skills Reference

Specialized analysis tools that activate automatically when needed:

### Content Quality Skills
- **page-structure-analyzer** - Evaluate overall page structure and readability
- **paragraph-flow-analyzer** - Check paragraph structure and idea flow
- **sentence-clarity-checker** - Analyze sentences for tone, clarity, and simplicity
- **citation-formatter** - Format citations using bracketed numbers with references

### Course Structure Skills
- **module-progression-analyzer** - Ensure logical learning flow between modules
- **section-progression-analyzer** - Analyze section-to-section progression within modules
- **duplicate-content-detector** - Find and flag redundant content across pages

### Utilities
- **style-extractor** - Learn writing style from examples and generate style guides

**To invoke a skill manually:**
```bash
Skill citation-formatter
Skill duplicate-content-detector
```

---

## 🤖 Agents

Background workers for complex tasks:

- **editor-agent** - Comprehensive content editor that uses all skills to improve structure, flow, clarity, and citations

Agents run autonomously and report back with results. They're invoked automatically by commands but you can also launch them directly using the Task tool.

---

## 📊 Learning System

The `/edit` command builds a learning history:

**How it works:**
1. Every time you run `/edit`, your comments are logged
2. Comments are stored in `courses/{COURSE}/.edit-history/comments-log.jsonl`
3. Future edits analyze this history to understand your preferences
4. The style guide evolves based on your actual feedback patterns

**What gets learned:**
- Your tone preferences
- Common issues you flag
- Your structural preferences
- Spelling and citation standards you prefer

**Benefits:**
- Edits become more aligned with your style over time
- Less repetitive feedback needed
- Proactive identification of issues you care about
- Data-driven style guide improvements

---

## 🛠️ File Structure

After using this plugin, your course will be organized like this:

```
courses/
  my-ai-course/
    content/                    # Your course content files
      1_1_intro.md
      1_2_section.md
      2_1_section.md
      ...
    docs/                       # Course documentation
      course-syllabus.md
      style-guide.md
      target-audience.md
      module-outlines/
        module_1_outline.md
        module_2_outline.md
        ...
    .edit-history/              # Learning history (auto-generated)
      comments-log.jsonl        # All your past feedback
      backups/                  # Timestamped backups
```

---

## 💡 Tips & Best Practices

### 1. Follow the Numbered Workflow
For new courses, use commands 1→2→3→4 in order for best results.

### 2. Use Comments for Precise Control
Add inline comments to guide edits exactly where you want them:
```markdown
<!-- EDIT: Add citation here -->
<!-- FIX: Simplify this paragraph -->
```

### 3. Review Before Editing
Always run `/review` before `/edit --from-review` to see what will be changed.

### 4. Iterate in Small Steps
Make small, incremental edits. Review after each change.

### 5. Let the Plugin Learn
The more you use `/edit` with comments, the smarter it gets about your preferences.

### 6. Use Extract for Legacy Content
Have old course materials? Use `/extract-course-info` to bring them into the plugin's structure.

### 7. Restructure Carefully
Before running `/restructure`, make sure you have backups. It changes file names and references.

---

## 🤝 Contributing

Found a bug or have a feature request? Please open an issue or submit a pull request!

---

## 📄 License

MIT License - Feel free to use and modify for your educational content creation needs.

---

## ✉️ Author

**Arvin**
Email: febrification@gmail.com

---

**Made with Claude Code** 🤖
