# function to print multiplication table
def multiplication_table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)
    return


if __name__ == "__main__":
    multiplication_table(int(input("Enter a number: ")))
