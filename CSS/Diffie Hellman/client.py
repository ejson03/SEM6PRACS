# assuming this is alice
import socket
import dhkeygen

serverAddressPort = ("127.0.0.1", 15000)

bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

aliceKeyGenerator = dhkeygen.DH(23, 5)
msgAlice = str(aliceKeyGenerator.keygenStage1(3))
sendAlice = str.encode(msgAlice)
UDPClientSocket.sendto(sendAlice, serverAddressPort)
msgServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}\nK1 = {}".format(int(msgServer[0]),
     aliceKeyGenerator.keygenStage2(int(msgServer[0]), 3))

print(msg)