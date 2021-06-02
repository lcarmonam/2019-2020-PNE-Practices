from Seq1 import Seq
from jinja2 import Template
import pathlib
import json
import http.client

PORT = 8080
SERVER = "rest.ensembl.org"
PARAMETERS = "?content-type=application/json"
connection = http.client.HTTPConnection(SERVER)


def print_colored(message, color):
    import termcolor
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content


def get_info(ENDPOINT):
    try:
        connection.request("GET", ENDPOINT + PARAMETERS)  # asking for connection
    except ConnectionRefusedError:
        print(f"Connection refused: {SERVER}:{PORT}")
        exit()
    response = connection.getresponse()
    decoded = response.read().decode("utf-8")
    data_decoded = json.loads(decoded)
    return data_decoded

def get_species(data_decoded,limit):
    print(data_decoded)
    list_species = []
    for element in range(0, int(limit)):
        data = data_decoded["species"]
        print(element)
        print(data[element]["display_name"])
        list_species.append(data[element]["display_name"])
        context = {
            "limit": limit,
            "species": list_species,
            "number": len(data)
        }
    contents = read_template_html_file("./html/species.html").render(context=context)
    return contents

def get_karyotype(karyo_data, specie):
    karyo = karyo_data["karyotype"]
    print(karyo)
    context = {
            "chromose_name": karyo,
            "specie": specie
    }
    contents = read_template_html_file("./html/karyotype.html").render(context=context)
    return contents

def get_chromosome_lenght(chromo_data, specie, chromosome):
    data = chromo_data["top_level_region"]
    for option in data:
        print(option)
        if option["name"] == chromosome:
            lenght = option["length"]
            context = {
                "chrmosome": chromosome,
                "specie": specie,
                "lenght": lenght
            }

    contents = read_template_html_file("./html/chromosome_lenght.html").render(context=context)
    return contents

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

def info(sequence):
    seq_info = Seq(sequence)
    lenght = len(sequence)
    count_bases = ""
    for base, count in seq_info.count().items():
        bases_info = str(base) + ": " + str(count) + " (" + str(round(count / lenght * 100, 1)) + "%)" + "\n"
        count_bases += bases_info
    calculation = ("Total length: " + str(lenght) + "\n" + count_bases)
    context = {
        "operation_contents": sequence,
        "operation_name": "Info",
        "operation_result": calculation
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





