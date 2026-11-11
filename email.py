#!/usr/bin/envr python3
import re

def confirm_email(email):
    validate_email = re.match(r'^[a-z0-9._%+-]+@[a-z.-]+\.[a-z]{2,}$', email)
    if validate_email is not None:
        print("email is valid")
        x = True
        return x
    else:
        print("email is invalid. Please enter a valid email address.")
        x = False
        return x

if __name__ == "__main__":
    x = False
    while x == False:
        email = input("Enter an email:")
        x = confirm_email(email)
    
