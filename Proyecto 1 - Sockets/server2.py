import socket
import sys

# Message Buffer size
MSG_BUFFER = 1024

# Obtaining the arguments using command line
try:
    HOST = sys.argv[1]
except:
    HOST = 'localhost'
try:
    PORT = int(sys.argv[2])
except:
    PORT = 8889

# Creating the client socket. AF_INET IP Family (v4)
# and STREAM SOCKET Type.
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(0) # Listen six clients

print('Client connected to %s:%s' % (HOST, PORT))
sclient, addr = serverSocket.accept()  # Acepting client
print("[SERVER] Client %s connected!" % str(sclient.getpeername()))

while True:
    msg = sclient.recv(MSG_BUFFER)
    print('<'+str(sclient.getpeername())+'>: '+ msg.decode('ascii'))
    sclient.close()
