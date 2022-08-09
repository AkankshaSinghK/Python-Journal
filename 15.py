""" Write a program for IndexError Exception in Python with Example """

try:
    list = [1, 2, 3, 4, 5]
    # print the element at index 5
    print(list[5])
except IndexError:
    print("IndexError Exception")
except Exception:
    print("Exception")
else:
    print("No exception")
