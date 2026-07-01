import os
import re

# Resolve references directory path relative to this script
REF_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "references"))

# Define base URL mapping prefixes for relative link conversion
MAPPINGS = [
    ("database-models-reference.md", "https://dev.fluentcart.com/database/models/"),
    ("hooks-actions-reference.md", "https://dev.fluentcart.com/hooks/actions/"),
    ("hooks-filters-reference.md", "https://dev.fluentcart.com/hooks/filters/"),
    ("rest-api-reference.md", "https://dev.fluentcart.com/restapi/"),
    ("paddle-gateway-case-study.md", "https://dev.fluentcart.com/payment-methods-integration/"),
]

def fix():
    # Loop over all mappings to fix relative links in each scraped reference file
    for filename, base_url in MAPPINGS:
        path = os.path.join(REF_DIR, filename)
        if not os.path.exists(path):
            continue
            
        print(f"Fixing links in {filename}...")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Inline helper function to resolve relative markdown links
        def replace_link(match):
            label = match.group(1)
            url = match.group(2)
            
            # Check if it is a relative link (does not start with http, mailto, or # anchor)
            if not url.startswith("http") and not url.startswith("mailto") and not url.startswith("#"):
                clean_url = url
                url_prefix = base_url
                
                # Strip parent directories and adjust target absolute URL base
                while clean_url.startswith("../"):
                    clean_url = clean_url[3:]
                    parts = url_prefix.rstrip('/').split('/')
                    if len(parts) > 3:
                        url_prefix = "/".join(parts[:-1]) + "/"
                        
                # Strip current directory dot prefixes
                if clean_url.startswith("./"):
                    clean_url = clean_url[2:]
                    
                fixed_url = url_prefix + clean_url
                print(f"  Fixed: [{label}]({url}) -> [{label}]({fixed_url})")
                return f"[{label}]({fixed_url})"
                
            return match.group(0)
            
        # Match and replace all standard markdown links using the regex matcher
        fixed_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(fixed_content)

if __name__ == "__main__":
    fix()
