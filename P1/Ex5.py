from Seq1 import Seq

def print_result(i, sequence):
    print("Sequence" + str(i) + ": (lenght:" + str(sequence.len()) + ") " + str(sequence))
    a, c, g, t = sequence.count_bases()
    print("A: " + str(a) + ", C: " + str(c) + ", T: " + str(t) + ", G: " + str(g))

print("-----| Practice 1, Exercise 5 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid Sequence")

list_seq = [s1, s2, s3]
for i in range(0, len(list_seq)):
    print_result(i, list_seq[i - 1])