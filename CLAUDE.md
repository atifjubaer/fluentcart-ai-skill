# Claude Code Instructions for FluentCart Development

This project is built using FluentCart (v1.5.1) for WordPress.

## Build/Developer Guidelines
- Always preserve theme compatibility actions: `add_theme_support('fluent_cart')`.
- All FluentCart page templates should be loaded via WordPress standard theme templates or overrides inside `fluent-cart/` subdirectory.
- Always include single-line comments in code to document key actions.

## Command Reference
- Link theme to local WordPress setup:
  `cmd /c mklink /J "C:\dhon\htdocs\fluentcart_theme\wp-content\themes\fluentfast" "."`

## FluentCart Framework APIs
### Key Actions:
- `fluent_cart/template/before_content` (Breadcrumbs, headings)
- `fluent_cart/product/render_product_header` (Product details purchase UI)
- `fluent_cart/product/after_product_content` (Post-product widgets)

### Key Filters:
- `fluent_cart/product/add_to_cart_text` (Button text customization)
- `fluent_cart/disable_auto_single_product_page` (Disables core templates layout)
