import sys, os
from socket import *

if(len(sys.argv)>1):
	port=int(sys.argv[1])
else:
	print("Unable to continue, port required as parameter")
	sys.exit(1)

listening_socket=socket(AF_INET,SOCK_STREAM)
listening_socket.bind(("",port))
listening_socket.listen(1)

accepted_socket, address=listening_socket.accept()
pid=os.fork()

if pid!=0:
	listening_socket.close()
	incoming_stream=accepted_socket.makefile("r")
	print("Server - Server is accepting client messages")
	while True:
		msg=incoming_stream.readline()
		print(msg)
		if msg=="salir\n":
			break
	incoming_stream.close()
	accepted_socket.close()
	print("Client disconnected: If the client is not already disconected, type 'Salir'")
	os.waitpid(pid,0)
else:
	listening_socket.close()
	outgoing_stream=accepted_socket.makefile("w")
	print("Server - Server alowed to send messagges to client")
	while True:
		msg=input()
		outgoing_stream.write(msg+"\n")
		outgoing_stream.flush()
		if msg=="salir\n":
			break
	outgoing_stream.close()
	accepted_socket.close()
	sys.exit(0)
