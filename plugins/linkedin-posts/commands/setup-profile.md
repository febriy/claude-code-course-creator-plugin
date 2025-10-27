---
description: One-time setup to learn about your LinkedIn profile, brand, and content goals
---

# LinkedIn Profile Setup

**Run this command once** to teach the LinkedIn plugin about who you are and what you want to achieve.

This creates a profile file that all other LinkedIn commands will reference.

---

## What This Does

Guides you through a conversation to capture:
1. **Your professional identity** - Role, expertise, industry
2. **Your LinkedIn goals** - Why you post (thought leadership, networking, sales, etc.)
3. **Your unique voice** - How you communicate (formal? casual? storytelling?)
4. **Your audience** - Who you're trying to reach
5. **Your constraints** - Time, frequency, topics to avoid

Then saves this to `linkedin-profile.md` for future reference.

---

## Task for Agent

When user runs `/linkedin-posts:setup-profile`, guide them through this conversation:

### Step 1: Professional Identity

Ask:
> **Let's start with the basics. Tell me about yourself professionally:**
> - What's your current role and company?
> - What's your primary area of expertise or industry?
> - What do you want to be known for on LinkedIn?

**Capture:**
- Role/title
- Company/industry
- Core expertise areas
- Professional positioning (e.g., "AI educator for non-technical audiences")

---

### Step 2: LinkedIn Goals

Ask:
> **What are you trying to achieve with LinkedIn posts?**
>
> Common goals:
> - Build thought leadership in your field
> - Share knowledge and help others learn
> - Network with industry peers
> - Generate leads or business opportunities
> - Document your learning journey
> - Position yourself for career opportunities
>
> Which of these resonate? Any others?

**Capture:**
- Primary goal (1-2 main objectives)
- Secondary goals
- Success metrics (if they have any - likes, comments, DMs, opportunities?)

---

### Step 3: Content Preferences

Ask:
> **What kind of content do you typically want to create?**
>
> Think about:
> - Do you prefer sharing insights from events you attend?
> - Reacting to articles or industry news?
> - Sharing personal experiences and lessons learned?
> - Commenting on trends or debates in your field?
> - Teaching concepts or frameworks?
> - Storytelling about projects or challenges?

**Capture:**
- Content types they gravitate toward
- Topics they're passionate about
- Topics they want to avoid

---

### Step 4: Voice & Tone

Ask:
> **How do you want to sound in your posts?**
>
> Consider:
> - Formal and authoritative vs. casual and conversational?
> - Personal storytelling vs. professional analysis?
> - Opinionated and bold vs. balanced and thoughtful?
> - Humorous and light vs. serious and focused?
>
> Is there a LinkedIn creator whose style you admire or want to emulate?

**Capture:**
- Tone preferences (formal/casual spectrum)
- Storytelling style (personal/analytical)
- Opinion level (bold/balanced)
- Example creators they like (optional)

---

### Step 5: Audience

Ask:
> **Who are you writing for?**
>
> Think about:
> - Their role/seniority (e.g., "Mid-level product managers")
> - Their challenges or interests
> - What they need from you
> - What would make them engage with your content?

**Capture:**
- Primary audience description
- Their pain points or interests
- What value you provide to them

---

### Step 6: Practical Constraints

Ask:
> **A few practical questions:**
>
> - How often do you want to post? (e.g., weekly, 2-3x/week, when inspired)
> - How much time can you spend on a post? (e.g., 15 min, 30 min, 1 hour)
> - Are there any topics or approaches you want to avoid?
> - Any company/professional boundaries to respect?

**Capture:**
- Posting frequency goal
- Time budget per post
- Topics to avoid
- Professional constraints (NDA, company policy, etc.)

---

### Step 7: Example Posts (Optional)

If they have existing posts they're proud of, ask:
> **Do you have any LinkedIn posts you've written that you really liked?**
>
> If yes, share the URL or text - I can analyze your natural style.

