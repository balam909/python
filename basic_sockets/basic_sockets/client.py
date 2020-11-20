import sys,os
from socket import *

if(len(sys.argv)>2):
	host=sys.argv[1]
	port=int(sys.argv[2])
else:
	print("Required Parameters not found. You should provide host and port to create socket connection")
	sys.exit(1)

server_address=gethostbyname(host)
connection_socket=socket(AF_INET,SOCK_STREAM)
connection_socket.connect((server_address,port))
incoming_stream = connection_socket.makefile("r")
outgoing_stream = connection_socket.makefile("w")
print(incoming_stream.read())
incoming_stream.close()
outgoing_stream.close()
connection_socket.close()
