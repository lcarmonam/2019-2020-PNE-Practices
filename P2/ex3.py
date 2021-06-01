from Client0 import Client

PRACTICE = 2
EXERCISE = 3


print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |-pyth-----")

PORT = 12000
IP = "212.128.253.141"
c = Client(IP, PORT)
response = c.talk("Hello I'm Lucia")
print("Response: ", response)