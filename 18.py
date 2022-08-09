# Write a program to Copy contents from one file to another file in Python.

def copy_file(src, dst):
    with open(src, 'r') as f:
        with open(dst, 'w') as f1:
            for line in f:
                f1.write(line)
    return


if __name__ == '__main__':
    copy_file('2/18.py', '2/18_copy.py')
