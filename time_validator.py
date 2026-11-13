#!/usr/bin/env python
import re

def confirm_time(name):
    # Validate time using regex
    validate_time = re.match(r'^(?:(?:[01]\d|2[0-3]):[0-5]\d|(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:[aApP]\.?[mM]\.?))$', name)
    if validate_time is not None:
        return True
    else:
        return False