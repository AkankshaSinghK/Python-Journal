# Write a Python program to create a new file in another directory.

import os

try:
    os.mkdir("new_dir")
except FileExistsError:
    print("Directory already exists")
else:
    print("Directory created")

    with open("new_dir/new_file.txt", "w") as f:
        f.write("Hello World")

