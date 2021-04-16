import termcolor
import colorama

colorama.init(strip="False")
print("To server:", end="")
print(termcolor.colored("Message", "Yellow"))

count_bases = ""
    for base, count in seq_info.count().items():
        bases_info = str(base) + ": " + str(count) + " (" + str(
            round(count / seq_info.len() * 100, 2)) + "%)" + "\n"
        count_bases += bases_info

    response = "Sequence: " + str(seq_info) + "\n" +
                "Total length: " + str(seq_info.len()) + "\n" +
                count_bases
    print(response)
    cs.send(str(response).encode())

response = "\n" + "Sequence " + str(arg) + "\n" + "Lenght " + str(len(arg))
    print(response)
    cs.send(str(response).encode())