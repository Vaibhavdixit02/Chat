import socket
from threading import Thread
from SocketServer import ThreadingMixIn
import select
 
TCP_IP = '127.0.0.1'
TCP_PORT = int(raw_input("Enter your port: "))
BUFFER_SIZE = 1024
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
rwe = []
clients = {}
total_mssg_list = []
len_mssg_list = 0
clientthreads = []

class Client(object):
	"""docstring for Client"""
	def __init__(self, name_s,name_t,socket_s):
		self.name_s = name_s
		self.name_t = name_t
		self.sock = socket_s
		self.messages = []
	
	def recvfrom(self):
		while True:
			data = self.sock.recv(1024)
			if data:
				total_mssg_list.append(data)
				self.messages.append(data)
				try:
					clients[self.name_t].send(data)
				except:
					print "The requested user not found"
					continue
				print data


def acceptor():
	while True:
		tcpsock.listen(20)
		(conn , (ip,port)) = tcpsock.accept()
		rwe.append(conn)
		conn.send("Who to connect with?")
		name = conn.recv(1024)
		newclient = Client(name[:name.find('-')],name[name.find('-')+1:],conn)
		for i in rwe[:len(rwe)-1]:
			i.send(name + " joined the server")
		newthread = Thread(target= newclient.recvfrom)
		clients[newclient.name_s] = newclient.sock
		clientthreads.append(newthread)
		newthread.start()
		print rwe

def StartSend(mssglst, conn=tcpsock):
	mssg = total_mssg_list[len(total_mssg_list)-1]
	addr_recv = mssg[:mssg.find('-')]
	# addr = ""
	# conn.send(addr_recv)

def runfunc():
	global len_mssg_list
	while True:
		if len(total_mssg_list) > len_mssg_list:
			StartSend(total_mssg_list)
			len_mssg_list = len(total_mssg_list)

def CheckRequestforChange(message):
	if message[message.find('-'): message.find('-')+2] == '1':
		

		
threa1 = Thread(target= acceptor)
threa2 = Thread(target= runfunc)


threa1.start()
threa2.start()