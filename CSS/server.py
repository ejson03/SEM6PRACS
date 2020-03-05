import socket
import rsa
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(1)

e,n,d = rsa.RSA_keygen()

while True:
    conn, addr = serv.accept()
    from_client = ''
    data = conn.recv(200)
    if not data: break
    from_client += data
    print(f"Alice send me {from_client}")
    conn.send(e+n)

    while True:
        message = input("Send Alice smething: ")
        conn.send(message)
    conn.close()
    