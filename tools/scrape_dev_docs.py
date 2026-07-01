import urllib.request
import re
import os
import time
from html.parser import HTMLParser

# Custom HTML parser to convert VitePress content to clean Markdown
class VitePressToMarkdownParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_doc = False  # Track if parser is inside the 'vp-doc' content container
        self.doc_div_depth = 0  # Keep track of nested divs to detect when exiting 'vp-doc'
        self.markdown_lines = []  # List to store converted markdown chunks
        self.current_tag = None  # Track the current active tag
        self.in_code = False  # Track if inside a <code> tag
        self.in_pre = False  # Track if inside a <pre> tag
        self.code_lang = ""  # Track the language of the code block
        self.list_depth = 0  # Track list nesting level
        self.table_headers = []  # Store headers for rendering tables properly
        self.in_table_head = False  # Track table header section
        self.table_cols_count = 0  # Count columns in current table row
        self.link_url = ""  # Store the active <a> tag URL
        self.in_link = False  # Track if inside a link tag

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Check if we enter the main VitePress document container
        if not self.in_doc:
            if tag == 'div' and 'class' in attrs_dict and 'vp-doc' in attrs_dict['class']:
                self.in_doc = True
                self.doc_div_depth = 1
            return

        # Keep track of nested div depth to ensure we exit at the right closing tag
        if tag == 'div':
            self.doc_div_depth += 1
            return

        self.current_tag = tag
        
        # Track code and pre tags for formatting code blocks
        if tag == 'pre':
            self.in_pre = True
            if 'class' in attrs_dict:
                lang_match = re.search(r'language-(\w+)', attrs_dict['class'])
                if lang_match:
                    self.code_lang = lang_match.group(1)
            self.markdown_lines.append(f"\n```{self.code_lang}\n")
            return
        elif tag == 'code':
            self.in_code = True
            if not self.in_pre:
                self.markdown_lines.append("`")
            return

        # Handle links
        if tag == 'a' and 'href' in attrs_dict:
            self.in_link = True
            self.link_url = attrs_dict['href']
            # Make relative links absolute if needed, or keep relative links intact
            if self.link_url.startswith('/'):
                self.link_url = "https://dev.fluentcart.com" + self.link_url
            self.markdown_lines.append("[")
            return

        # Convert layout tags to Markdown structures
        if tag == 'h1':
            self.markdown_lines.append("\n# ")
        elif tag == 'h2':
            self.markdown_lines.append("\n## ")
        elif tag == 'h3':
            self.markdown_lines.append("\n### ")
        elif tag == 'h4':
            self.markdown_lines.append("\n#### ")
        elif tag == 'p':
            self.markdown_lines.append("\n")
        elif tag in ['ul', 'ol']:
            self.list_depth += 1
            self.markdown_lines.append("\n")
        elif tag == 'li':
            indent = "  " * (self.list_depth - 1)
            self.markdown_lines.append(f"\n{indent}- ")
        elif tag == 'table':
            self.markdown_lines.append("\n")
        elif tag == 'thead':
            self.in_table_head = True
            self.table_cols_count = 0
        elif tag == 'tr':
            self.markdown_lines.append("\n| ")
            self.table_cols_count = 0
        elif tag == 'th':
            pass
        elif tag == 'td':
            pass
        elif tag == 'strong':
            self.markdown_lines.append("**")
        elif tag == 'em':
            self.markdown_lines.append("*")

    def handle_endtag(self, tag):
        if not self.in_doc:
            return

        # Handle exiting the main VitePress document container
        if tag == 'div':
            self.doc_div_depth -= 1
            if self.doc_div_depth == 0:
                self.in_doc = False
            return

        # Close code block tags
        if tag == 'pre':
            self.markdown_lines.append("```\n")
            self.in_pre = False
            self.code_lang = ""
            return
        elif tag == 'code':
            self.in_code = False
            if not self.in_pre:
                self.markdown_lines.append("`")
            return

        # Close link formatting
        if tag == 'a':
            self.in_link = False
            self.markdown_lines.append(f"]({self.link_url})")
            return

        # Close layout and table tags
        if tag in ['h1', 'h2', 'h3', 'h4']:
            self.markdown_lines.append("\n")
        elif tag in ['ul', 'ol']:
            self.list_depth -= 1
            self.markdown_lines.append("\n")
        elif tag == 'thead':
            self.in_table_head = False
            # Render the table divider row in markdown
            divider = "\n| " + " | ".join(["---"] * self.table_cols_count) + " |"
            self.markdown_lines.append(divider)
        elif tag in ['th', 'td']:
            self.markdown_lines.append(" | ")
            self.table_cols_count += 1
        elif tag == 'strong':
            self.markdown_lines.append("**")
        elif tag == 'em':
            self.markdown_lines.append("*")

    def handle_data(self, data):
        if not self.in_doc:
            return
        # Skip internal tags like script or style
        if self.current_tag in ['style', 'script']:
            return
        
        # Directly output code block contents
        if self.in_pre:
            self.markdown_lines.append(data)
            return

        # Clean whitespace and escape double asterisks if not formatted
        clean_data = re.sub(r'\s+', ' ', data)
        if clean_data:
            # Skip VitePress navigation anchor headers
            if clean_data.strip() in ['#', '\u200b', 'Permalink to']:
                return
            self.markdown_lines.append(clean_data)

    def get_markdown(self):
        text = "".join(self.markdown_lines)
        # Post-process cleanup of double linebreaks and spaces
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r' +', ' ', text)
        return text.strip()

# Function to fetch and convert a single page to Markdown
def fetch_and_convert(url):
    print(f"Fetching: {url}")
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
        parser = VitePressToMarkdownParser()
        parser.feed(html)
        return parser.get_markdown()
    except Exception as e:
        print(f"Error fetching/converting {url}: {e}")
        return ""
