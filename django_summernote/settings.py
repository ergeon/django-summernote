ALLOWED_TAGS = [
    'a', 'div', 'p', 'span', 'img', 'em', 'i', 'li', 'ol', 'ul', 'strong', 'br',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'table', 'tbody', 'thead', 'tr', 'td',
    'abbr', 'acronym', 'b', 'blockquote', 'code', 'strike', 'u', 'sup', 'sub',
]

# In bleach 6.x+, styles are handled as attributes
STYLES = [
    'background-color', 'font-size', 'line-height', 'color', 'font-family'
]

ATTRIBUTES = {
    '*': ['style', 'align', 'title', ],
    'a': ['href', ],
    # Add style attributes for bleach 6.x compatibility
    'span': {'style': STYLES},
    'p': {'style': STYLES},
    'div': {'style': STYLES},
}
