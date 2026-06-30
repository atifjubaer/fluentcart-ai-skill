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

## One-Line CLI Installation

Open your terminal in the skill repository directory and run the command matching your operating system:

### 1. Windows (PowerShell)
To install globally for Antigravity:
```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```
To install globally *and* copy Cursor/Claude configs to your project directory (e.g. `C:\path\to\theme`):
```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1 -ProjectPath "C:\path\to\theme"
```

### 2. macOS & Linux (Bash)
To install globally for Antigravity:
```bash
chmod +x install.sh && ./install.sh
```
To install globally *and* copy Cursor/Claude configs to your project directory:
```bash
chmod +x install.sh && ./install.sh "/path/to/theme"
```

---

## Shared Platform Formats

- **`.cursorrules`**: Copy this file to your theme folder root for **Cursor** to use.
- **`CLAUDE.md`**: Copy this file to your theme folder root for **Claude Code CLI** to use.
- **`fluentcart-rules.md`**: Paste these general rules directly into the web chat interface of **ChatGPT**, **Claude Web**, or any other chatbot.

---

## Folder Structure
```
fluentcart-ai-skill/
├── README.md                  # Installation and overview
├── SKILL.md                   # Antigravity/Gemini configuration
├── .cursorrules               # Cursor rules file
├── CLAUDE.md                  # Claude Code instructions
├── fluentcart-rules.md        # Plain text rules for web AIs
├── install.ps1                # Windows installer script
├── install.sh                 # Unix/Mac installer script
└── references/
    └── theme-development-guide.md  # Coding guide & helper functions
```

---

## Created by
Developed and maintained by **Fastrsoft**.
