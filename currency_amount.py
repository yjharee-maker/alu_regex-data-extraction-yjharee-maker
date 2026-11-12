#!/usr/bin/env python
import re

def confirm_currency_amount(currency_amount):
    validate_currency = re.match(r'^\$?\d{1,3}(,\d{3})*(\.\d{2})?$', currency_amount)
    if validate_currency is not None:
        return True
    else:
        return False