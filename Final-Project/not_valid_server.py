import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils1 as su


PORT = 8080
SERVER = "rest.ensembl.org"
PARAMETERS = "?content-type=application/json"


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


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')
        request_line = self.requestline.split(' ')
        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters:", arguments)
        print(request_line)
        path = request_line[1]
        print(path)
        data = path.split('?')  # split separates the content from the '?'
        print(data)
        data_1 = data[0]  # This is the content before interrogation mark.
        print(data_1)

        context = {}
        try:
            if path_name == "/":
                contents = su.read_template_html_file("./html/index.html").render(context=context)

            elif path_name == "/listSpecies":
                try:
                    ENDPOINT = "info/species"
                    data_decoded = su.get_info(ENDPOINT)
                    limit = arguments["limit"][0]
                    contents = su.get_species(data_decoded, limit)

                except KeyError:
                    contents = su.read_template_html_file("./html/Error.html").render()

            elif path == "/karyotype":
                try:
                    ENDPOINT = "info/assembly/"
                    specie = arguments["specie"][0]
                    print(specie)
                    karyo_data = su.get_info(ENDPOINT + specie)
                    print(karyo_data)
                    print(karyo_data["karyotype"])
                    contents = su.get_karyotype(karyo_data, specie)

                except KeyError:
                    contents = su.read_template_html_file("./html/Error.html").render()

            elif path == "/chromosomeLength":
                try:
                    ENDPOINT = "/info/assembly/"
                    specie = arguments["specie"][0]
                    chromosome = arguments["chromo"][0]
                    chromo_data = su.get_info(ENDPOINT + specie)
                    contents = su.get_chromosome_lenght(chromo_data, specie, chromosome)

                except KeyError:
                    contents = su.read_template_html_file("./html/Error.html").render()



        except KeyError:
            contents = su.read_template_html_file("./html/Error.html").render()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

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
