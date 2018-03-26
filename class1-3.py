import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
import os

class SelfTest:
    def func1():
        print("func1 Called!!")
    def func2(self):
        print(id(self))
        print("func2 Called!!")


f = SelfTest()

# print(dir(f))

# f.func1()

print(id(f))
f.func2()

print(SelfTest.func1())
