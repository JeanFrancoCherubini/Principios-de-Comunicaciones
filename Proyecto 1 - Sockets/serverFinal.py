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
        print("[SERVER] Cliente %s se ha desconectado!" % str(self.socket.getpeername()))
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        break
      else:
        print('<'+str(self.socket.getpeername())+'>: '+ message.decode('ascii'))
    accept = acceptThread(1,serverSocket)
    accept.start()

class acceptThread(threading.Thread):
  def __init__(self,counter,serverSocket):
    threading.Thread.__init__(self)
    self.counter=counter
    self.serverSocket=serverSocket
  def run(self):
    cliente,direccion=self.serverSocket.accept()
    print("[SERVER] Cliente %s conectado!" % str(cliente.getpeername()))
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
serverSocket.listen(6) # Escuchar 6 clientes máximo

print('Cliente conectado a %s:%s' % (HOST, PORT))
accept = acceptThread(1,serverSocket)
accept2 = acceptThread(2,serverSocket)
accept3 = acceptThread(3,serverSocket)
accept4 = acceptThread(4,serverSocket)
accept5 = acceptThread(5,serverSocket)
accept6 = acceptThread(6,serverSocket)
accept.start()
accept2.start()
accept3.start()
accept4.start()
accept5.start()
accept6.start()
while True:
  pass