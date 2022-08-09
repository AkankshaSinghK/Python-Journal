""" Write a Python program to count the number of lines in a file. """

def count_lines(file_name):
    with open(file_name, 'r') as f:
        return len(f.readlines())


if __name__ == "__main__":
  print(count_lines("./4.py"))
