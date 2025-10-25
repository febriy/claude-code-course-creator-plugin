# Migration Guide: Single Course → Multi-Course Structure

This guide helps you migrate existing course content from the old structure (one course per repo) to the new structure (multiple courses per repo).

## What Changed?

### Old Structure (Before)
```
repo-root/
├── docs/
│   ├── course-proposal.md
│   ├── course-syllabus.md
│   ├── style-guide.md
│   └── module-outlines/
│       └── module_1_outline.md
└── content/
    ├── 1_1_intro.md
    ├── 2_1_what_is_ai.md
    └── 2_2_section.md
```

### New Structure (After)
```
repo-root/
└── courses/
    ├── my-first-course/
    │   ├── docs/
    │   │   ├── course-proposal.md
    │   │   ├── course-syllabus.md
    │   │   ├── style-guide.md
    │   │   └── module-outlines/
    │   │       └── module_1_outline.md
    │   └── content/
    │       ├── 1_1_intro.md
    │       ├── 2_1_what_is_ai.md
    │       └── 2_2_section.md
    │
    └── my-second-course/
        ├── docs/
        └── content/
```

---

## Migration Steps

### Step 1: Choose a Course Name

Pick a descriptive name for your existing course:
- Use lowercase letters, numbers, and hyphens only
- Be concise but clear (e.g., "ai-literacy", "data-science-101")
- Avoid spaces or special characters

**Example:** If your course is about "AI Literacy for Educators", name it `ai-literacy-educators`

---

### Step 2: Create the New Folder Structure

Run these commands from your repo root:

```bash
# Replace "YOUR-COURSE-NAME" with your chosen course name
COURSE_NAME="YOUR-COURSE-NAME"

# Create the new folder structure
mkdir -p courses/$COURSE_NAME/docs
mkdir -p courses/$COURSE_NAME/content
```

**Example:**
```bash
COURSE_NAME="ai-literacy-educators"
mkdir -p courses/$COURSE_NAME/docs
mkdir -p courses/$COURSE_NAME/content
```

---

### Step 3: Move Your Files

Move all existing course files to the new location:

```bash
# Move documentation
mv docs/* courses/$COURSE_NAME/docs/

# Move content files
mv content/* courses/$COURSE_NAME/content/

# Optional: Keep old folders as backups temporarily
# (You can delete them later after verifying everything works)
mv docs docs_backup
mv content content_backup
```

---

### Step 4: Update Temporary/Review Files (Optional)

If you have review reports in `.claude/temp/`, consider renaming them to include the course name:

```bash
# Example: Rename review reports
cd .claude/temp
mv module_2_review_report.md ai-literacy-educators_module_2_review_report.md
```

---

### Step 5: Update Style Extractor Examples (If Applicable)

If you've been using the style-extractor skill, organize examples by course:

```bash
# Create course-specific example folders
mkdir -p .claude/skills/style-extractor/examples/$COURSE_NAME/good
mkdir -p .claude/skills/style-extractor/examples/$COURSE_NAME/bad

# Move existing examples
mv .claude/skills/style-extractor/examples/good/* .claude/skills/style-extractor/examples/$COURSE_NAME/good/
mv .claude/skills/style-extractor/examples/bad/* .claude/skills/style-extractor/examples/$COURSE_NAME/bad/
```

---

### Step 6: Verify the Migration

Check that all files are in the right place:

```bash
# List documentation files
ls -la courses/$COURSE_NAME/docs/

# List content files
ls -la courses/$COURSE_NAME/content/

# Verify folder structure
tree courses/$COURSE_NAME/
```

**You should see:**
- All `.md` files from `docs/` now in `courses/{COURSE_NAME}/docs/`
- All `.md` files from `content/` now in `courses/{COURSE_NAME}/content/`
- Module outlines in `courses/{COURSE_NAME}/docs/module-outlines/`

---

### Step 7: Test the New Commands

Try running commands with the new course name parameter:

```bash
# Review the course
/review $COURSE_NAME all

# Build a new module
/build-module $COURSE_NAME 3

# Analyze existing content
/analyze $COURSE_NAME
```

---

## Updated Command Syntax

All commands now require a course name as the first parameter:

| Old Command | New Command |
|-------------|-------------|
| `/design-course` | `/design-course my-course` |
| `/build-module 2` | `/build-module my-course 2` |
| `/review all` | `/review my-course all` |
| `/fix` | `/fix my-course` |
| `/analyze` | `/analyze my-course` |
| `/edit my-file.md` | `/edit my-course my-file.md` |
| `/edit-detailed module 2` | `/edit-detailed my-course module 2` |
| `/refine-syllabus "changes"` | `/refine-syllabus my-course "changes"` |

---

## Troubleshooting

### Problem: "Course not found" error

**Solution:** Double-check your course folder exists:
```bash
ls courses/
# Should show your course name
```

### Problem: Commands can't find files

**Solution:** Verify files are in the correct locations:
```bash
# Check docs exist
ls courses/YOUR-COURSE-NAME/docs/course-syllabus.md

# Check content exists
ls courses/YOUR-COURSE-NAME/content/
```

### Problem: Old commands still referencing old paths

**Solution:** Make sure you're using the updated plugin version. The plugin should now expect the new structure.

---

## Rollback (If Needed)

If something goes wrong, you can restore the old structure:

```bash
# Restore from backups (if you created them)
mv docs_backup docs
mv content_backup content

# Remove the new structure
rm -rf courses/
```

---

## Benefits of the New Structure

✅ **Multiple courses:** You can now work on multiple courses in one repo
✅ **Clear organization:** Each course is self-contained
✅ **No conflicts:** Course files won't interfere with each other
✅ **Easy archiving:** Move completed courses to an archive folder
✅ **Scalable:** Add as many courses as you want

---

## Next Steps

After migration:
1. ✅ Test all your commands with the new course name
2. ✅ Create a second course to test multi-course functionality
3. ✅ Update any external scripts or documentation that reference file paths
4. ✅ Delete backup folders (`docs_backup`, `content_backup`) once verified

---

## Questions?

If you encounter issues:
1. Check that all files moved correctly
2. Verify the course name has no spaces or special characters
3. Ensure you're using the course name parameter in all commands
4. Review the folder structure matches the expected layout

Happy course creating! 🎓
