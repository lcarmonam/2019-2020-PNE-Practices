from Seq1 import Seq

gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]


def print_result(sequence):
        print("Gene " + str(gene) + ": Most frequent Base: " + str(sequence.frequent_base()))


print("-----| Practice 1, Exercise 10 |------")
s1 = Seq()
for gene in gene_list:
    s1.seq_read_fasta(gene + ".txt")
    print_result(s1)



