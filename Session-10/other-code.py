import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.253.130"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))
count_connections = 0

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")


# -- Waits for a client to connect
print("Waiting for Clients to connect")
ls.accept()

client_address_list = []
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION" + str(count_connections) + ": Client IP, PORT: " + )
    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
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

        # -- Print the received message
        print(f"Message received: {msg}")

        # -- Send a response message to the client
        try:
            response = int(msg) ** int(msg)
            print("Response", response)
            # --The message has to be encoded into bytes
            cs.send(str(response).encode())
        except ValueError:
            cs.send("We need a number".encode())

        # -- Close the data socket
        cs.close()
        if count_connections == 5:
            for i in range(0, len(client_adress_list)):
                print("Client" + str(i) + ": Client IP, PORT: " + str(client_address_list[i]))
                exit(0)
