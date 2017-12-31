import socket
from threading import Thread


class Client:
	"""docstring for Client"""
	def __init__(self,connect_host,connect_port,urname):
		self.connect_host = connect_host
		self.connect_port = connect_port
		self.socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket1.connect((self.connect_host,self.connect_port))
		self.name = urname
	
	def sendmssg(self):
		while True:
			a = raw_input()
			self.socket1.send(self.name + '-' +a)

	def recievemssg(self):
		while True:
			mssg = self.socket1.recv(1024)
			if mssg:
				print "recieved: " + mssg

	def addnewclient(self):
		while True:
			control_input = raw_input()
			menu_select = ""
			if control_input == "menu":
				print "|add new client|change my name|"
				menu_select += raw_input()
			if menu_select == "add new client":
				new_client = int(raw_input("enter port to connect to: "))
				self.socket1.connect((self.connect_host,new_client))

port1 = int(raw_input("enter port to connect to: "))
urname = raw_input("enter your name")
client = Client("127.0.0.1",port1,urname)

threa1 = Thread(target = client.sendmssg)
threa2 = Thread(target = client.recievemssg)
threa3 = Thread(target = Client.addnewclient)

threa1.start()
threa2.start()
threa3.start()	
