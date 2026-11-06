#!/usr/bin/envr python
import re


class Email:

    def __init__(self, email):
        self.email = email

    def confirm_email(email):
        x = False
        while x is False:
            email = input("Enter your email address: ")
            validate_email = re.match(r'^[a-z0-9._%+-]+@[a-z.-]+\.[a-z]{2,}$', email)
            if validate_email is not None:
                print("email is valid")
                x = True
            else:
              print("email is invalid. Please enter a valid email address.")
              x = False

if __name__ == "__main__":
    email = None
    Email.confirm_email(email)

