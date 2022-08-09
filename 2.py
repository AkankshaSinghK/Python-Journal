# function to check if a number is odd, even or prime
def check_number(number):
    if number % 2 == 0:
        print("Even")
    elif number % 2 == 1:
        print("Odd")
    if number == 2:
        print("Prime")
    else:
        for i in range(2, number):
            if number % i == 0:
                print("Not Prime")
                break
            else:
                print("Prime")
                break

if __name__ == "__main__":
    print(check_number(int(input("Enter a number: "))))
