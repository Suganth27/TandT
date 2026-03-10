import socket
import random
from crypto import verify_response

HOST = "127.0.0.1"
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Reader waiting for NFC tap...")

conn, addr = server.accept()
print("Phone connected:", addr)

challenge = random.randint(100000, 999999)
print("Generated challenge:", challenge)

conn.send(str(challenge).encode())

data = conn.recv(1024).decode()
counter, response = data.split(",")

counter = int(counter)

print("Received counter:", counter)
print("Received response:", response)

if verify_response(counter, challenge, response):
    print("Authentication SUCCESS")
else:
    print("Authentication FAILED")

conn.close()