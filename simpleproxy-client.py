import socket, sys, codecs

# command line parameters
if(len(sys.argv) != 3 and len(sys.argv) != 2):
        print("Usage: cat request.txt | simpleproxy-server.py <ip> <port>\r\n\r\nrequest.txt:\r\n1.2.3.4:80/GET / HTTP/1.1\r\nHost: .......\r\n\r\nthis also could be a raw TCP request, not HTTP\r\n(HTTP is also TCP but... yeah)")
	exit()

server_address = (sys.argv[1], int(sys.argv[2]))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(server_address)

request = ""
for line in sys.stdin:
    request += line
try:
	message = codecs.encode(request, 'rot_13') # encode HTTP request
	if len(message) % 16 == 0:
		message += "/EOF"
	sock.sendall(message)

	data = ""
	while True:
		current_data = sock.recv(16)
		data += current_data
		if len(current_data) < 16:
			break
		elif len(current_data) == 4 and current_data == "/EOF":
			data = data.rstrip('/EOF')
			break

	print(codecs.decode(data, 'rot_13'))

finally:
	sock.close()


