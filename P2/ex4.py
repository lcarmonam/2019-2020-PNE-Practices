import colorama
from colorama import Fore
from Client0 import Client


PRACTICE = 2
EXERCISE = 3


print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 12000
IP = "212.128.253.130"
c = Client(IP, PORT)

colorama.init()
response_one = c.talk(Fore.BLUE+ "Message 1---")

print(Fore.YELLOW + response_one)



