
import socket
import dhkeygen

localIP = "127.0.0.1"
localPort = 15000
bufferSize = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

key_gen = dhkeygen.DH(23, 5)
msgFromServer = str(key_gen.keygenStage1(4))
bytesToSend = str.encode(msgFromServer)

#while (True):
bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

message = int(bytesAddressPair[0])

address = bytesAddressPair[1]

clientMsg = "Message from Client {}\nK2 :{} ".format(message, key_gen.keygenStage2(message, 4))
clientIP = "Client IP Address:{}".format(address)

print(clientMsg)
print(clientIP)


UDPServerSocket.sendto(bytesToSend, address)