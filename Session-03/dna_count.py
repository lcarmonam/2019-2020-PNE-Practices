def correct_sequence(dna):
    for c in dna:
        if c != "A" and c != "G" and c != "C" and c != "T":
            return False
    return True


def count_bases(dna):
    a = 0
    c = 0
    t = 0
    g = 0
    for i in dna:
        if i == "A":
            a += 1
        elif i == "C":
            c += 1
        elif i == "G":
            g += 1
        else:
            t += 1
    return a, c, g, t

dna = input("Introduce the sequence: ")
correct_dna = correct_sequence(dna)
if correct_dna:
    print("Total lenght: ", len(dna))
    a, c, g, t = count_bases(dna)
    print("A", a)
    print("C", c)
    print("T", t)
    print("G", g)
else:
    print("Not a valid dna sequence")


