from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 5


print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 12000
IP = "212.128.253.141"
c = Client(IP, PORT)
print(c.talk("Sending the US gene to the server..."))
print(c.talk(Path("U5.txt").read_text()))