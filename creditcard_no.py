#!/usr/bin/env python
import re

def confirm_credit_card_number(credit_card_number):
    validate_credit_card = re.match(r'^\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$', credit_card_number)
    if validate_credit_card is not None:
        return True
    else:
        return False
