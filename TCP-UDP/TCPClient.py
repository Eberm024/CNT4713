#TCPClient.py

#TCP (SOCK_STREAM) is a connection-based protocol. The connection is e
#parties have a conversation until the connection is terminated by one
from socket import socket, AF_INET, SOCK_STREAM
#Create a localhost
serverName = 'localhost'
serverPort = 12001
#Notice the use of SOCK_STREAM for TCP packets
clientSocket = socket (AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = raw_input ('Input lowercase sentence: ')
clientSocket.send(message)
modifiedMessage = clientSocket.recv(2048)
print 'From Server: ', modifiedMessage
clientSocket.close()
