import Seq0

GENE_FOLDER = "./sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "T", "G"]

unique = list(set(base_list))
print(unique)
values = [unique[0], unique[1]]
solution_one = base_list.count(unique[0])
solution_two = base_list.count(unique[1])
print(unique, solution_one, solution_two)

print("-----| Exercise 8 |------")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    sequence_list = list(sequence)
    unique = list(set(sequence_list))
    print(sequence_list.count(unique[0]))
    print("Gene" + str(gene) + ": Most frequent Base:")

