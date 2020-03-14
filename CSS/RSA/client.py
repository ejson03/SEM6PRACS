# assuming this is alice
import socket
import rsa
import json
import time
import hashlib

start = time.time()
e, n, d = rsa.RSA_keygen()
keytime = time.time() - start
print(f"It took {keytime} seconds to generate the public private key")

serverAddressPort = ("127.0.0.1", 15000)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

data = json.dumps({'e':e, 'n':n}).encode('utf-8')
print(f"my data is {data}")

UDPClientSocket.sendto(data, serverAddressPort)
message = UDPClientSocket.recvfrom(bufferSize)
server_data = json.loads(message[0].decode())
server_e = int(server_data['e'])
server_n = int(server_data['n'])
server_address = message[1]
print(f"message from server {server_data} at address {server_address}")

data = UDPClientSocket.recvfrom(bufferSize)
server_data = json.loads(data[0].decode())
server_address = data[1]
print(f"cipher text from server {server_data} at address {server_address}")

cipher = int(server_data['cipher'])
signature = int(server_data['signature'])

start = time.time()
pt = pow(cipher, d) % n
keytime = time.time() - start
print(f"It took {keytime} seconds to generate the decrypted ")
print(f"Decrypted text from server is {pt}")

h = hashlib.md5(str(pt).encode('utf-8'))
client_hash = int(h.hexdigest(), 16)
print(f"Hash generated is {client_hash}")

start = time.time()
server_hash = pow(signature, server_e) % server_n
keytime = time.time() - start
print(f"It took {keytime} seconds to generate the decrypted ")
print(f"Decrypted signature hash is {server_hash}")
if (server_hash == client_hash):
    print("Genuine data recieved")


