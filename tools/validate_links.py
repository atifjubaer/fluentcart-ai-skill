import os
import re

# Resolve directories relative to this script
SKILL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REF_DIR = os.path.join(SKILL_DIR, "references")

def find_links(text):
    # Find all standard markdown links format [text](url)
    return re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)

def validate():
    has_errors = False
    
    # Validate the main SKILL.md index file links
    skill_path = os.path.join(SKILL_DIR, "SKILL.md")
    print(f"Validating main skill file: {skill_path}...")
    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    for label, url in find_links(content):
        # Only validate local relative paths (not external web links)
        if not url.startswith("http") and not url.startswith("mailto"):
            # Normalize target file path ignoring anchor links
            target_path = os.path.abspath(os.path.join(SKILL_DIR, url.split("#")[0]))
            if not os.path.exists(target_path):
                print(f"  [ERROR] Broken link: [{label}]({url}) -> Resolved to: {target_path}")
                has_errors = True
                
    # Validate links inside all the individual guide markdown files
    for filename in os.listdir(REF_DIR):
        if filename.endswith(".md"):
            ref_path = os.path.join(REF_DIR, filename)
            with open(ref_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            for label, url in find_links(content):
                # Only check relative local paths
                if not url.startswith("http") and not url.startswith("mailto"):
                    # Resolve relative targets from the references folder context
                    target_path = os.path.abspath(os.path.join(REF_DIR, url.split("#")[0]))
                    if not os.path.exists(target_path):
                        print(f"  [ERROR] Broken link in {filename}: [{label}]({url}) -> Resolved to: {target_path}")
                        has_errors = True
                        
    # Print final validation summary
    if not has_errors:
        print("\nSUCCESS: All local links verified successfully! No broken links found.")
    else:
        print("\nFAILURE: Some broken links were detected.")

if __name__ == "__main__":
    validate()