**If provided:**
- Read the posts
- Note patterns in:
  - Structure (how they open, develop, close)
  - Language (vocabulary, sentence length)
  - Hooks (how they grab attention)
  - Personal elements (do they share stories?)

---

### Step 8: Generate Profile Document

Create `linkedin-profile.md` with this structure:

```markdown
# LinkedIn Profile - [Name]

**Created:** [Date]
**Last Updated:** [Date]

---

## Professional Identity

**Role:** [Current role and company]
**Industry:** [Industry/domain]
**Expertise:** [Core areas of expertise]
**Positioning:** [How they want to be known - one sentence]

---

## LinkedIn Goals

**Primary Goal:** [Main objective]
**Secondary Goals:**
- [Goal 2]
- [Goal 3]

**Success Looks Like:** [How they measure impact]

---

## Target Audience

**Who:** [Description of primary audience]
**Their Challenges:** [What problems they face]
**Value You Provide:** [What you give them]

---

## Voice & Tone

**Tone:** [Formal/Casual spectrum with description]
**Style:** [Personal storytelling / Professional analysis / Mix]
**Opinion Level:** [Bold and opinionated / Balanced and thoughtful]
**Inspiration:** [Any creators they admire - if mentioned]

---

## Content Preferences

**Favorite Content Types:**
- [Type 1 - e.g., Event insights]
- [Type 2 - e.g., Article reactions]
- [Type 3 - e.g., Personal lessons]

**Topics of Interest:**
- [Topic 1]
- [Topic 2]
- [Topic 3]

**Topics to Avoid:**
- [Any topics to stay away from]

---

## Posting Habits

**Frequency Goal:** [How often they want to post]
**Time Budget:** [How long they can spend per post]
**Best Posting Times:** [If they know - otherwise leave for later optimization]

---

## Constraints & Boundaries

**Professional:**
- [Any company policies, NDAs, etc.]

**Personal:**
- [Any personal boundaries]

---

## Style Analysis

[If they provided example posts, include analysis here:]

**Observed Patterns:**
- **Opening hooks:** [How they typically start posts]
- **Structure:** [How they organize ideas]
- **Personal elements:** [How much they share about themselves]
- **Call-to-action:** [How they end posts]

**Vocabulary notes:** [Any distinctive language patterns]

---

## Quick Reference

Use this profile when:
- Creating new LinkedIn posts (`/linkedin-posts:create`)
- Brainstorming content ideas
- Reviewing post drafts
- Suggesting post angles

**Remember:** [Name] wants to [primary goal] by [approach] for [audience].
```

---

### Step 9: Confirm & Save

Show them the profile and ask:
> **Here's your LinkedIn profile. Does this accurately capture who you are and what you want to achieve?**
>
> Feel free to request changes to any section.

Once approved, save to `linkedin-profile.md`

Confirm:
> ✅ **Profile saved!**
>
> You're all set. Next time you want to create a post, run:
> `/linkedin-posts:create`
>
> I'll use this profile to help you brainstorm angles, develop your thoughts, and write compelling posts.

---

## Important Notes

- This is a **living document** - they can update it anytime
- Be conversational and patient - not an interrogation
- If they're unsure about something, give examples to help them think
- Don't force them to answer every question if they're uncertain
- The goal is to understand them well enough to be a helpful thought partner

---

## Example Usage

```
User: /linkedin-posts:setup-profile

Agent: Let's get to know you! This will help me create better LinkedIn content for you.

First, tell me about yourself professionally:
- What's your current role and company?
- What's your primary area of expertise?
- What do you want to be known for on LinkedIn?

User: I'm a learning designer specializing in AI education. I work with companies to train their employees on AI tools. I want to be known as someone who makes AI accessible to non-technical people.

Agent: Perfect! That's a clear positioning.

Now, what are you trying to achieve with LinkedIn posts?
[Continues conversation...]
```

---

## Success Criteria

This command succeeds when:
- ✅ Profile document captures their identity, goals, audience, and voice
- ✅ They feel understood and accurately represented
- ✅ Document is detailed enough to guide future post creation
- ✅ File saved to `linkedin-profile.md`
