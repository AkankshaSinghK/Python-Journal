# Write a Python Program for Raising User Generated Exception.

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise Exception("Number is less than 0")
    print(num)
except Exception as e:
    print(e)
finally:
    print("Program completed")
