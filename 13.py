# Write a python Program to validate Mobile no. using Regular expression.

import re


def validate_mobile(mobile):
    pattern = r'^[789]\d{9}$'
    if re.match(pattern, mobile):
        return True
    return False


if __name__ == "__main__":
    mobile = input("Enter a mobile number: ")
    if validate_mobile(mobile):
        print("Valid mobile number")
    else:
        print("Invalid mobile number")
