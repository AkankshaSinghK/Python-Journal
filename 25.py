""" Write a Python program for multithreading with class. """

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n

    def run(self):
        print(f"Going to sleep for {self.n} seconds")
        time.sleep(self.n)
        print("running")

thread1 = MyThread(1)
thread2 = MyThread(2)

thread1.run()
thread2.run()
