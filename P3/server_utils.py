from Seq1 import Seq

def print_colored(message, color):
    import termcolor
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping(cs):
    print_colored("PING command!", "green")
    response = "OK!"
    cs.send(str(response).encode())

def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(response.encode())

def comp(cs, argument):
    print_colored("COMP", "yellow")
    comp_seq = Seq(argument)
    response = comp_seq.complement()
    print(response)
    cs.send(response.encode())

def rev(cs, argument):
    print_colored("REV", "yellow")
    rev_seq = Seq(argument)
    response = rev_seq.reverse()
    print(response)
    cs.send(response.encode())


def info(cs, arg):
    print_colored("INFO", "yellow")
    seq_info = Seq(arg)
    lenght = len(arg)
    count_bases = ""
    for base, count in seq_info.count().items():
        bases_info = str(base) + ": " + str(count) + " (" + str(round(count / lenght * 100, 1)) + "%)" + "\n"
        count_bases += bases_info
    response = ("Sequence: " + str(arg) + "\n" + "Total length: " + str(lenght) + "\n" + count_bases)
    print(response)
    cs.send(str(response).encode())



