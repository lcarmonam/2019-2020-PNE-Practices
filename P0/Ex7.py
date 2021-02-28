import Seq0

FOLDER = "./sequences/"
ID = "U5.txt"

U5_Seq = Seq0.seq_read_fasta(FOLDER + ID)
fragment = U5_Seq[0:20]
print("-----| Exercise 7 |------ \nGene U5: \nFrag: " + str(fragment) + "\nComp: " + str(Seq0.seq_complement(fragment)))
