# Ideas

Prompt to Claude:
```
Interview me to discover my interests, then help me generate five ideas for websites and apps that would maintain my interest while I learn to build them with Claude Code.
```

## Interview 1

- Claude: What topics or hobbies do you find yourself reading about or thinking about outside of work?
- Person 1: Arts, music & creative pursuits
- Claude: What's your current coding experience level?
- Person 1: Some scripting/basics
- Claude: What kind of project structure keeps you motivated?
- Person 1: Something useful I'd actually use daily
- Claude: Within arts/music/creative, what pulls you in most?
- Person 1: Writing or storytelling

Great — writing/storytelling, some scripting experience, and you want something you'd actually use daily. Here are five project ideas, ordered roughly from easiest to most ambitious, so you can build momentum with Claude Code as you go.

1. A personal writing journal with mood/theme tracking
A daily-entry app that tags each entry by theme, mood, or story project, then surfaces patterns over time ("you write about travel a lot in spring"). Simple CRUD app, local storage or a small database — great first Claude Code project since it's contained but genuinely useful daily.

2. A "story bible" for your fiction projects
A structured wiki-style tool for tracking characters, locations, timelines, and plot threads across a novel or series — searchable, with relationship maps between characters. Solves the real pain of scattered notes; teaches you data modeling and search.

3. A daily writing prompt generator tuned to your taste
Instead of generic prompts, you feed it themes/genres/authors you like, and it generates prompts (using the Claude API) that match your voice. You'd use it every morning as a warm-up. Good intro to API integration inside your own app.

4. A reading/writing habit tracker with streaks and word-count goals
Tracks daily word counts or reading time, shows streaks and progress toward a manuscript goal, maybe with gentle nudges. Motivating because you'll watch it fill up with your own real data.

5. A personal "style analyzer" for your own writing
Paste in your drafts over time; it uses the Claude API to track how your voice, sentence length, and vocabulary evolve, and flags overused phrases or crutch words. More technically ambitious (API calls, some light analysis/visualization) — a natural "capstone" once the earlier ones feel easy.

A sensible path: start with #1 (pure fundamentals, no API needed), move to #2 or #4 to add more structure, then tackle #3 and #5 once you're comfortable wiring in the Claude API. Want me to help you scope out the first one — like a simple feature list and data structure — so you have something concrete to hand to Claude Code?

## Interview 2

- Claude: What topics or hobbies do you find yourself reading about or thinking about outside of work?
- Person 2: Health, fitness & food
- Claude: What's your current coding experience level?
- Person 2: Total beginner
- Claude: What kind of project structure keeps you motivated?
- Person 2: A tool solving a personal problem
- Claude: Within health/fitness/food, what pulls you in most?
- Person 2: Cooking & meal planning

Cooking & meal planning, total beginner, and you want something that solves a real problem for you — perfect combo. Here are five ideas, ordered from easiest to most ambitious, so each one builds skills you'll use in the next.

**1. A "what can I make with this?" pantry app**
You type in what's in your fridge/pantry, it matches against a small recipe list you enter yourself. Dead simple to start (just filtering a list), and solves the "I have random stuff, what do I cook" problem immediately. Great first project — no APIs, just basic logic and a form.

**2. A recipe box that scales servings automatically**
Save your favorite recipes, and when you say "make this for 6 instead of 4," it recalculates every ingredient amount. Teaches you basic math/logic in code plus simple data storage — still beginner-friendly but a step up.

**3. A weekly meal planner that builds a shopping list for you**
Drag recipes onto a weekly calendar, and it auto-generates a consolidated grocery list (combining "2 onions" + "1 onion" from different recipes into one line). This is the classic "actually use it every Sunday" app — solves real friction and teaches you to combine and structure data.

**4. A leftover/expiration tracker with smart reminders**
Log what's in your fridge with dates, and it nudges you ("that chicken needs to be used in 2 days — here's a recipe that uses it"). Combines your pantry app (#1) with time-based logic — a natural next step once you're comfortable with the basics.

**5. An AI cooking assistant that adapts recipes to what you have**
Using the Claude API, you describe what's in your kitchen and what you're in the mood for, and it generates a custom recipe on the spot — plus can adjust for dietary swaps ("make this dairy-free"). This is your capstone: once you've built the fundamentals, this teaches you to wire in AI generation for something genuinely useful.

A good path: start with #1 to learn the ropes, then #3 becomes your daily driver pretty fast (meal planning + shopping list is the highest-value habit loop), and #5 is the fun finale once you're not afraid of the basics anymore.

Want me to scope out #1 or #3 into a concrete feature list you can hand to Claude Code to start building?
