from Seq1 import test_sequences


def print_result(i, sequence):
    print("Sequence " + str(i) + ": (lenght:" + str(sequence.len()) + ") " + str(sequence))
    print("Bases:", sequence.count())
    print("Rev:", sequence.reverse())
    print("Complement:", sequence.complement())


print(print("-----| Practice 1, Exercise 8 |------"))
list_sequences = list(test_sequences())
for i in range(0, len(list_sequences)):
    print_result(1, list_sequences[i])