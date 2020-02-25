import socket

port = 8080
s = socket.socket()
host = socket.gethostname()
s.bind((host,port))
s.listen(5)

print ("Server is listening")

while True:
	conn, addr = s.accept()
	print("got connection from",addr)
	data = conn.recv(1024)
	print('Server Recieved',repr(data))

	filename = 'login_packet.txt'
	f = open(filename,'rb')
	l = f.read(1024)
	f.close()

print('done sending')
conn.send ('heartbeat packet -- 78 78 0B 23 C0 01 22 04 00 01 00 08 18 72 0D 0A')
conn.close()