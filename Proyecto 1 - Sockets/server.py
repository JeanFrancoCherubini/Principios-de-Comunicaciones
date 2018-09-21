import socket
import sys
import threading

class clientThread(threading.Thread):
  def __init__(self, socket, direccion):
    threading.Thread.__init__(self)
    self.socket = socket
    self.direccion = direccion
  def run(self):
    while True:
      message=self.socket.recv(MSG_BUFFER)
      if message.decode('ascii') == ':q':
        print("[SERVER] Client %s disconnected!" % str(self.socket.getpeername()))
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        break
      else:
        print('<'+str(self.socket.getpeername())+'>: '+ message.decode('ascii'))
    accept = acceptThread(serverSocket)
    accept.start()

class acceptThread(threading.Thread):
  def __init__(self,serverSocket):
    threading.Thread.__init__(self)
    self.serverSocket=serverSocket
  def run(self):
    cliente,direccion=self.serverSocket.accept()
    print("[SERVER] Client %s connected!" % str(cliente.getpeername()))
    usuario=clientThread(cliente,direccion)
    usuario.start()


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
serverSocket.listen(6) # Listen one client clients

print('Client connected to %s:%s' % (HOST, PORT))
accept = acceptThread(serverSocket)
accept2 = acceptThread(serverSocket)
accept3 = acceptThread(serverSocket)
accept4 = acceptThread(serverSocket)
accept5 = acceptThread(serverSocket)
accept6 = acceptThread(serverSocket)
accept.start()
accept2.start()
accept3.start()
accept4.start()
accept5.start()
accept6.start()
while True:
  pass