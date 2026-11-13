#!/usr/bin/env python
import re

def confirm_hashtag(hashtag):
    # Validate hashtag format using regex
    validate_hashtag = re.match(r'^#[a-zA-Z0-9_]+$', hashtag)
    if validate_hashtag is not None:
        return True
    else:
        return False