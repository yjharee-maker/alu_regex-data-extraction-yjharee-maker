#!/usr/bin/env python
import re

def confirm_phone_number(phone_number):
    # Validate phone number format using regex
    validate_phone = re.match(r'^\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$', phone_number)
    if validate_phone is not None:
        return True
    else:
        return False