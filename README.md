# Course Creation Plugin for Claude Code

A comprehensive Claude Code plugin for creating, editing, and reviewing educational course content. This plugin provides specialized commands, skills, and agents to help you design courses, write modules, and ensure high-quality educational materials.

## 🎯 What Does This Plugin Do?

This plugin transforms Claude Code into a powerful course development assistant. It helps you:

- **Design complete courses** from initial concept to full curriculum
- **Build engaging modules** with proper structure and flow
- **Review and improve** existing content for quality and clarity
- **Analyze learning progression** across modules and sections
- **Format citations** consistently throughout your materials
- **Detect duplicate content** to keep your courses concise
- **Ensure clear writing** that meets educational standards

## 📦 Features

### Slash Commands

Quick-access commands for common course creation tasks:

- `/course-creation:design-course` - Research and design a complete course curriculum from scratch
- `/course-creation:build-module` - Draft complete module content from an outline
- `/course-creation:content-review` - Review course content for structure, flow, clarity, and citations
- `/course-creation:edit-quick` - Quick focused edits on specific issues (tone, citations, flow)
- `/course-creation:edit-detailed` - Detailed page-by-page, line-by-line editing
- `/course-creation:fix-from-review` - Fix issues identified in content review reports
- `/course-creation:refine-syllabus` - Update course syllabus based on feedback
- `/course-creation:analyze-existing-course` - Reverse-engineer course documentation from existing content
- `/course-creation:improve-process` - Analyze and improve your course creation workflow

### Skills

Specialized analysis tools that you can invoke anytime:

- **citation-formatter** - Format citations using bracketed numbers with references
- **duplicate-content-detector** - Find and flag redundant content across pages
- **module-progression-analyzer** - Ensure logical learning flow between modules
- **section-progression-analyzer** - Analyze section-to-section progression within modules
- **page-structure-analyzer** - Evaluate overall page structure and readability
- **paragraph-flow-analyzer** - Check paragraph structure and idea flow
- **sentence-clarity-checker** - Analyze sentences for tone, clarity, and simplicity
- **style-extractor** - Learn writing style from examples and generate style guides

### Agents

Background workers for complex tasks:

- **editor-agent** - Comprehensive content editor for structure, flow, clarity, and citations

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

## 💡 How to Use

### Starting a New Course

```bash
/course-creation:design-course
```
Claude will guide you through researching and designing a complete curriculum.

### Building Module Content

```bash
/course-creation:build-module
```
Provide your module outline and Claude will draft the complete content.

### Reviewing Your Content

```bash
/course-creation:content-review
```
Get a comprehensive quality report on your course materials.

### Quick Edits

```bash
/course-creation:edit-quick
```
Fix specific issues like tone, citations, or flow problems.

## 📝 Example Workflow

1. **Design** your course with `/course-creation:design-course`
2. **Build** each module with `/course-creation:build-module`
3. **Review** the content with `/course-creation:content-review`
4. **Fix issues** using `/course-creation:fix-from-review`
5. **Refine** based on feedback with `/course-creation:refine-syllabus`

## 🛠️ Configuration

This plugin works out-of-the-box with default settings. You can customize:

- **Style preferences** - Use `/course-creation:style-extractor` to create custom style guides
- **Citation formats** - Adjust citation formatting rules in the citation-formatter skill
- **Review criteria** - Modify rubrics in the analyzer skills

## 🤝 Contributing

Found a bug or have a feature request? Please open an issue or submit a pull request!

## 📄 License

MIT License - Feel free to use and modify for your educational content creation needs.

## ✉️ Author

**Arvin**
Email: febrification@gmail.com

---

**Made with Claude Code** 🤖
