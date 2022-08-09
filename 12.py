# python program to validate email id using Regular Expression
import re


def validate_email(email):
    pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.match(pattern, email):
        return True
    return False


if __name__ == "__main__":
    email = input("Enter an email: ")
    if validate_email(email):
        print("Valid email")
    else:
        print("Invalid email")
