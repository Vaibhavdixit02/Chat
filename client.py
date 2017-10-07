import socket
from threading import Thread

class Client:
	"""docstring for Client"""
	def __init__(self,connect_host,connect_port):
		self.connect_host = connect_host
		self.connect_port = connect_port
		# self.self_host = self_host
		# self.self_port = self_port
		self.socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# self.socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket1.connect((self.connect_host,self.connect_port))
		# self.socket2.bind((self.socket1.getsockname()[0], self.socket1.getsockname()[1]))
		# self.socket2.listen(100)
	
	def sendmssg(self,name):
		while True:
			self.socket1.send(name + raw_input())
	
	def handle_accept(self):
		sock, addr = self.socket2.accept()
		self.client_name = repr(addr)
		self.mssg_recvr = sock 

	def recievemssg(self):
		while True:
			mssg = self.socket1.recv(1024)
			print "recieved: " + mssg


port1 = int(raw_input("enter port to connect to: "))
urname = raw_input("enter ")
client = Client("10.8.120.165",port1)
# Thread(target=client.handle_accept()).start()

threa1 = Thread(target = client.sendmssg, kwargs={'name' : urname})
threa2 = Thread(target = client.recievemssg)

threa1.start()
threa2.start()
	
