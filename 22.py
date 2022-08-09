""" Write a Python program to demonstrate parameterized threads. """

import threading
import time


def sleeper(n, name):
    print(f"Hi, I am {name} and I am going to sleep for {n} seconds")
    time.sleep(n)
    print(f"{name} has woken up")


# Create new threads
thread1 = threading.Thread(target=sleeper, args=(1, "thread1"))
thread2 = threading.Thread(target=sleeper, args=(2, "thread2"))

thread1.start()
thread2.start()()
