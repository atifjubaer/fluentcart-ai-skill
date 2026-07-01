import os
import re
import time
from scrape_dev_docs import fetch_and_convert

# Define output references directory path
REF_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "references"))

# Define URLs for action hooks
ACTION_HOOKS_URLS = [
    ("Orders", "https://dev.fluentcart.com/hooks/actions/orders.html"),
    ("Subscriptions", "https://dev.fluentcart.com/hooks/actions/subscriptions.html"),
    ("Licenses", "https://dev.fluentcart.com/hooks/actions/licenses.html"),
    ("Cart & Checkout", "https://dev.fluentcart.com/hooks/actions/cart-and-checkout.html"),
    ("Customers & Users", "https://dev.fluentcart.com/hooks/actions/customers-and-users.html"),
    ("Products & Coupons", "https://dev.fluentcart.com/hooks/actions/products-and-coupons.html"),
    ("Payments & Integrations", "https://dev.fluentcart.com/hooks/actions/payments-and-integrations.html"),
    ("Admin & Templates", "https://dev.fluentcart.com/hooks/actions/admin-and-templates.html")
]

# Define URLs for filter hooks
FILTER_HOOKS_URLS = [
    ("Settings & Configuration", "https://dev.fluentcart.com/hooks/filters/settings-and-configuration.html"),
    ("Orders & Payments", "https://dev.fluentcart.com/hooks/filters/orders-and-payments.html"),
    ("Products & Pricing", "https://dev.fluentcart.com/hooks/filters/products-and-pricing.html"),
    ("Cart & Checkout", "https://dev.fluentcart.com/hooks/filters/cart-and-checkout.html"),
    ("Customers & Subscriptions", "https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions.html"),
    ("Integrations & Advanced", "https://dev.fluentcart.com/hooks/filters/integrations-and-advanced.html")
]

# Define URLs for database models
DATABASE_MODELS_URLS = [
    ("Order", "https://dev.fluentcart.com/database/models/order.html"),
    ("OrderItem", "https://dev.fluentcart.com/database/models/order-item.html"),
    ("OrderMeta", "https://dev.fluentcart.com/database/models/order-meta.html"),
    ("OrderTransaction", "https://dev.fluentcart.com/database/models/order-transaction.html"),
    ("OrderAddress", "https://dev.fluentcart.com/database/models/order-address.html"),
    ("OrderOperation", "https://dev.fluentcart.com/database/models/order-operation.html"),
    ("OrderTaxRate", "https://dev.fluentcart.com/database/models/order-tax-rate.html"),
    ("OrderDownloadPermission", "https://dev.fluentcart.com/database/models/order-download-permission.html"),
    ("Customer", "https://dev.fluentcart.com/database/models/customer.html"),
    ("CustomerAddresses", "https://dev.fluentcart.com/database/models/customer-addresses.html"),
    ("CustomerMeta", "https://dev.fluentcart.com/database/models/customer-meta.html"),
    ("Product", "https://dev.fluentcart.com/database/models/product.html"),
    ("ProductDetail", "https://dev.fluentcart.com/database/models/product-detail.html"),
    ("ProductVariation", "https://dev.fluentcart.com/database/models/product-variation.html"),
    ("ProductMeta", "https://dev.fluentcart.com/database/models/product-meta.html"),
    ("ProductDownload", "https://dev.fluentcart.com/database/models/product-download.html"),
    ("Subscription", "https://dev.fluentcart.com/database/models/subscription.html"),
    ("SubscriptionMeta", "https://dev.fluentcart.com/database/models/subscription-meta.html"),
    ("Cart", "https://dev.fluentcart.com/database/models/cart.html"),
    ("Coupon", "https://dev.fluentcart.com/database/models/coupon.html"),
    ("AppliedCoupon", "https://dev.fluentcart.com/database/models/applied-coupon.html"),
    ("Activity", "https://dev.fluentcart.com/database/models/activity.html"),
    ("ScheduledAction", "https://dev.fluentcart.com/database/models/scheduled-action.html"),
    ("Meta", "https://dev.fluentcart.com/database/models/meta.html"),
    ("User", "https://dev.fluentcart.com/database/models/user.html"),
    ("DynamicModel", "https://dev.fluentcart.com/database/models/dynamic-model.html"),
    ("AttributeGroup", "https://dev.fluentcart.com/database/models/attribute-group.html"),
    ("AttributeTerm", "https://dev.fluentcart.com/database/models/attribute-term.html"),
    ("AttributeRelation", "https://dev.fluentcart.com/database/models/attribute-relation.html"),
    ("ShippingZone", "https://dev.fluentcart.com/database/models/shipping-zone.html"),
    ("ShippingMethod", "https://dev.fluentcart.com/database/models/shipping-method.html"),
    ("ShippingClass", "https://dev.fluentcart.com/database/models/shipping-class.html"),
    ("TaxClass", "https://dev.fluentcart.com/database/models/tax-class.html"),
    ("TaxRate", "https://dev.fluentcart.com/database/models/tax-rate.html"),
    ("Label", "https://dev.fluentcart.com/database/models/label.html"),
    ("LabelRelationship", "https://dev.fluentcart.com/database/models/label-relationship.html"),
    ("License", "https://dev.fluentcart.com/database/models/license.html"),
    ("LicenseMeta", "https://dev.fluentcart.com/database/models/license-meta.html"),
    ("LicenseActivation", "https://dev.fluentcart.com/database/models/license-activation.html"),
    ("LicenseSite", "https://dev.fluentcart.com/database/models/license-site.html"),
    ("OrderPromotion", "https://dev.fluentcart.com/database/models/order-promotion.html"),
    ("OrderPromotionStat", "https://dev.fluentcart.com/database/models/order-promotion-stat.html"),
    ("UserMeta", "https://dev.fluentcart.com/database/models/user-meta.html")
]

