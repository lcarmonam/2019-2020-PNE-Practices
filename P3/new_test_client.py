from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8090
first_sequence = "TGTGAACATTCTGCGCTGCGCCTGGGCGGGTTTCTT"
c = Client(IP, PORT)
print(c)

print("* Testing PING...")
print(c.talk("PING"))

print("* Testing GET...")
print("GET 0:", c.talk("GET 0"))
print("GET 1:", c.talk("GET 1"))
print("GET 2:", c.talk("GET 2"))
print("GET 3:", c.talk("GET 3"))
print("GET 4:", c.talk("GET 4"))

print("* Testing INFO...")
print(c.talk("INFO " + first_sequence))

print("* Testing COMP...")
print("COMP " + first_sequence)
print(c.talk("COMP " + first_sequence))

print("* Testing REV...")
print("REV " + first_sequence)
print(c.talk("REV " + first_sequence))

print("* Testing GENE...")
file_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in file_list:
    print("GENE", gene)
    print(c.talk("GENE " + gene))