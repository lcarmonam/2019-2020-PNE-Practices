import http.server
import socketserver
import termcolor
from pathlib import Path
import pathlib
import json
import http.client

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content


PORT = 8080
SERVER = "rest.ensembl.org"
PARAMETERS = "?content-type=application/json"
connection = http.client.HTTPConnection(SERVER)


def info_species(inf):
    try:
        connection.request("GET", inf)  # asking for connection
    except ConnectionRefusedError:
        print(f"Connection refused: {SERVER}:{PORT}")
        exit()
    response = connection.getresponse()
    decoded = json.loads(response.read().decode())
    return decoded


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        try:

            termcolor.cprint(self.requestline, 'green')
            request_line = self.requestline.split(' ')
            print(request_line)
            path = request_line[1]
            print(path)
            # used to delete the interrogation mark.
            data = path.split('?')  # split separates the content from the '?'
            print(data)
            data_1 = data[0]  # This is the content before interrogation mark.
            print(data_1)

            # reads the index from the file
            contents = Path('Error.html').read_text()  # opens the error.html file

            try:
                if data_1 == "/":  # Opens the index.html file
                    contents = Path("index.html").read_text()  # Reads the index from the fil

                # -----PART 1: LIST OF SPECIES----

                elif data_1 == "/listSpecies":
                    ENDPOINT = "info/species"  # this endpoint returns Ok
                    species = info_species(ENDPOINT + PARAMETERS)["species"]  # we use the FUNCTION to read the content of the list
                    data_2 = data[1]  # Stores the information after the '?'
                    print(data_2)
                    data_3 = data_2.split("=")[1]  # Stores the information after the '='
                    print(data_3)

                    try:
                        if data_3 == "":  # if the limit if empty, our application will print all 267 species
                                contents = f"""
                                            <!DOCTYPE html>
                                            <html lang="en">
                                            <head>
                                                <meta charset="utf-8">
                                                <title>LIST OF SPECIES IN THE BROWSER</title>
                                            </head>
                                            <body style="background-color: lightgreen">
                                            <h1>List of Species in the browser</h1>
                                            <p><a href="/">Main page</a></p>
                                                <p>Total number of species is: 267 </p>
                                                <p>The limit you have selected is: {267}</p>
                                                <p>The names of the species are:</p>
                                                """
                                for element in species:  # We create a for to list all tipe of species when the limit is empty
                                    contents += f"""<p>{element["display_name"]} </p></body></html>"""

                        elif int(data_3) > 267:
                            contents = Path('Error.html').read_text()

                        elif int(data_3) < 0:
                            contents = Path('Error.html').read_text()

                        else:  # Now the application will print the name of spècies selected in the limit.ex 10,11...
                            contents = f"""
                                            <!DOCTYPE html>
                                            <html lang="en">
                                            <head>
                                                <meta charset="utf-8">
                                                <title>LIST OF SPECIES IN THE BROWSER</title>
                                            </head>
                                            <body style="background-color: lightgreen">
                                            <h1>List of Species in the browser</h1>
                                            <p><a href="/">Main page</a></p>
                                                <p>Total number of species is: 267 </p>
                                                <p>The limit you have selected is: {data_3}</p>
                                                <p>The names of the species are:</p>
                                            """

                            for element in species[:int(data_3)]:
                                contents += f"""<p>{element["common_name"]} </p></body></html>"""
                    except ValueError:
                        contents = Path('Error.html').read_text()

                # ------PART 2: KARYOTYOPE-------

                elif data_1 == "/karyotype":
                    endpoint = "info/assembly/"  # this endpoint returns Ok
                    data_2 = data[1]  # Stores the information after the '?'
                    data_3 = data_2.split("=")[1]
                    print(data_3)
                    species = info_species(endpoint + data_3 + PARAMETERS)["karyotype"]
                    print(species)

                    # the console will print the number of chromosomes of the specie selected in the limit
                    contents = f"""                             
                                   <!DOCTYPE html>
                                   <html lang="en">
                                   <head>
                                        <meta charset="utf-8">
                                        <title>KARYOTYPE OF A SPECIFIC SPECIES</title>
                                    </head>
                                    <body style="background-color: lightgreen">
                                    <h1>Karyotype</h1>
                                    <p><a href="/">Main page</a></p>
                                    <p>The name of the chromosomes are:</p>
                                    """
                    for element in species:
                        contents += f"""<p>{element} </p></body></html>"""

                # ---------PART 3: CHROMOSOME LENGTH------

                elif data_1 == "/chromosomeLength":
                    endpoint = "/info/assembly/"
                    data_2 = data[1]
                    print(data_2)
                    data_3, data_4 = data_2.split("&")
                    specie = data_3.split("=")[1]
                    print(specie)
                    chromosome = data_4.split("=")[1]
                    print(chromosome)
                    print(info_species(endpoint + specie + PARAMETERS))
                    species = info_species(endpoint + specie + PARAMETERS)["top_level_region"]
                    print(species)


                    for option in species:
                        print(option)
                        if option["name"] == chromosome:
                            contents = f"""
                                           <!DOCTYPE html>
                                           <html lang="en">
                                           <head>
                                                <meta charset="utf-8">
                                                <title>LENGHT OF THE SELECTED CHROMOSOME</title>
                                           </head>
                                           <body style="background-color: lightgreen">   
                                           <h1>Chromosome lenght</h1>
                                           <p><a href="/">Main page</a></p>
                                              <p>The length of the Chromosome is: {option["length"]}</p>
                                           </body>
                                           </html>"""
                else:
                    contents = Path('Error.html').read_text()

            except KeyError:
                contents = Path('Error.html').read_text()

        except KeyboardInterrupt:
            contents = Path('Error.html').read_text()

        self.send_response(200)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
