# Changes for *Claude Code Visual Bible*

> **Last checked:** 30 October 2026
>
> This page covers changes to Claude Code from the start of September 2026 up to version **2.1.311** (26 October 2026). To check which version you have, run `claude --version`. To update, run `claude update`.

- [Changes for *Claude Code Visual Bible*](#changes-for-claude-code-visual-bible)
- [Summary](#summary)
- [Models](#models)
  - [New default models: Opus 5.5, Sonnet 5.5, Haiku 5.5, and Fable 5.1](#new-default-models-opus-55-sonnet-55-haiku-55-and-fable-51)
  - [Effort: Ultracode is now a separate toggle, and ultrathink means xhigh](#effort-ultracode-is-now-a-separate-toggle-and-ultrathink-means-xhigh)
- [Permissions](#permissions)
  - [Auto mode is now the default for interactive sessions](#auto-mode-is-now-the-default-for-interactive-sessions)
  - [Project settings can no longer turn on bypassPermissions](#project-settings-can-no-longer-turn-on-bypasspermissions)
  - [Headless runs start in Manual mode](#headless-runs-start-in-manual-mode)
  - [New /auto-mode-setup command](#new-auto-mode-setup-command)
- [Project instructions: AGENTS.md support](#project-instructions-agentsmd-support)
- [Extending Claude Code](#extending-claude-code)
  - [Mods](#mods)
  - [Testing plugins with claude plugin eval](#testing-plugins-with-claude-plugin-eval)
- [Subagents and context](#subagents-and-context)
  - [Fork subagents are on by default everywhere](#fork-subagents-are-on-by-default-everywhere)
  - [Idle compaction](#idle-compaction)
- [Everyday quality-of-life changes](#everyday-quality-of-life-changes)
- [Code review](#code-review)
- [Desktop app and VS Code](#desktop-app-and-vs-code)
- [Other behavior changes to be aware of](#other-behavior-changes-to-be-aware-of)
- [Sources](#sources)

---

# Summary

| Date | Version | Change |
|---|---|---|
| 1 Sep 2026 | 2.1.257 | Claude Fable 5.1 becomes the default Fable model. Project settings can no longer turn on `bypassPermissions`. |
| 7–11 Sep 2026 | 2.1.263–2.1.269 | `claude plugin eval`, `maxEffortLevel` setting, 5-minute WebFetch deadline, pop-out panes in the desktop app. |
| 18 Sep 2026 | 2.1.277 | Claude Code reads `AGENTS.md` when there is no `CLAUDE.md`. |
| 22 Sep 2026 | 2.1.280 | Claude Opus 5.5 becomes the default Opus model. |
| 28 Sep 2026 | 2.1.284 | Claude Sonnet 5.5 becomes the default Sonnet model. Auto mode becomes the default for interactive sessions on every plan and provider. Ultracode becomes a separate toggle. |
| 29 Sep 2026 | 2.1.285 | `claude --desktop` opens the Claude desktop app on the current folder or session. |
| 1 Oct 2026 | 2.1.287 | **Mods** launch, including the built-in "You should know" mod. |
| 2 Oct 2026 | 2.1.288 | Recover a prompt cleared with Ctrl+C. `/code-review --max-findings`. `claude project purge` renamed to `claude purge`. |
| 7 Oct 2026 | 2.1.293 | Claude Haiku 5.5 becomes the default Haiku model. |
| 14 Oct 2026 | 2.1.299 | Idle compaction for large conversations. |
| 16 Oct 2026 | 2.1.302 | Fork subagents on by default everywhere. `claude -p` and Agent SDK runs start in Manual mode in more situations. |
| 19 Oct 2026 | 2.1.304 | `/auto-mode-setup`. Code Review levels (Quick, Standard, Deep). |
| 22 Oct 2026 | 2.1.309 | `sed -i` edits run as normal Bash commands and are not restored by `/rewind`. |
| 26 Oct 2026 | 2.1.311 | `ultrathink` runs the turn at xhigh effort on the 5.5-generation models. |

---

# Models

## New default models: Opus 5.5, Sonnet 5.5, Haiku 5.5, and Fable 5.1

Between 1 September and 7 October, Anthropic released four new models, and Claude Code added each one on its launch day. On the Anthropic API, the `opus`, `sonnet`, `haiku`, and `fable` aliases now point to the new models:

| Model | Model ID | Released | Minimum Claude Code version | Context | Price per million tokens (input/output) |
|---|---|---|---|---|---|
| Claude Fable 5.1 | `claude-fable-5-1` | 1 Sep 2026 | 2.1.257 | 1M | $10 / $50 |
| Claude Opus 5.5 | `claude-opus-5-5` | 22 Sep 2026 | 2.1.280 | 1M | $4 / $20 |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | 28 Sep 2026 | 2.1.284 | 1M | $2 / $10 |
| Claude Haiku 5.5 | `claude-haiku-5-5` | 7 Oct 2026 | 2.1.293 | — | — |

Notes:

- Opus 5.5 is now the default model on the Pro, Max, Team, and Enterprise plans.
- Haiku 5.5's context window and price aren't shown in Claude Code's changelog; check Anthropic's models overview before quoting them.
- In 2.1.296, the price Claude Code reports for Sonnet 5.5 cache reads dropped from $0.20 to $0.10 per million tokens. This affects `/cost`, the status line, and `--max-budget-usd`.
- On Amazon Bedrock, Google Vertex AI, Microsoft Foundry, and Claude apps gateways, some aliases kept pointing to older models for a while after launch. If you use one of these, check which model you are on with `/model`.

> **Book update:** Wherever the book names a specific default model, or shows `/model` output, readers will now see the 5.5-generation models.

## Effort: Ultracode is now a separate toggle, and ultrathink means xhigh

- **Ultracode (2.1.284):** Ultracode is now an on/off toggle in `/effort`, separate from the effort level. It no longer forces xhigh effort. When it is on, Claude can use dynamic workflows for larger tasks at whatever effort level the session uses.
  - To turn it on, enter `/effort ultracode`.
  - To turn it off, enter `/effort ultracode off`.
  - `claude --effort ultracode` still starts a session with Ultracode on **and** xhigh effort.
- **ultrathink (2.1.311):** Typing `ultrathink` in the terminal now runs that turn at xhigh effort on Opus 5.5, Sonnet 5.5, Haiku 5.5, and Fable 5.1 through Anthropic's API. If you type it while Claude is working, it raises the effort for the rest of that turn.
- **maxEffortLevel (week of 7 September):** Administrators can now cap the effort level for every provider. Set it at the top level or per model under `modelSettings`. Any higher level runs at the cap.

---

# Permissions

## Auto mode is now the default for interactive sessions

Auto mode uses a safety classifier to check each action, instead of asking you to approve every command. It became the default in two steps:

1. **14 August 2026:** Auto mode became the default for new sessions on the Pro, Max, and Team plans.
2. **28 September 2026 (2.1.284):** Interactive terminal and VS Code sessions with no permission mode set now start in auto mode on **every** plan and provider.

Since late September, auto mode for Claude API and Enterprise users, and on Bedrock, Vertex, Foundry, and gateways, uses a server-side classifier by default. Anthropic does not charge for that classifier's overhead.

To start in a different mode, set `permissions.defaultMode` in your user settings (`~/.claude/settings.json`), or pass `--permission-mode` when you start Claude Code. You can still switch modes during a session with Shift+Tab.

> **Book update:** Wherever the book says Claude Code starts in default (Manual) mode and asks before each action, readers on 2.1.284 or later will start in auto mode unless they have set a different default.

## Project settings can no longer turn on bypassPermissions

From 2.1.257, Claude Code ignores `"defaultMode": "bypassPermissions"` in a project's `.claude/settings.json` or `.claude/settings.local.json`, as it already did for `"auto"`. This stops a repository you clone from switching off permission checks for you.

If you need bypass permissions mode, do one of these instead:

- Set it in your user settings, `~/.claude/settings.json`.
- Start Claude Code with `claude --permission-mode bypassPermissions`.

**Watch out:** When the project file sets `bypassPermissions`, the session starts in Manual mode, even if your user settings say `auto`. Remove the line from the project's settings files.

## Headless runs start in Manual mode

From 2.1.302, `claude -p` and Agent SDK sessions with no permission mode set start in Manual (`default`) mode on third-party providers, with telemetry off, or on a fresh install. To use auto mode in those runs, pass `--permission-mode auto`.

## New /auto-mode-setup command

Version 2.1.304 adds `/auto-mode-setup`. It reads your project and recent sessions, and then helps auto mode learn about your environment, so it blocks fewer legitimate actions.

---

# Project instructions: AGENTS.md support

Many other coding agents (Codex, Cursor, Copilot, and others) read project instructions from `AGENTS.md`. From 2.1.277, Claude Code reads `AGENTS.md` when there is no `CLAUDE.md` in the folder you work in or any folder above it.

- If both files exist, Claude Code uses `CLAUDE.md` and ignores `AGENTS.md`. To use both, import `AGENTS.md` from your `CLAUDE.md`.
- Any `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` in your folder or above it turns the fallback off.
- To change this behavior, run `/config` and change **Project instructions**.
- At launch, the fallback was off on Bedrock, Vertex, and Foundry.

> **Book update:** Wherever the book says Claude Code only reads `CLAUDE.md`, add that it now falls back to `AGENTS.md`.

---

# Extending Claude Code

## Mods

Version 2.1.287 (1 October 2026) introduced **mods**. A mod is a plugin written in JavaScript or TypeScript that runs inside Claude Code. It can:

- change prompts and tool calls, for example to hold a risky command until you approve it
- replace some built-in features
- add panes, buttons, and status bars to the screen

Mods are on by default. They work in the terminal and in the Code tab of the desktop app. Some of Claude Code's own features are now built-in mods, including `/diff` and `AGENTS.md` loading. You can find these in `/plugin` under **Built-in**.

The easiest way to create a mod is to describe what you want in a Claude Code session, and Claude will write and load it for you.

**Security:** Mods are **not** sandboxed. They run with the same access to your machine as Claude Code itself. Only install mods you trust. Organization administrators can control which mods load.

**You should know:** Version 2.1.287 also added a built-in mod called "You should know". It runs a side agent that watches the session and points out things you or Claude might have missed.

If you set `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` to try mods during early access, remove it. Version 2.1.287 and later ignore it.

## Testing plugins with claude plugin eval

Version 2.1.269 added `claude plugin eval`. It runs your plugin against a set of test cases and scores the results. By default, it also runs each case without the plugin, so you can see what the plugin adds.

1. From your plugin's root folder, run `claude plugin eval init`. Claude asks what a good result looks like, and then drafts the test cases.
2. Run `claude plugin eval .` to score every case. A summary table appears in your terminal, and `evals/results/report.html` has the details.

Every run is a real model call on your account, so evals cost usage.

---

# Subagents and context

## Fork subagents are on by default everywhere

A fork subagent starts with a copy of your current conversation. Version 2.1.302 turns fork subagents on by default in `claude -p`, the Agent SDK, the desktop app, and VS Code, as they already were in the terminal. To turn them off, set `CLAUDE_CODE_FORK_SUBAGENT=0`.

The desktop app and VS Code now always run the main conversation's subagents in the background, as the terminal does.

## Idle compaction

From 2.1.299, if you leave a conversation of 200K tokens or more idle for about 54 minutes, Claude Code compacts it just before its one-hour prompt cache expires. This means your next message doesn't reprocess the whole conversation at full cost.

To turn it off, use the **Idle compaction** row in `/config` (2.1.302 or later), or set `"idleCompaction": false` in `settings.json`.

---

# Everyday quality-of-life changes

- **Recover a cleared prompt (2.1.288):** If you clear a prompt with Ctrl+C by mistake, press Up on the empty prompt to bring it back, including pasted text and images.
- **Open the desktop app (2.1.285):** `claude --desktop` opens the Claude desktop app on the current folder. Add `--continue` or `--resume <id>` to open a session.
- **Command completion mid-prompt:** When you type `/` partway through a prompt, Claude Code shows a list of matching commands instead of a single suggestion.
- **WebFetch deadline:** If WebFetch hasn't finished downloading a page within five minutes, the fetch now fails instead of hanging. Change the limit with `CLAUDE_CODE_WEBFETCH_DEADLINE_MS`, or set it to `0` to remove it.
- **Usage warnings on resume (2.1.304):** On the Pro and Max plans, Claude Code warns you when resuming a long inactive conversation would use a noticeable share of your 5-hour usage limit. You can resume anyway, or start a new conversation and refer to the old one.
- **Renamed command (2.1.288):** `claude project purge` is now `claude purge`.

---

# Code review

- **Choose how many findings (2.1.288):** `/code-review --max-findings <n>` reports up to that many findings, and `--max-findings all` reports every finding. Claude Code remembers your choice until you pass `--max-findings default`.
- **Review levels (2.1.304):** For Code Review on GitHub, organization Owners can choose **Quick**, **Standard** (the default), or **Deep** reviews for the whole organization or per repository.
- **Stop automatic reviews (2.1.307):** Comment `@claude review stop` on a pull request to end an `@claude review always` subscription.

---

# Desktop app and VS Code

- **Pop-out panes:** In the desktop app, you can pop any pane, such as the diff or terminal, out into its own window, and dock it back later.
- **Agent map in VS Code:** Click the agent count under the prompt box to see your subagents, open a read-only transcript, or stop one.
- **Hooks and permissions in VS Code:** In the command menu's **Customize** section, select **Hooks** or **Permissions** to add or remove them in your user, project, and local settings.

---

# Other behavior changes to be aware of

- **`sed -i` and `/rewind` (2.1.309):** `sed -i` now runs as a normal Bash command with the standard permission prompt. Like other Bash edits, `/rewind` does not undo it.
- **Claude Design (2.1.302):** Claude Code now warns in `/design-sync` and `/design-login` that the standalone Claude Design site (claude.ai/design) closes by 14 December 2026.

---

# Sources

- [Claude Code changelog – Anthropic](https://code.claude.com/docs/en/changelog)
- [What's new, Week 37 (7–11 September 2026) – Anthropic](https://code.claude.com/docs/en/whats-new/2026-w37)
- [Choose a permission mode – Anthropic](https://code.claude.com/docs/en/permission-modes)
- [Claude Code v2.1.284 release notes – claude-world.com](https://claude-world.com/articles/claude-code-21284-release/)
- [Claude Fable 5.1 and the Claude 5.5 family: what changed for Claude Code – claude-world.com](https://claude-world.com/articles/claude-fable-5-1-and-claude-5-5-family/)
- [Claude Code adds AGENTS.md fallback – DevOps.com](https://devops.com/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)
- [Customize Claude Code with mods – claudekit](https://claudekit.io/en/updates/claude-code-mods/)
- [Claude Code 2.1.288 – claudekit](https://claudekit.io/en/updates/claude-code-2-1-288/)
- [Project settings no longer turn on bypass permissions – wmedia.es](https://wmedia.es/en/tips/claude-code-bypass-permissions-project-settings)