# Define URLs for REST API endpoints
REST_API_URLS = [
    ("Orders", "https://dev.fluentcart.com/restapi/orders.html"),
    ("Products", "https://dev.fluentcart.com/restapi/products.html"),
    ("Customers", "https://dev.fluentcart.com/restapi/customers.html"),
    ("Coupons", "https://dev.fluentcart.com/restapi/coupons.html"),
    ("Subscriptions", "https://dev.fluentcart.com/restapi/subscriptions.html"),
    ("Tax", "https://dev.fluentcart.com/restapi/tax.html"),
    ("Shipping", "https://dev.fluentcart.com/restapi/shipping.html"),
    ("Settings", "https://dev.fluentcart.com/restapi/settings.html"),
    ("Email Notifications", "https://dev.fluentcart.com/restapi/email-notifications.html"),
    ("Reports", "https://dev.fluentcart.com/restapi/reports.html"),
    ("Integrations", "https://dev.fluentcart.com/restapi/integrations.html"),
    ("Files", "https://dev.fluentcart.com/restapi/files.html"),
    ("Labels & Attributes", "https://dev.fluentcart.com/restapi/labels-and-attributes.html"),
    ("Dashboard", "https://dev.fluentcart.com/restapi/dashboard.html"),
    ("Public Shop", "https://dev.fluentcart.com/restapi/public-shop.html"),
    ("Checkout", "https://dev.fluentcart.com/restapi/checkout.html"),
    ("Customer Profile", "https://dev.fluentcart.com/restapi/customer-profile.html"),
    ("Licensing", "https://dev.fluentcart.com/restapi/licensing.html"),
    ("Roles", "https://dev.fluentcart.com/restapi/roles.html"),
    ("Order Bumps", "https://dev.fluentcart.com/restapi/order-bumps.html")
]

def scrape_and_save_category(urls, output_filename, title, category_name):
    # Log progress for category start
    print(f"\n--- Scraping {title} ---")
    markdown_content = f"# {title}\n\nThis reference contains all FluentCart {category_name} details scraped from the developer documentation site.\n\n"
    
    # Process each page in the list
    for name, url in urls:
        # Fetch the content of page
        content = fetch_and_convert(url)
        if content:
            # Clean up page-level title tags to avoid multiple top-level h1 tags
            content = re.sub(r'^# .*\n', '', content)
            markdown_content += f"## {name}\n\nSource: {url}\n\n{content}\n\n---\n\n"
        # Pause slightly to avoid overloading site
        time.sleep(0.5)
        
    # Write aggregated markdown to destination file
    output_path = os.path.join(REF_DIR, output_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    # Log completion info
    print(f"Saved: {output_path}")

def main():
    # 1. Scrape action hooks
    scrape_and_save_category(ACTION_HOOKS_URLS, "hooks-actions-reference.md", "Action Hooks Reference", "actions")
    
    # 2. Scrape filter hooks
    scrape_and_save_category(FILTER_HOOKS_URLS, "hooks-filters-reference.md", "Filter Hooks Reference", "filters")
    
    # 3. Scrape database models
    scrape_and_save_category(DATABASE_MODELS_URLS, "database-models-reference.md", "Database Models Reference", "models")
    
    # 4. Scrape REST API endpoints
    scrape_and_save_category(REST_API_URLS, "rest-api-reference.md", "REST API Endpoints Reference", "endpoints")

    # 5. Scrape Paddle gateway case study details separately
    print("\n--- Scraping Paddle Gateway details ---")
    paddle_content = fetch_and_convert("https://dev.fluentcart.com/payment-methods-integration/paddle-example.html")
    fields_content = fetch_and_convert("https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields.html")
    
    # Check and save Paddle example data
    if paddle_content or fields_content:
        # Define Paddle case study file output path
        paddle_path = os.path.join(REF_DIR, "paddle-gateway-case-study.md")
        with open(paddle_path, "w", encoding="utf-8") as f:
            f.write("# Paddle Payment Gateway Case Study\n\n")
            if fields_content:
                f.write("## Settings Field Schema Reference\n\n" + fields_content + "\n\n---\n\n")
            if paddle_content:
                f.write("## Paddle Core Implementation Detail\n\n" + paddle_content)
        # Log successful save of Paddle case study
        print(f"Saved: {paddle_path}")

if __name__ == "__main__":
    main()
