# Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter.

def add_it_up(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
  
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("The sum of the integers from zero to", n, "is", add_it_up(n))
