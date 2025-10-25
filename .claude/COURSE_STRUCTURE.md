# Course Folder Structure Reference

## Overview

This plugin supports **multiple courses** in a single repository. Each course lives in its own folder under `courses/`.

## Folder Structure

```
repo-root/
└── courses/
    ├── my-ai-course/
    │   ├── docs/
    │   │   ├── course-proposal.md
    │   │   ├── course-syllabus.md
    │   │   ├── style-guide.md
    │   │   ├── target-audience.md
    │   │   ├── course-structure.md
    │   │   ├── personalization_decision_criteria.md
    │   │   ├── citation-url-archive.md
    │   │   ├── research-findings.md
    │   │   ├── research-brief.md
    │   │   └── module-outlines/
    │   │       ├── module_1_outline.md
    │   │       ├── module_2_outline.md
    │   │       └── module_N_outline.md
    │   └── content/
    │       ├── 1_1_intro.md
    │       ├── 1_2_section.md
    │       ├── 2_1_what_is_ai.md
    │       └── N_N_description.md
    │
    ├── advanced-ai-course/
    │   ├── docs/
    │   └── content/
    │
    └── data-science-101/
        ├── docs/
        └── content/
```

## Path Templates

All commands and skills should use these path templates:

### Documentation Paths
- **Course Proposal:** `courses/{COURSE_NAME}/docs/course-proposal.md`
- **Course Syllabus:** `courses/{COURSE_NAME}/docs/course-syllabus.md`
- **Style Guide:** `courses/{COURSE_NAME}/docs/style-guide.md`
- **Target Audience:** `courses/{COURSE_NAME}/docs/target-audience.md`
- **Course Structure:** `courses/{COURSE_NAME}/docs/course-structure.md`
- **Personalization Criteria:** `courses/{COURSE_NAME}/docs/personalization_decision_criteria.md`
- **Citation Archive:** `courses/{COURSE_NAME}/docs/citation-url-archive.md`
- **Research Findings:** `courses/{COURSE_NAME}/docs/research-findings.md`
- **Research Brief:** `courses/{COURSE_NAME}/docs/research-brief.md`
- **Module Outlines:** `courses/{COURSE_NAME}/docs/module-outlines/module_{N}_outline.md`

### Content Paths
- **Lesson Files:** `courses/{COURSE_NAME}/content/{MODULE}_{SECTION}_{description}.md`
- **Pattern Example:** `courses/my-ai-course/content/2_1_what_is_ai.md`

### Temporary/Review Paths
- **Review Reports:** `.claude/temp/{COURSE_NAME}_review_report.md`

### Style Extractor Paths (Global - Shared Across Courses)
- **Good Examples:** `.claude/skills/style-extractor/examples/{COURSE_NAME}/good/`
- **Bad Examples:** `.claude/skills/style-extractor/examples/{COURSE_NAME}/bad/`
- **Style Output:** `courses/{COURSE_NAME}/docs/style-guide.md`

## Command Parameter Convention

All course-related commands should accept the course name as the **first parameter**:

```
/design-course {COURSE_NAME}
/build-module {COURSE_NAME} {MODULE_NUMBER}
/review {COURSE_NAME}
/fix {COURSE_NAME}
/analyze {COURSE_NAME}
/edit {COURSE_NAME}
/edit-deep {COURSE_NAME}
/refine-syllabus {COURSE_NAME}
```

## How Commands Should Handle Course Names

### 1. Extract Course Name from User Input
Commands should expect the course name as the first argument.

Example:
```
User types: /design-course my-ai-course
Command receives: "my-ai-course"
```

### 2. Validate Course Folder Exists (For Read Operations)
Before reading files, check if the course folder exists:
- If `courses/{COURSE_NAME}/` doesn't exist → show error message
- Suggest running `/design-course {COURSE_NAME}` first

### 3. Create Course Folder (For Write Operations)
When creating new course content:
- Create `courses/{COURSE_NAME}/docs/` if it doesn't exist
- Create `courses/{COURSE_NAME}/content/` if it doesn't exist

### 4. Construct All Paths Using the Template
Replace all hardcoded paths like:
- `docs/course-syllabus.md` → `courses/{COURSE_NAME}/docs/course-syllabus.md`
- `content/2_1_lesson.md` → `courses/{COURSE_NAME}/content/2_1_lesson.md`

## Migration from Single-Course Structure

If you have an existing repo with the old structure:
```
docs/
content/
```

You can migrate to:
```
courses/your-course-name/
├── docs/     (move old docs/ here)
└── content/  (move old content/ here)
```

See `MIGRATION_GUIDE.md` for detailed instructions.

## Benefits of This Structure

✅ **Clear separation:** Each course is completely independent
✅ **Scalable:** Add as many courses as you want
✅ **No conflicts:** No file name collisions between courses
✅ **Easy browsing:** Can see all courses at a glance in `courses/` folder
✅ **Easy archiving:** Can move a course folder to archive when done
