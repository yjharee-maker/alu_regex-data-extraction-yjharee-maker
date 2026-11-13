#!/usr/bin/env python3
from email_validator import confirm_email
from phone_no import confirm_phone_number
from creditcard_no import confirm_credit_card_number
from currency_amount import confirm_currency_amount
from hashtag import confirm_hashtag
from html_validator import confirm_html
from time_validator import confirm_time

def email_in_file(file):
    # Check for valid emails in file
    email_list = []
    for line in file:
        for word in line.split():
            word = word.strip(".,!?;:()[]{}<>")
            confirm = confirm_email(word)
            if confirm == True:
                email_list.append(word)
    return email_list

def phone_numbers_in_file(file):
    # Check for valid phone numbers in file
    phone_list = []
    for line in file:
        words = line.split()
        for i in range(len(words)):
            for j in range(i + 1, len(words) + 1):
                word = " ".join(words[i:j])
                word = word.strip(".,!?;:[]{}<>")
                if confirm_phone_number(word) == True:
                    if word not in phone_list:
                        phone_list.append(word)
    return phone_list

def credit_cards_in_file(file):
    # Check for valid credit card numbers in file
    credit_card_list = []
    for line in file:
        words = line.split()
        for i in range(len(words)):
            for j in range(i + 1, len(words) + 1):
                word = " ".join(words[i:j])
                word = word.strip(".,!?;:()[]{}<>")
                confirm = confirm_credit_card_number(word)
                if confirm == True:
                    if word not in credit_card_list:
                        credit_card_list.append(word)
    return credit_card_list

def currency_amounts_in_file(file):
    # Check for valid currency amounts in file
    currency_list = []
    for line in file:
        for word in line.split():
            word = word.strip(".,!?;:()[]{}<>")
            confirm = confirm_currency_amount(word)
            if confirm == True:
                currency_list.append(word)
    return currency_list

def hashtags_in_file(file):
    # Check for valid hashtags in file
    hashtag_list = []
    for line in file:
        for word in line.split():
            word = word.strip(".,!?;:()[]{}<>")
            confirm = confirm_hashtag(word)
            if confirm == True:
                hashtag_list.append(word)
    return hashtag_list

def html_in_file(file):
    # Check for valid HTML tags in file
    html_list =[]
    for line in file:
        words = line.split()
        for i in range(len(words)):
            for j in range(i + 1, len(words) + 1):
                word = " ".join(words[i:j])
                confirm = confirm_html(word)
                if confirm == True:
                    if word not in html_list:
                        html_list.append(word)
    return html_list

def time_in_file(file):
    # Check for valid time formats in file
    time_list = []
    for line in file:
        words = line.split()
        for i in range(len(words)):
            for j in range(i + 1, len(words) + 1):
                word = " ".join(words[i:j])
                word = word.strip(".,!?;:()[]{}<>")
                confirm = confirm_time(word)
                if confirm == True:
                    if word not in time_list:
                        time_list.append(word)
    return time_list

if __name__ == "__main__":
    with open(input("Enter the file name: "), "r") as file:
        # Read the file and extract valid data
        email_list = email_in_file(file)
        file.seek(0)
        phone_list = phone_numbers_in_file(file)
        file.seek(0)
        credit_card_list = credit_cards_in_file(file)
        file.seek(0)
        hashtag_list = hashtags_in_file(file)
        file.seek(0)
        currency_list = currency_amounts_in_file(file)
        file.seek(0)
        html_list = html_in_file(file)
        file.seek(0)
        time_list = time_in_file(file)
    with open("valid_emails.txt", "w") as output_file:
        # Write valid emails to output file
        for email in email_list:
            output_file.write(email + "\n")
    with open("valid_phone_numbers.txt", "w") as output_file:
        # Write valid phone numbers to output file
        for phone in phone_list:
            output_file.write(phone + "\n")
    with open("valid_credit_cards.txt", "w") as output_file:
        # Write valid credit card numbers to output file
        for credit_card in credit_card_list:
            output_file.write(credit_card + "\n")
    with open("valid_currency_amounts.txt", "w") as output_file:
        # Write valid currency amounts to output file
        for currency in currency_list:
            output_file.write(currency + "\n")
    with open("valid_hashtags.txt", "w") as output_file:
        # Write valid hashtags to output file
        for hashtag in hashtag_list:
            output_file.write(hashtag + "\n")
    with open("valid_html.txt", "w") as output_file:
        # Write valid HTML tags to output file
        for html in html_list:
            output_file.write(html + "\n")
    with open("valid_time.txt", "w") as output_file:
        # Write valid time formats to output file
        for times in time_list:
            output_file.write(times + "\n")