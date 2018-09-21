import sys
import socket

clientSocket = socket.socket()
try:
    host = sys.argv[1]
except:
    host = 'localhost'
try:
    port = sys.argv[2]
except:
    port = 8889

# Connecting
clientSocket.connect((host, port))
print('Bienvenido al mejor chat del universo!')

while True:
    message = str(input('Tu: '))
    clientSocket.send(str.encode(message))
    if message == ':q':
    	print('Adios!')
    	clientSocket.shutdown(socket.SHUT_RDWR)
    	clientSocket.close()
    	break