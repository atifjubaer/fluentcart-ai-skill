# FluentCart Theme Development Guide

## Compatibility Declaration
To make a WordPress theme fully compatible with FluentCart:

```php
// functions.php
add_action('after_setup_theme', function () {
    add_theme_support('fluent_cart');
});
```

---

## Template Overrides

You can create a `fluent-cart` folder in your theme root to override core templates.

### Overridable files:
- `single-fluent-products.php` (Single product details)
- `taxonomy-product-categories.php` (Category listing page)
- `taxonomy-product-brands.php` (Brand listing page)
- `archive-fluent-products.php` (Main shop list page)

### Example `single-fluent-products.php` Template:
```php
<?php
get_header();
?>
<div class="fluent-fast-single-product site-container">
    <div id="main" class="site-main">
        <?php
        // Renders Breadcrumbs
        do_action('fluent_cart/template/before_content');
        
        // Renders Product Images, Gallery, Variations and Cart Button
        do_action('fluent_cart/product/render_product_header', get_the_ID());
        
        // Renders the Description Content from block editor
        the_content();
        
        // Renders Related Products Carousel
        echo do_shortcode('[fluent_cart_related_products]');
        
        // Fires after main content
        do_action('fluent_cart/product/after_product_content', get_the_ID());
        ?>
    </div>
</div>
<?php
get_footer();
?>
```

---

## Shortcodes

- **Shop/Products Grid**: `[fluent_cart_products columns="4" per_page="12" enable_filter="true"]`
- **Mini Cart Drawer**: `[fluent_cart_mini_cart count_mode="total_quantity"]`
- **Direct Purchase Button**: `[fluent_cart_checkout_button variation_id="123" instant_checkout="yes" button_text="Buy Now"]`
- **Add to Cart Button**: `[fluent_cart_add_to_cart_button variation_id="123" button_text="Add to Bag"]`
- **Customer Dashboard**: `<!-- wp:fluent-cart/customer-profile /-->` or `[fluent_cart_customer_profile]`
- **Cart Page**: `[fluent_cart_cart]`
- **Checkout Page**: `[fluent_cart_checkout]`
- **Receipt Page**: `[fluent_cart_receipt]`
