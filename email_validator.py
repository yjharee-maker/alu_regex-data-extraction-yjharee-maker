#!/usr/bin/env python3
import re

def confirm_email(email):
    # Validate email address using regex
    validate_email = re.match(r'^[a-z0-9._+-]+@[a-z0-9.-]+\.[a-z]{2,}$', email)
    if validate_email is not None:
        return True
    else:
        return False