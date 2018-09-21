import socket
import sys
import threading

class crearCliente (threading.Thread):
   def __init__(self, socket, direccion):
      threading.Thread.__init__(self)
      self.socket = socket
      self.direccion = direccion
   def run(self):
      message=self.socket.recv(MSG_BUFFER)
      print('<'+str(self.socket.getpeername())+'>: '+ message.decode('ascii'))



class aceptarCliente (threading.Thread):
   def __init__(self,serverSocket):
      threading.Thread.__init__(self)
      self.serverSocket=serverSocket
   def run(self):
      cliente,direccion= self.serverSocket.accept()
      usuario=crearCliente(cliente,direccion)
      while True:
        usuario.run()

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
serverSocket.listen(6) # Listen to SIX clients

print('Client connected to %s:%s' % (HOST, PORT))

while True:
  ejecutar=aceptarCliente(serverSocket)
  ejecutar.run()