# transfer file from server to the client

import socket

s = socket.socket()

# defining configurations
host = "127.0.0.1"
port = 50000

# binding to the client connection
s.bind((host, port))
s.listen(5)

print("Server is listening...")

while True:
	c, addr = s.accept()

	print("\nConnection has been established from ", addr)
	data = c.recv(1024)

	# file info
	filename = "file.txt"
	f = open(filename, 'rb')
	l = f.read(1024)

	while(l):
		c.send(l)
		print("Sent", repr(l))
		l = f.read(1024)

	f.close()

	print("\nFile has been successfully sent.")

	# closing connection
	c.close()
