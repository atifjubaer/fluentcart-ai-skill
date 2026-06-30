# FluentCart AI Developer Skill

A comprehensive, platform-agnostic knowledge base and instruction set for FluentCart (v1.5.1) theme and plugin development.

This repository provides ready-to-use configurations and rules for all major AI coding assistants, enabling them to write correct, compatible code for FluentCart out-of-the-box.

## Features Covered
- **WordPress Hooks & Filters**: Complete list of developer hooks and actions.
- **Template System Overrides**: Folder structure, template hierarchy, and FSE block templates.
- **Shortcodes & Gutenberg Blocks**: Full attributes, usage examples, and styling selectors.
- **Elementor Integration**: Widgets reference and custom page-builder controls.
- **Models & Database Tables**: Schema overview for orders, products, carts, and subscriptions.

---

## One-Line Installation (CLI)

You can run this installer instantly on any machine (Windows, macOS, Linux) using Node's `npx` tool without even downloading the repository first:

### Install globally & copy rules to the current directory:
```bash
npx fluentcart-ai-skill@latest
# OR from GitHub directly:
npx github:atifjubaer/fluentcart-ai-skill
```

### Options:
- `npx fluentcart-ai-skill init` — Install global skill + copy project files (Default)
- `npx fluentcart-ai-skill global` — Install global skill only (for Antigravity/Gemini)
- `npx fluentcart-ai-skill project` — Copy project rule files only (for Cursor/Claude Code)

---

## Supported IDE Agents & Formats

This repository covers 100% of the active agentic development platforms:

1. **Antigravity / Gemini-based IDEs**: Configured automatically via `SKILL.md` and the `references/` directory.
2. **Cursor / Windsurf**: Configured automatically via `.cursorrules` placed in your project root.
3. **Claude Code (CLI)**: Configured automatically via `CLAUDE.md` in your project root.
4. **General Web Chat AIs (ChatGPT, Claude Web, Gemini)**: Paste the contents of `fluentcart-rules.md` directly into the chat session.

---

## Folder Structure
```
fluentcart-ai-skill/
├── README.md                  # Installation and overview
├── SKILL.md                   # Antigravity/Gemini configuration
├── .cursorrules               # Cursor/Windsurf rules file
├── CLAUDE.md                  # Claude Code instructions
├── fluentcart-rules.md        # Plain text rules for web AIs
├── package.json               # NPM package configuration
└── bin/
    └── index.js               # CLI Node.js runner script
```

---

## Created by
Developed and maintained by **Fastrsoft**.
