import http.server
import socketserver
import termcolor
from pathlib import Path
import pathlib
import json
import http.client
from urllib.parse import urlparse, parse_qs

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

PORT = 8080
SERVER = "rest.ensembl.org"
PARAMETERS = "?content-type=application/json"
connection = http.client.HTTPConnection(SERVER)

DICT_GENES = {
"FRAT1": "ENSG00000165879",
"ADA": "ENSG00000196839",
"FXN": "ENSG00000165060",
"RNU6_269P": "ENSG00000212379",
"MIR633": "ENSG00000207552",
"TTTY4C": "ENSG00000226906",
"RBMY2YP": "ENSG00000227633",
"FGFR3": "ENSG00000068078",
"KDR": "ENSMUSG00000062960",
"ANK2": "ENSG00000145362",
}

def info_species(inf):
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", inf)
    response = connection.getresponse()
    print("Response received!", response.status, response.reason)
    response_dict = json.loads(response.read().decode())
    return response_dict

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        try:
            termcolor.cprint(self.requestline, 'green')
            termcolor.cprint(self.path, 'blue')
            o = urlparse(self.path)
            path_name = o.path
            arguments = parse_qs(o.query)
            print("Resource requested: ", path_name)
            print("Parameters:", arguments)

            try:
                if path_name == "/":
                    contents = Path("html/index.html").read_text()

                elif path_name == "/listSpecies":
                    ENDPOINT = "info/species"
                    species = info_species(ENDPOINT + PARAMETERS)["species"]
                    limit = arguments["limit"][0]

                    try:
                        if limit == "":
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
                            for element in species:
                                contents += f"""<p>{element["display_name"]} </p></body></html>"""

                        elif int(limit) > 267:
                            contents = Path('html/Error.html').read_text()

                        elif int(limit) < 0:
                            contents = Path('html/Error.html').read_text()

                        else:
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
                                        <p>The limit you have selected is: {limit}</p>
                                        <p>The names of the species are:</p>
                                    """

                            for element in species[:int(limit)]:
                                contents += f"""<p>{element["common_name"]} </p></body></html>"""

                    except ValueError:
                        contents = Path('html/Error.html').read_text()

                elif path_name == "/karyotype":
                    ENDPOINT = "info/assembly/"
                    specie = arguments["specie"][0]
                    species = info_species(ENDPOINT + specie + PARAMETERS)["karyotype"]

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

                elif path_name == "/chromosomeLength":
                    ENDPOINT = "/info/assembly/"
                    specie = arguments["specie"][0]
                    chromosome = arguments["chromo"][0]
                    species = info_species(ENDPOINT + specie + PARAMETERS)["top_level_region"]

                    for option in species:
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
                            contents = Path('html/Error.html').read_text()

                elif path_name == "/geneSeq":
                    ENDPOINT = "/sequence/id/"
                    try:
                        for key, id in DICT_GENES.items():
                            gene = arguments["gene"][0]
                            genes = info_species(ENDPOINT + PARAMETERS)[gene]
                            print(genes)
                            if key == gene:
                                contents = f"""                             
                                               <!DOCTYPE html>
                                               <html lang="en">
                                               <head>
                                                    <meta charset="utf-8">
                                                    <title>SEQUENCE OF A GIVEN GENE</title>
                                                </head>
                                                <body style="background-color: lightgreen">
                                                <h1>Gene sequence</h1>
                                                <p><a href="/">Main page</a></p>
                                                   <p>The sequence is:> {genes["seq"]}</p>
                                                </body>
                                                </html>"""

                    except KeyError:
                        print("The gene is not inside our dictionary. Choose one of the following", list(DICT_GENES.keys()))

                else:
                    contents = Path('html/Error.html').read_text()

            except KeyError:
                contents = Path('html/Error.html').read_text()

        except KeyboardInterrupt:
            contents = Path('html/Error.html').read_text()

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
    # -- client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
