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

## Installation & CLI Usage

You can install this skill globally or run it on-demand using any major package manager:

### 1. Global Installation (Recommended for Antigravity/Gemini)

Install the CLI globally on your machine:

```bash
# Using npm
npm install -g fluentcart-ai-skill

# Using pnpm
pnpm add -g fluentcart-ai-skill

# Using yarn
yarn global add fluentcart-ai-skill

# Using bun
bun add -g fluentcart-ai-skill
```

Once installed, run the initializer globally to install the skill for Antigravity/Gemini:
```bash
fluentcart-ai-skill init
```

---

### 2. On-Demand Execution (Recommended for Cursor/Claude Code)

If you just want to initialize rules files in your current project directory on the fly without a global install:

```bash
# Using npm
npx fluentcart-ai-skill init

# Using pnpm
pnpm dlx fluentcart-ai-skill init

# Using yarn
yarn dlx fluentcart-ai-skill init

# Using bun
bunx fluentcart-ai-skill init
```

---

### CLI Command Options:
- `fluentcart-ai-skill init` — Install global skill for Antigravity + copy project rules (`.cursorrules`, `CLAUDE.md`, `fluentcart-rules.md`) to the current directory (Default).
- `fluentcart-ai-skill global` — Install the global Antigravity/Gemini skill only.
- `fluentcart-ai-skill project` — Copy Cursor/Windsurf (`.cursorrules`) and Claude Code (`CLAUDE.md`) rules to the current directory only.

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
├── SKILL.md                   # Antigravity/Gemini configuration index
├── CONTRIBUTING.md            # Guidelines for repository contributors
├── .cursorrules               # Cursor/Windsurf rules file
├── CLAUDE.md                  # Claude Code instructions
├── fluentcart-rules.md        # Plain text rules for web AIs
├── package.json               # NPM package configuration
├── bin/
│   └── index.js               # CLI Node.js runner script
└── references/                # Detailed developer guides
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
