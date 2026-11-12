#!/usr/bin/env python3
from email_validator import confirm_email
def email_in_file(file):
    email_list = []
    for line in file:
        for word in line.split():
            word = word.strip(".,!?;:()[]{}<>")
            confirm = confirm_email(word)
            if confirm == True:
                email_list.append(word)
    return email_list
if __name__ == "__main__":
    with open(input("Enter the file name: "), "r") as file:
        email_list = email_in_file(file)
    with open("valid_emails.txt", "w") as output_file:
        for email in email_list:
            output_file.write(email + "\n")