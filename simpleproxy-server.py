import socket, sys, codecs

# command line parameters
if(len(sys.argv) != 3 and len(sys.argv) != 2):
	print("Usage: simpleproxy-server.py <listen port> [listen ip]")
	exit()
elif(len(sys.argv) == 2):
	listenIP = "0.0.0.0"
else:
	listenIP = sys.argv[2]

# listen port
server_address = (listenIP, int(sys.argv[1]))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)
sock.listen(1)
print("Listening on " + listenIP + ":" + str(server_address[1]))

# accept connections forever
while True:
	connection, client_address = sock.accept()
	try:
		print("Connection from " + client_address[0])

		data = ""
		# receive data
		while True:
			current_data = connection.recv(16)
			data += current_data
			if len(current_data) < 16:
				break
			elif len(current_data) == 4 and current_data == "/EOF":
				data = data.rstrip('/EOF')
				break
		print("Received request from client")
		data = codecs.decode(data, 'rot_13') # decode rot13
		httpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		splitted = data.split("/", 1)
		ipport = splitted[0].split(':')
		ipport = (ipport[0], int(ipport[1]))
		httpsock.connect((ipport))

		# process actual request
		httpsock.sendall(splitted[1])
		print("Sent request")
		httpdata = ""
		while True:
			httpcurrent_data = httpsock.recv(16)
			httpdata += httpcurrent_data
			if len(httpcurrent_data) < 16:
				 break
		print("Received response")
		connection.sendall(codecs.decode(httpdata, 'rot_13')) # sent rot13 encoded response to user
		print("Sent response to client")
	finally:
		connection.close()
		print("Connection closed")
		print("")
