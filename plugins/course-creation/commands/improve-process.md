---
description: Analyze workflow with agents/skills/commands and propose process improvements
---

Use the **process-improvement** agent to analyze recent interactions with agents, skills, and slash commands, then recommend structural improvements.

## Context to Provide

When invoking this command, you should tell the agent about:
- **What you just did** - Which agents/skills/commands you used
- **What worked well** - Smooth parts of the workflow
- **What was frustrating** - Friction points, unclear steps, inefficiencies
- **What you wished existed** - Missing capabilities or better integration

## Task for the Agent

The process-improvement agent should:

1. **Analyze the current workflow** based on your description
2. **Review existing agent/skill/command structure**
3. **Identify improvement opportunities** in:
   - Agent design (prompts, task delegation, output format)
   - Skill structure (granularity, reusability, parameters)
   - Command workflows (user experience, integration patterns)
   - Agent-skill-command integration
4. **Propose specific changes** with implementation guidance

## Areas of Analysis

The agent will examine:

### Agent Design
- Is the agent prompt clear and actionable?
- Does it use skills effectively?
- Is the output format useful?
- Are there unnecessary steps?

### Skill Structure
- Are skills at the right level of granularity?
- Can skills be reused across multiple agents?
- Do skills have clear, focused purposes?
- Are skill outputs standardized?

### Command Workflows
- Is the user experience smooth?
- Are there unnecessary confirmation steps?
- Is scope determination intuitive?
- Does the command integrate well with other workflows?

### Integration Patterns
- How do agents, skills, and commands work together?
- Are there redundancies or gaps?
- Could automation be improved?
- Are handoffs between components smooth?

## Output Format

The agent should provide:

```
🔧 PROCESS IMPROVEMENT ANALYSIS

WORKFLOW REVIEWED: [name of agent/skill/command analyzed]

---

✅ WHAT'S WORKING WELL:
- [Strength 1]
- [Strength 2]
- [Strength 3]

---

⚠️ FRICTION POINTS IDENTIFIED:

1. [HIGH PRIORITY] [Issue]
   - Impact: [how this affects user]
   - Root cause: [why this happens]

2. [MEDIUM PRIORITY] [Issue]
   - Impact: [how this affects user]
   - Root cause: [why this happens]

---

💡 PROPOSED IMPROVEMENTS:

### Improvement 1: [Title]
**Type:** [Agent Design / Skill Structure / Command Workflow / Integration]
**Priority:** [High / Medium / Low]
**Impact:** [Expected benefit]

**Current state:**
[What exists now]

**Proposed change:**
[What should change]

**Implementation:**
```
[Concrete code/config changes]
```

**Why this helps:**
[Explanation of benefit]

---

### Improvement 2: [Title]
[Same structure as above]

---

🎯 RECOMMENDED IMPLEMENTATION ORDER:

1. [Improvement name] - [Reason to do first]
2. [Improvement name] - [Reason to do second]
3. [Improvement name] - [Reason to do third]

---

📋 NEXT STEPS:

To implement these improvements:
1. [Specific action]
2. [Specific action]
3. [Specific action]
```

## Usage Examples

**After using an agent:**
```
User: /improve-process
User: I just ran /content-review on Module 2. The agent worked well but I had to answer 2 separate questions to specify scope. Also, the report was great but I wish I could jump directly to fixing high-priority issues.
```

**After using a skill:**
```
User: /improve-process
User: I used the citation-formatter skill and it found issues but didn't suggest the exact format I should use. I had to look up examples separately.
```

**General workflow analysis:**
```
User: /improve-process
User: I notice I keep running content-review, then edit-detailed separately. Could these be combined somehow?
```

**IMPORTANT:**
- Be specific about what you experienced
- Focus on your actual workflow, not hypotheticals
- Describe both what worked and what didn't
- The agent will propose concrete, implementable changes
