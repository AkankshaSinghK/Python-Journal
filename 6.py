
def is_armstrong(num):
    sum = 0
    for i in str(num):
        sum += int(i)**3
    return sum == num


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_armstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")
