import sys
import socket
import threading


MSG_BUFFER=1024
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
print('Wena Kongpare, te conectaste a %s:%s' % (host, port))

while True:
    message = input("Tu: ")
    clientSocket.send(str.encode(message))
