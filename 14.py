#  Write a python program for Integer Input Validation with Exception Handling (Example of ValueError Exception).

try:
    n = int(input("Enter a number: "))
    print(f"You entered {n}")
except ValueError:
    print("Invalid input")
except Exception as e:
    print(e)
