---
name: FluentCart Developer
description: Comprehensive knowledge base for FluentCart WordPress e-commerce plugin development. Covers theme compatibility, template system, shortcodes, hooks/filters, Elementor integration, custom post types, taxonomies, models, CSS classes, and JavaScript APIs. Use this skill when building themes, plugins, or customizations for FluentCart.
---

# FluentCart Developer Knowledge Base

## Overview

FluentCart is a modern WordPress e-commerce plugin (current version: 1.5.1) that provides a full-featured online store solution. It uses a Vue.js-based frontend with server-side rendering for shop pages, and a custom post type system for products.

**Company**: Fastrsoft
**Plugin Slug**: `fluent-cart`
**Text Domain**: `fluent-cart`
**Minimum PHP**: 7.4+
**WordPress**: 6.0+

## Quick Reference

### Critical Theme Compatibility Line
```php
// Add this in your theme's functions.php — REQUIRED for FluentCart template loading
add_theme_support('fluent_cart');
```

Without this, FluentCart falls back to generic templates and won't load your theme's custom product/archive templates.

### FluentCart Page Types
FluentCart recognizes these page types (from `TemplateService::getCurrentFcPageType()`):
- `single_product` — Single product page (`fluent-products` CPT)
- `product_taxonomy` — Category/Brand archive
- `shop` — Main shop page
- `cart` — Cart page
- `checkout` — Checkout page
- `receipt` — Order receipt/confirmation
- `customer_dashboard` — Customer account/profile
- `registration` — Registration page
- `login` — Login page

---

## Custom Post Types & Taxonomies

### Product CPT
- **Post Type**: `fluent-products` (constant: `FluentProducts::CPT_NAME`)
- **URL Slug**: Configurable via store settings, defaults to `item`
- **Supports**: title, editor, excerpt, thumbnail, author, revisions, custom-fields
- **REST API**: Enabled (`show_in_rest: true`)
- **Has Archive**: Yes
- **Gallery Meta Key**: `fluent-products-gallery-image` (array of `{id, url, name}`)

### Taxonomies
| Taxonomy | Slug | Hierarchical | REST |
|----------|------|-------------|------|
| Product Categories | `product-categories` | Yes | Yes |
| Product Brands | `product-brands` | Yes | Yes |

### URL Hooks
```php
// Customize the product URL slug
add_filter('fluent_cart/front_url_slug', function($slug) {
    return 'products'; // Changes /item/product-name to /products/product-name
}, 10, 1);

// Control whether product URLs include the blog prefix
add_filter('fluent_cart/product_url_with_front', function($withFront) {
    return false;
}, 10, 1);
```

---

## Template System

### How Template Loading Works

FluentCart's template system (`TemplateLoader` class) works like WooCommerce:

1. **Block themes** (`wp_is_block_theme()`) → Uses block templates from `templates/` directory
2. **Classic themes with `fluent_cart` support** → Uses PHP template hierarchy
3. **Unsupported themes** → Falls back to generic template with `get_header()`/`get_footer()`

### Template Hierarchy (Classic Themes)

For **Single Products**, FluentCart looks for (in order):
1. `fluent-cart.php` (in theme root)
2. `single-fluent-products-{slug}.php`
3. `single-fluent-products.php`
4. `fluent-cart/single-fluent-products.php` (in theme subdirectory)

For **Taxonomy Archives** (categories/brands):
1. `taxonomy-product-categories-{slug}.php`
2. `fluent-cart/taxonomy-product-categories-{slug}.php`
3. `taxonomy-product-categories.php`
4. `fluent-cart/taxonomy-product-categories.php`
5. `archive-fluent-products.php`

### Template Path Filter
```php
// Change the subdirectory FluentCart looks in (default: 'fluent-cart/')
add_filter('fluent_cart/template_path', function($path) {
    return 'my-custom-path/';
});
```

### Block Templates (FSE Themes)
Place `.html` block templates in your theme's `templates/` directory:
- `templates/single-fluent-products.html`
- `templates/taxonomy-product-categories.html`
- `templates/taxonomy-product-brands.html`
- `templates/archive-fluent-products.html`

