# FluentCart AI Developer Skill

A comprehensive, platform-agnostic knowledge base and instruction set for FluentCart (v1.5.1) theme and plugin development.

This repository provides ready-to-use configurations and rules for all major AI coding assistants, enabling them to write correct, compatible code for FluentCart out-of-the-box.

---

## Features Covered
- **Custom Payment Gateway Integration**: Register and implement your own payment processor (`AbstractPaymentGateway`) and checkout billing fields (`BaseGatewaySettings`).
- **Ghost Product Selling (Non-Catalog Items)**: Sell custom, dynamically-priced items without creating them in the database.
- **Fee System (Surcharges & Custom Fees)**: Apply dynamic cart surcharges via hooks or save persistent DB fees.
- **Subscription Customization**: Configure renewal grace periods, custom billing intervals, and software license validity defaults.
- **Database Models & Query Builder**: Query database records using Laravel Eloquent model classes (Orders, Customers, Subscriptions, and Products).
- **WordPress Hooks & Filters**: Hook into order status transitions, payment events, and asset loadings.
- **REST API & Webhooks**: Configure outgoing webhook event listeners and REST endpoints.
- **Shipping, Storage, Licensing & Order Bumps**: Register custom shipping calculators, storage drivers, license key status transitions, and checkout upselling triggers (Pro).
- **Easy Digital Downloads (EDD) Migration & Compatibility**: Migrate EDD stores via CLI/wizard and intercept legacy license calls.
- **Template System Overrides**: Folder structure, template hierarchy, and FSE block templates.

---

## Installation

Choose the installation method that fits your environment and AI coding assistant:

### Method 1: The `skills.sh` Method (Recommended for Cursor, Claude Code, Windsurf, Open Code)

You can install this skill directly into your project's local workspace using the agent-agnostic `skills.sh` manager:

```bash
# Using npm
npx skills add atifjubaer/fluentcart-ai-skill

# Using pnpm
pnpm dlx skills add atifjubaer/fluentcart-ai-skill

# Using bun
bunx skills add atifjubaer/fluentcart-ai-skill
```
*This downloads the skill metadata and automatically configures it in your project's agent directory (e.g., `.cursor/skills/` or `.continue/skills/`).*

---

### Method 2: The Direct CLI Initializer (Recommended for Antigravity, Gemini, & Local Rules)

To install the global Antigravity/Gemini developer skill and initialize project rules files (`.cursorrules`, `CLAUDE.md`, `fluentcart-rules.md`) in your current directory on-the-fly:

```bash
# Initialize both global Gemini skill and current project rules
npx github:atifjubaer/fluentcart-ai-skill init

# Setup ONLY the global Antigravity/Gemini skill
npx github:atifjubaer/fluentcart-ai-skill global

# Setup ONLY the Cursor, Claude Code, and web AI rules in current project
npx github:atifjubaer/fluentcart-ai-skill project
```

---

### Method 3: Manual Installation

If you prefer manual setup:
1. **For Antigravity / Gemini**: Copy the `SKILL.md` file and the `references/` directory into your global Gemini config path:
   `~/.gemini/config/skills/fluentcart-developer/`
2. **For Cursor / Windsurf**: Copy the `.cursorrules` file to your project's root directory.
3. **For Claude Code**: Copy the `CLAUDE.md` file to your project's root directory.
4. **For Web-based AIs**: Copy the content of `fluentcart-rules.md` and paste it into the start of your chat thread.

---


## Supported IDE Agents & Formats

This repository covers 100% of the active agentic development platforms:

1. **Antigravity / Gemini-based IDEs**: Configured automatically via `SKILL.md` and the `references/` directory.
2. **Cursor / Windsurf**: Configured automatically via `.cursorrules` placed in your project root.
3. **Claude Code (CLI)**: Configured automatically via `CLAUDE.md` in your project root.
4. **General Web Chat AIs (ChatGPT, Claude Web, Gemini)**: Paste the contents of `fluentcart-rules.md` directly into the chat session.

---

## How it Works

AI coding agents use different mechanisms to load instructions and rules. This repository is built to support all of them:

- **For Antigravity & Gemini**: The `SKILL.md` file serves as the main index with frontmatter triggers. The agent automatically detects when you are working on a FluentCart project and reads `SKILL.md` and the linked documents in `references/` to gain complete context.
- **For Cursor, Windsurf, Kilo Code, and Open Code**: The `.cursorrules` file acts as the project instruction set. When the editor starts up, the AI assistant parses `.cursorrules` automatically and applies the guidelines and reference file patterns to its code generation.
- **For Claude Code**: When launched in your project folder, Claude automatically detects and reads the `CLAUDE.md` file to understand the development workflow, build commands, and coding conventions.

---


## Folder Structure
```
fluentcart-ai-skill/
├── README.md                  # Installation and overview
├── SKILL.md                   # Antigravity/Gemini configuration index
├── CONTRIBUTING.md            # Guidelines for repository contributors & AI agent prompt
├── .cursorrules               # Cursor/Windsurf rules file
├── CLAUDE.md                  # Claude Code instructions
├── fluentcart-rules.md        # Plain text rules for web AIs
├── package.json               # NPM package configuration
├── bin/
│   └── index.js               # CLI Node.js runner script
├── tools/                     # Shared developer scripts
│   ├── scrape_dev_docs.py     # Crawl & convert docs
│   ├── run_scraper.py         # Batch orchestrator
│   ├── fix_links.py           # Relative to absolute links corrector
│   └── validate_links.py      # Relative links validator
└── references/                # Detailed developer guides
    ├── hooks-actions-reference.md
    ├── hooks-filters-reference.md
    ├── database-models-reference.md
    ├── rest-api-reference.md
    ├── paddle-gateway-case-study.md
    ├── database-models-query-builder.md
    ├── fee-system-guide.md
    ├── ghost-product-selling.md
    ├── hooks-actions-filters.md
    ├── payment-gateway-integration.md
    ├── rest-api-webhooks.md
    ├── subscription-customization.md
    └── theme-development-guide.md
```


---

## Contributing
We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to add new references, rules, or update existing documentation.

---

## Created by
Developed and maintained by **Fastrsoft**.
