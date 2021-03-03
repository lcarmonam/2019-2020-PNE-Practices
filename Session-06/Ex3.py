
print("New sequence created!")


def len_(seq_list):
    return len(seq_list)

def generate_seqs(seq, number):
    list_created = []
    for a in range(0, number):
        list_created.append(seq + seq * a)
    return list_created

def print_seqs(seq_list):
    for sequence in range(0, len(seq_list)):
        print(f"Sequence {sequence} (length: {len_(seq_list[sequence])}) {seq_list[sequence]}")


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)