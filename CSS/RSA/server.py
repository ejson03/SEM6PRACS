import socket
import rsa
import time
import json
import hashlib

start = time.time()
e, n, d = rsa.RSA_keygen()
keytime = time.time() - start
print(f"It took {keytime} seconds to generate the public private key")

localIP = "127.0.0.1"
localPort = 15000
bufferSize = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

data = json.dumps({'e':e, 'n':n}).encode('utf-8')
print(f"Server data is {data}")

message = UDPServerSocket.recvfrom(bufferSize)
client_data = json.loads(message[0].decode())
client_address = message[1]
print(f"message from client {client_data} at address {client_address}")

UDPServerSocket.sendto(data, client_address)

client_e = int(client_data['e'])
client_n = int(client_data['n'])

pt = int(input("Enter message: "))
h = hashlib.md5(str(pt).encode('utf-8'))
pt_hash = int(h.hexdigest(), 16)
print(f"Hash generated is {pt_hash}")

start = time.time()
ct = pow(pt, client_e) % client_n
keytime = time.time() - start
print(f"It took {keytime} seconds to generate cipher")

start = time.time()
signature = pow(pt_hash, d) % n
keytime = time.time() - start
print(f"It took {keytime} seconds to generate signature")

data = json.dumps({'cipher':ct, 'signature':signature}).encode('utf-8')
print(f"Cipher text and signature of plaintext {pt} is {ct},.......{signature}")
UDPServerSocket.sendto(data, client_address)
