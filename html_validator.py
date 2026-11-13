#!/usr/bin/env python
import re

def confirm_html(name):
    # Validate HTML tag format using regex
    validate_html = re.match(r'^<([a-zA-Z][a-zA-Z0-9]*)\b[^>]*>(.*?)</\1>$', name)
    if validate_html is not None:
        return True
    else:
        return False