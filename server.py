import http.server
import socketserver
from os import system
from time import sleep

PORT = 8000  # Porta que o servidor vai usar

# Para acessar o servidor, use o Endereço IPv4 com o número da porta
# Assim: 000.000.0.000:porta

system("ipconfig")

sleep(2)
print()

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servindo na porta", PORT)
    httpd.serve_forever()   