# function to check if number is positive negative or zero
def check_number(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


if __name__ == "__main__":
    print(check_number(int(input("Enter a number: "))))
