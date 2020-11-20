import sys, os
from socket import *
from time import *

if(len(sys.argv[1])):
	port=int(sys.argv[1])
else:
	print("Required parameter not provided. Set a non used port number major than 1024 and try again")
	sys.exit(1)

listening_socket=socket(AF_INET,SOCK_STREAM)
listening_socket.bind(('',port))
listening_socket.listen(1)

while 1:
	accepted_socket, address=listening_socket.accept()
	incoming_stream=accepted_socket.makefile("r")
	outgoing_stream=accepted_socket.makefile("w")
	localtime=ctime()
	outgoing_stream.write(localtime+"\n")
	print("Connection from",address,"at",localtime)
	incoming_stream.close()
	outgoing_stream.close()
	accepted_socket.close()

