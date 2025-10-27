# Claude Code Writer Plugins

A marketplace of Claude Code plugins for creating professional content - educational courses, LinkedIn posts, and more.

## 🎯 What's Inside?

This marketplace provides specialized plugins that transform Claude Code into a powerful content creation assistant:

### 📚 Plugin 1: **course-creation**
Create, edit, and review educational course content with AI-powered tools.

### 💼 Plugin 2: **linkedin-posts**
Create engaging LinkedIn posts using atomic essay methodology with guided workflows.

---

## 🚀 Quick Start

### Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- Basic familiarity with Claude Code plugins

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/febriy/claude-code-writer-plugins.git
   cd claude-code-writer-plugins
   ```

2. **The plugins are automatically available** through the marketplace structure

3. **Verify installation** by typing `/course-creation:` or `/linkedin-posts:` in Claude Code

---

## 📦 Plugin 1: Course Creation

### What It Does

Transform Claude Code into a comprehensive course development assistant:

- ✅ **Design complete courses** from concept to curriculum
- ✅ **Build engaging modules** with proper structure
- ✅ **Review and improve** content quality
- ✅ **Edit based on feedback** with learning system
- ✅ **Extract documentation** from existing content
- ✅ **Restructure courses** (split, merge, reorder)
- ✅ **Analyze progression** across modules
- ✅ **Format citations** consistently
- ✅ **Detect duplicate content**

### Main Commands

```bash
/course-creation:design-course {name} "description"
/course-creation:create-content {name} module {number}
/course-creation:review {name} [module|all]
/course-creation:edit {name} [--from-review]
/course-creation:extract-course-info {name}
/course-creation:restructure {name} "instruction"
```

### Quick Example

```bash
# Create a new course
/course-creation:design-course my-ai-course "AI literacy for employees"

# Build the modules
/course-creation:create-content my-ai-course module 1

# Review quality
/course-creation:review my-ai-course all

# Fix issues
/course-creation:edit my-ai-course --from-review
```

[📖 Full Course Creation Documentation](./plugins/course-creation/README.md)

---

## 💼 Plugin 2: LinkedIn Posts

### What It Does

Create compelling LinkedIn posts with strategic guidance and proven structure:

- ✅ **Profile-based writing** - Remembers your brand, voice, and goals
- ✅ **Thought development** - Helps you move beyond surface-level ideas
- ✅ **Strategic angles** - Suggests directions based on your objectives
- ✅ **Atomic essay structure** - Uses Nicolas Cole's proven 4-piece format
- ✅ **Guided workflow** - From inspiration to publish in 15-20 minutes
- ✅ **Performance tracking** - Save posts with metadata for learning

### Main Commands

```bash
# One-time setup
/linkedin-posts:setup-profile

# Create posts
/linkedin-posts:create
```

### How It Works

1. **Setup once:** Tell the agent about your professional identity, goals, voice, and audience
2. **Create posts:** The agent guides you through:
   - Capturing what inspired you
   - Developing your unique angle
   - Writing a structured draft (headline, intro, main points, conclusion)
   - Iterating until you're satisfied
   - Saving with metadata

### The Atomic Essay Structure

Every post follows this proven format:
- **Headline** (2-3 min): Clear, specific promise
- **Intro** (4-5 min): 5-element checklist (what, who, promise, credibility, benefit)
- **Main Points** (3-4 min): 1-3-1 pattern (topic, details, summary) × 3
- **Conclusion** (1-2 min): Add NEW insight (don't recap)

**Total time: 10-15 minutes of writing**

### Quick Example

```bash
# First time setup
/linkedin-posts:setup-profile

# Create a post
/linkedin-posts:create

Agent: What inspired this post?
You: I went to an AI conference where someone said AI will replace 80% of jobs...
Agent: [Helps you develop your angle and writes a structured post]
```

[📖 Full LinkedIn Posts Documentation](./plugins/linkedin-posts/README.md)

---

## 🧰 Skills & Agents

### Course Creation Skills
- `page-structure-analyzer` - Overall page organization
- `paragraph-flow-analyzer` - Idea flow and transitions
- `sentence-clarity-checker` - Tone, clarity, simplicity
- `citation-formatter` - Consistent citation formatting
- `module-progression-analyzer` - Learning flow validation
- `section-progression-analyzer` - Section-level flow
- `duplicate-content-detector` - Redundancy detection
- `style-extractor` - Style guide generation

### LinkedIn Posts Skills
- `atomic-essay-writer` - Nicolas Cole's 4-piece structure with 1-3-1 pattern

### Agents
- `editor-agent` (course-creation) - Comprehensive content editing
- `post-creator-agent` (linkedin-posts) - Guided post creation workflow

---

## 💡 Usage Examples

### Create a Course from Scratch

```bash
/course-creation:design-course ai-fundamentals "AI basics for managers"
/course-creation:create-content ai-fundamentals module 1
/course-creation:review ai-fundamentals module 1
/course-creation:edit ai-fundamentals --from-review
```

### Create a LinkedIn Post

```bash
/linkedin-posts:setup-profile  # One time only
/linkedin-posts:create          # Creates post with guided workflow
```

### Work with Existing Course Content

```bash
/course-creation:extract-course-info legacy-course
/course-creation:review legacy-course all
/course-creation:edit legacy-course --from-review
```

---

## 📁 Project Structure

```
claude-code-writer-plugins/
├── .claude-plugin/
│   └── marketplace.json              # Marketplace configuration
├── plugins/
│   ├── course-creation/              # Course creation plugin
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/                 # Slash commands
│   │   ├── skills/                   # Specialized analysis tools
│   │   └── agents/                   # Background workers
│   │
│   └── linkedin-posts/               # LinkedIn posts plugin
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── commands/                 # Slash commands
│       ├── skills/                   # Writing methodology
│       └── agents/                   # Post creator
│
└── README.md                         # This file
```

---

## 🛠️ File Organization (Generated)

### Course Creation Output

```
courses/
  {course-name}/
    content/                          # Course content files
    docs/                             # Documentation & guides
    .edit-history/                    # Learning history
```

### LinkedIn Posts Output

```
linkedin-profile.md                   # Your profile (one time)
linkedin-posts/                       # Saved posts with metadata
  2025-01-27-topic-name.md
  2025-01-28-topic-name.md
```

---

## 💡 Best Practices

### Course Creation
1. Follow the numbered workflow (1→2→3→4) for new courses
2. Use inline comments (`<!-- EDIT: ... -->`) for precise control
3. Review before editing with `--from-review`
4. Let the plugin learn from your feedback patterns

### LinkedIn Posts
1. Set up your profile first for consistent brand voice
2. Don't rush to writing - develop your thinking first
3. Follow the atomic essay structure consistently
4. Track performance data to learn what works

---

## 🤝 Contributing

Found a bug or have a feature request? Please open an issue or submit a pull request!

### Ideas for Future Plugins
- Email newsletter creation
- Blog post writing
- Twitter thread generation
- Presentation slide content

---

## 📄 License

MIT License - Feel free to use and modify for your content creation needs.

---

## ✉️ Author

**Arvin**
Email: febrification@gmail.com
GitHub: [@febriy](https://github.com/febriy)

---

**Made with Claude Code** 🤖
