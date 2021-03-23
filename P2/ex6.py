from Client0 import Client
from pathlib import Path
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 12000
IP = "212.128.253.139"
c = Client(IP, PORT)

s = Seq()
s.seq_read_fasta("FRAT1.txt")
count = 0
i = 0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i: i + 10]
    count += 1
    i += 10
    print("Fragment", count, ":", fragment)
    print(c.talk(fragment))