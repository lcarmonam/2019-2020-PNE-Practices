import termcolor
from pathlib import Path

def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid Sequence")
    return s1, s2, s3

class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, strbases=NULL_SEQUENCE):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if strbases == Seq.NULL_SEQUENCE:
            print("NULL Seq created")
            self.strbases = strbases
        else:
            if self.is_valid_sequence():
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INCORRECT Sequence detected")

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = "Sequence" + str(i) + ": (lenght:" + str(list_sequences[i].len()) + ")" + str(list_sequences[i])
            termcolor.cprint(text, "yellow")


    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases =="NULL" or self.strbases == "Error":
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a = 0
        c = 0
        t = 0
        g = 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, g, t
        else:
            for i in self.strbases:
                if i == "A":
                    a += 1
                elif i == "C":
                    c += 1
                elif i == "G":
                    g += 1
                elif i == "T":
                    t += 1
            return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        return {"A": a, "C": c, "G": g, "T": t}

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            complement = ""
            for i in self.strbases:
                if i == "A":
                    complement += "T"
                elif i == "C":
                    complement += "G"
                elif i == "G":
                    complement += "C"
                elif i == "T":
                    complement += "A"
            return complement

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def seq_read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())


    def frequent_base(self):
        a, c, g, t = self.count_bases()
        values_list = []
        result = {"A": a, "C": c, "G": g, "T": t}
        for key,value in result.items():
            values_list.append(value)
            higher = max(values_list)
            if a == higher:
                answer = "A"
            elif c == higher:
                answer = "C"
            elif g == higher:
                answer = "G"
            elif t == higher:
                answer = "T"
        return answer






