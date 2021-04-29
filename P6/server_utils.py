from Seq1 import Seq
import pathlib
from jinja2 import Template


def print_colored(message, color):
    import termcolor
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content

def ping(cs):
    print_colored("PING command!", "green")
    response = "OK!"
    cs.send(str(response).encode())

def get(list_sequences, seq_number):
    context = {
        "number": seq_number,
        "sequence": list_sequences[int(seq_number)]
    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents

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

def gene(argument):
    sequence = Seq()
    sequence.seq_read_fasta("./sequences/" + argument + ".txt")
    context = {
        "gene_name": argument,
        "gene_contents": sequence.strbases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents






