import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
import os


class UserInfo:
    def __init__(self, name,phone):
        self.name = name
        self.phone = phone
    def print_info(self):
        print("-----------------")
        print("Name :" + self.name)
        print("phone :" + self.phone)
        print("-----------------")

    def __del__(self):
        print("Del!!")


user1 = UserInfo("Kim","010-111-1111")
user2 = UserInfo("Park","000-2222")


# user1.set_info("Kim","010-111-1111")
# user2.set_info("Park","000-2222")

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone,user1.name)
