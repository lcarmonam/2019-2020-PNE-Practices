from Client0 import Client

PRACTICE = 2
EXERCISE = 1


print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 12000
IP = "212.128.253.139"
c = Client(IP, PORT)
c.advanced_ping()
c.ping()
print(f"IP: {c.ip}, {c.port}")