class Seq:

    def __init__(self, strbases):
        self.strbases = strbases


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

def print_seqs(seq_list):
    for sequence in range(0, len(seq_list)):
        answer = f"Sequence {sequence} (length: {seq_list[sequence].len()}) {seq_list[sequence]}"
        return answer

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print(print_seqs(seq_list))