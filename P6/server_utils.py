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

def info(arg, operation):
    seq_info = Seq(arg)
    lenght = len(arg)
    count_bases = ""
    for base, count in seq_info.count().items():
        bases_info = str(base) + ": " + str(count) + " (" + str(round(count / lenght * 100, 1)) + "%)" + "\n"
        count_bases += bases_info
    calculation = ("Sequence: " + str(arg) + "\n" + "Total length: " + str(lenght) + "\n" + count_bases)
    context = {
        "operation_name": operation,
        "operation_contents": arg,
        "operation_calculation": calculation
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents

def comp(sequence):
    comp_seq = Seq(sequence)
    context = {
        "operation_contents": sequence,
        "operation_name": "Comp",
        "operation_result": comp_seq.complement()
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def rev(sequence):
    rev_seq = Seq(sequence)
    context = {
        "operation_contents": sequence,
        "operation_name": "Rev",
        "operation_result": rev_seq.reverse()
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents

def gene(argument):
    sequence = Seq()
    sequence.seq_read_fasta("./sequences/" + argument + ".txt")
    context = {
        "gene_name": argument,
        "gene_contents": sequence.strbases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents





