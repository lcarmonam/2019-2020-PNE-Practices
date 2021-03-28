import colorama
from colorama import Fore
from Client0 import Client


PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 12000
IP = "212.128.253.130"
c = Client(IP, PORT)

colorama.init()
answer_one = c.debug_talk(Fore.BLUE + "Message 1---")
print(Fore.YELLOW + answer_one)
answer_two = c.debug_talk(Fore.BLUE + "Message 2: Testing !!!")
print(Fore.YELLOW + answer_two)




