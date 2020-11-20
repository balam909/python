import sys, os
from socket import *

if(len(sys.argv)>2):
	host=sys.argv[1]
	port=int(sys.argv[2])
else:
	print("Unable to create connection, required parameters 'Host' and/or 'Port' where not provided")
	sys.exit(1)
server_address=gethostbyname(host)
connection_socket=socket(AF_INET,SOCK_STREAM)
connection_socket.connect((server_address,port))
pid=os.fork()

if pid!=0:
	incoming_stream=connection_socket.makefile("r")
	print("Client - Client is accepting server messages")
	while True:
		msg=incoming_stream.readline()
		print(msg)
		if msg=="salir\n":
			break
	incoming_stream.close()
	connection_socket.close()
	print("Server disconnected, if you are not disconnected type 'salir'")
	os.waitpid(pid,0)
else:
	outgoing_stream=connection_socket.makefile("w")
	print("Client - Server is accepting client messages")
	while True:
		msg=input()
		outgoing_stream.write(msg+"\n")
		outgoing_stream.flush()
		if msg=="salir\n":
			break
	outgoing_stream.close()
	connection_socket.close()
	sys.exit(0)
