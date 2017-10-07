import socket
from threading import Thread
from SocketServer import ThreadingMixIn
import select
 
TCP_IP = '10.8.120.165'
TCP_PORT = int(raw_input("Enter your port: "))
BUFFER_SIZE = 1024
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
tcpsock.listen(3)
(conn1, (ip,port)) = tcpsock.accept()
(conn2, (ip,port)) = tcpsock.accept()
conn1me = []
conn2me = []
rwe = [conn1,conn2]
lenconn1 = 0
lenconn2 = 0

def StartSend(conn,mssglst):
	conn.send(mssglst[len(mssglst)-1][5:])

def StartRecv(conn):
	data = conn.recv(1024)
	print data
	if data[:5] == "conn1":
		conn1me.append(data)
	if data[:5] == "conn2":
		conn2me.append(data)

while True:
	r,w,e = select.select(rwe,[],[])
	StartRecv(r[0])
	print conn1me
	print conn2me
	# StartSend(conn1, conn1me)
	if len(conn1me) > lenconn1:
		StartSend(conn2,conn1me)
		lenconn1 = len(conn1me)
	elif len(conn2me) > lenconn2:
		StartSend(conn1,conn2me)
		lenconn2 = len(conn2me)
	