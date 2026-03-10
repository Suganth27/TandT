import socket
from crypto import generate_response

HOST = "127.0.0.1"
PORT = 65432

counter = 0

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

challenge = client.recv(1024).decode()
challenge = int(challenge)

print("Phone received challenge:", challenge)

counter += 1

response = generate_response(counter, challenge)

message = f"{counter},{response}"

client.send(message.encode())

print("Phone sent response")

client.close()