class Seq:

    def __init__(self, strbases):

        self.strbases = strbases

        for bases in strbases:
            if bases == "A" and bases == "C" and bases == "G" and bases == "T":
                print("New sequence created!")
            else:
                print("Error")

    def __str__(self):

        return self.strbases


    def len(self):

        return len(self.strbases)

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
s2 = Seq("Error")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")