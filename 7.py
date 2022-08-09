# decorator to calculate factorial from square root
def factorial(func):
    def inner(num):
        fact = 1
        for i in range(1, int(func(num))+1):
            fact *= i
        return fact
    return inner


def square_root(func):
    def inner(num):
        sqr = num**0.5
        return sqr
    return inner


@factorial
@square_root
def sqrt_then_factorial(num):
    return num


if __name__ == "__main__":
    print(sqrt_then_factorial(25))
