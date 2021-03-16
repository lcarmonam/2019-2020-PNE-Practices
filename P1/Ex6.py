import Seq1

def print_result(i, sequence):
    print("Sequence " + str(i) + ": (lenght:" + str(sequence.len()) + ") " + str(sequence))
    print("Bases:", sequence.count())


print(print("-----| Practice 1, Exercise 6 |------"))
list_sequences = list(Seq1.test_sequences())
for i in range(0, len(list_sequences)):
    print_result(1, list_sequences[i])
