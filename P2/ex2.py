from Client0 import Client

PRACTICE = 2
EXERCISE = 2


print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 12000
IP = "212.128.253.130"
c = Client(IP, PORT)
print(c)