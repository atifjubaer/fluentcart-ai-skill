# Contributing to FluentCart AI Developer Skill

We welcome contributions to expand the scope and improve the quality of the FluentCart AI Developer Skill and guides!

---

## Contribution Guidelines

To ensure that the documentation and configurations are easily consumable by both developers and AI agentic workflows (e.g. Antigravity/Gemini, Cursor, Claude Code), please follow these core guidelines:

### 1. Relative Reference Pathing
- All links within `SKILL.md` or other files MUST use **relative path links** (e.g., `references/payment-gateway-integration.md`).
- **NEVER** use local-machine absolute paths (e.g., `file:///C:/Users/...` or similar) in the repository files, as they will break for other users and contributors.

### 2. Code Block Comments Rule
- Any code snippets (PHP, JavaScript, HTML, CSS) included in guides or inline code MUST contain **meaningful, descriptive single-line comments**.
- This makes it easy for AI coding agents to follow the implementation context and write correct, readable code for the user.

### 3. File Sizes and Indexing
- Keep `SKILL.md` under **500 lines**.
- If a section grows too long or requires detailed code implementations, split it off into a separate guide file in the `references/` directory, and add a link to it inside the `SKILL.md` index.

---

## Workflow

1. **Fork the Repository**: Create your own copy of the repository on GitHub.
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/your-new-guide
   ```
3. **Make and Validate Changes**:
   - Write or update guides in the `references/` directory.
   - Keep all code examples clear and include meaningful single-line comments in PHP/JS scripts.
   - Run the link validator script (`tools/validate_links.py`) to verify that all relative paths resolve correctly without broken targets.
4. **Shared Developer Tools**:
   - Common utility scripts (e.g. crawler/scraper, link fixer, validator) are located in the `tools/` directory.
   - Contributors can run these tools to pull updates from online docs or check link consistency.
   - The `scratch/` directory is git-ignored and can be used for custom temporary personal scripts.
5. **Submit a Pull Request (PR)**: Send your changes back to the main repository for review!

---

## Auto-Updating Documentation via AI Agents

If you are using an AI coding agent (like Antigravity, Plot, Windsurf, Cursor, or Claude Code) and want to sync the repository with the latest online FluentCart developer documentation, you can use the built-in tools.

### The Update Prompt

Copy and paste the following prompt directly into your AI coding assistant:

```text
Please help me update the FluentCart Developer skill references using the local scraping tools in the repository:
1. Run the scraper script using: python tools/run_scraper.py
2. Run the links corrector to resolve relative paths: python tools/fix_links.py
3. Run the link validator to verify there are no broken references: python tools/validate_links.py
4. If there are any updates, review the changes and commit them to git.
```

The scraper will fetch and convert the latest details from:
- **Development Documentation**: https://dev.fluentcart.com/
- **Full Documentation**: https://docs.fluentcart.com/

