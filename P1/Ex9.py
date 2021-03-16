from Seq1 import Seq


def print_result(i, sequence):
    print("Sequence " + str(i) + ": (lenght:" + str(sequence.len()) + ") " + str(sequence))
    print("Bases:", sequence.count())
    print("Rev:", sequence.reverse())
    print("Complement:", sequence.complement())


print("-----| Practice 1, Exercise 9 |------")
s1 = Seq()
s1.seq_read_fasta("ADA.txt")
print_result("", s1)

for gene in gene_list:
    s1.seq_read_fasta(gene + ".txt")
    print_result(s1)