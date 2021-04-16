import socket
import server_utils

list_sequences = ["TGTGAACATTCTGCGCTGCGCCTGGGCGGGTTTCTT", "CAGGAGGGGACTGTCCGAGCTCCAGCCTTC",
            "CTCCCAGCTCCCTGGAGTCGTAGAATGTCCTCTCCACCCC", "GAACTCCTGCAGGTTCTGCAGGCCCTCGAAAGT",
            "CTGCAGGGGGACGCTTGAAAGGAGGAGCCGGGGGGAA"]
# Configure the Server's IP and PORT
PORT = 8091
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 3: Configure the socket for listening

count_connections = 0
ls.listen()
print("The server is configured!")
client_address_list = []

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)
        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()
        formatted_message = server_utils.format_command(msg)
        formatted_message = formatted_message.split(" ")
        if len(formatted_message) == 1:
            command = formatted_message[0]
        else:
            command = formatted_message[0]
            argument = formatted_message[1]

        if command == "PING":
            server_utils.ping(cs)

        elif command == "GET":
            server_utils.get(cs, list_sequences, argument)

        elif command == "INFO":
            server_utils.info(cs, argument)

        elif command == "COMP":
            server_utils.comp(cs, argument)

        elif command == "REV":
            server_utils.rev(cs, argument)

        elif command == "GENE":
            server_utils.gene(cs, argument)

        else:
            response = "Not available command"
            cs.send(str(response).encode())
        # -- Close the data socket
        cs.close()
