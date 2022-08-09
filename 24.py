""" Write a python program to create and delete theread """

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n
    
    def run(self):
        print(f"Hi, I am {self.n} and I am going to sleep for {self.n} seconds")
        time.sleep(self.n)
        print(f"{self.n} has woken up")

print("In main program")
thread1 = MyThread(1)
thread1.daemon = True
thread1.start()
time.sleep(5)
print("End of main program")