### Template Action Hooks
```php
// Fires before main content in archive/taxonomy templates
do_action('fluent_cart/template/before_content');

// Fires for main content rendering
do_action('fluent_cart/template/main_content');

// Fires after main content
do_action('fluent_cart/template/after_content');

// Fires before rendering the product header (gallery + buy section)
do_action('fluent_cart/product/render_product_header', $productId);

// Fires after product content on single product pages
do_action('fluent_cart/product/after_product_content', $postId);

// Generic fallback template hooks
do_action('fluent_cart/generic_template/rendering');
do_action('fluent_cart/generic_template/before_content');
do_action('fluent_cart/generic_template/after_content');
```

### Fallback Generic Template Structure
```php
<?php
// This is what FluentCart renders for unsupported themes
get_header();
?>
<div class="fct-genric-template-wrapper site-container">
    <div id="main" class="site-main">
        <?php do_action('fluent_cart/template/before_content'); ?>
        <?php do_action('fluent_cart/template/main_content'); ?>
        <?php do_action('fluent_cart/template/after_content'); ?>
    </div>
</div>
<?php get_footer(); ?>
```

---

## Shortcodes

### Complete Shortcode Reference

| Shortcode | Description | Key Attributes |
|-----------|-------------|---------------|
| `[fluent_cart_products]` | Product grid/shop | `per_page`, `view_mode`, `columns`, `category`, `on_sale`, `sort_by`, `enable_filter`, `paginator` |
| `[fluent_cart_checkout]` | Checkout page | — |
| `[fluent_cart_cart]` | Cart page | — |
| `[fluent_cart_receipt]` | Order receipt | — |
| `[fluent_cart_mini_cart]` | Mini cart icon with count | `count_mode` (`distinct_products`/`total_quantity`) |
| `[fluent_cart_single_product]` | Single product display | `id`, `product_id`, `productId`, `productid` |
| `[fluent_cart_pricing_table]` | Pricing comparison table | `variant_ids`, `group_by`, `active_tab`, `badge`, `product_per_row` |
| `[fluent_cart_product_header]` | Product header (gallery+buy) | `id` |
| `[fluent_cart_related_products]` | Related products | `id` |
| `[fluent_cart_add_to_cart_button]` | Add to Cart button | `button_text`, `variation_id`, `class` |
| `[fluent_cart_checkout_button]` | Buy Now / Direct checkout | `button_text`, `variation_id`, `instant_checkout`, `target`, `class` |
| `[fluent_cart_search_bar]` | AJAX product search | — |
| `[fluent_cart_product_card]` | Single product card | `id` |
| `[fluent_cart_store_logo]` | Store logo | — |
| `[fluent_cart_customer_dashboard_button]` | Customer dashboard link | — |
| `[fluent_cart_product_categories_list]` | Category list | — |
| `[fluent_cart_product_title]` | Product title | — |
| `[fluent_cart_product_image]` | Product image | — |

---

## Hooks & Filters

### Product Display Filters
```php
// Customize Add to Cart button text
add_filter('fluent_cart/product/add_to_cart_text', function($text, $args) {
    return 'Add to Bag';
}, 10, 2);

// Customize Out of Stock text
add_filter('fluent_cart/product/out_of_stock_text', function($text, $args) {
    return 'Sold Out';
}, 10, 2);

// Customize Buy Now button text
add_filter('fluent_cart/product/buy_now_button_text', function($text, $args) {
    return 'Purchase Now';
}, 10, 2);

// Show/hide related products on single product page
add_filter('fluent_cart/single_product_page/show_relevant_products', function($show, $productId) {
    return true;
}, 10, 2);

// Disable auto single product page rendering (for custom implementations)
add_filter('fluent_cart/disable_auto_single_product_page', '__return_true');
```

---

## Database Tables

FluentCart creates these custom tables:
- `fc_orders`, `fc_order_items`, `fc_order_transactions`, `fc_order_addresses`, `fc_order_meta`
- `fc_customers`, `fc_customer_addresses`, `fc_customer_meta`
- `fc_carts`, `fc_subscriptions`, `fc_subscriptions_meta`
- `fc_product_details`, `fc_product_variations`, `fc_product_downloads`
- `fc_shipping_zones`, `fc_shipping_methods`, `fc_shipping_classes`
- `fc_tax_classes`, `fc_tax_rates`
- `fc_attribute_groups`, `fc_attribute_terms`, `fc_attribute_relations`
