# transfer file from server to the client

import socket

# creating socket
s = socket.socket()

# defining configurations
host = "127.0.0.1"
port = 50000

# connecting to server
s.connect((host, port))
s.send("\nConnection established.")

# receiving file
with open('received_file.txt', 'wb') as f:
	print("File has been opened.")

	while True:
		print("\nReceiving data...")
		data = s.recv(1024)
		print("data = %s", (data))
		if not data:
			break

		# write data to a file
		f.write(data)

f.close()
print("\nFile has been received.")

# closing the connection
s.close()
print("\nConnection terminated.")
