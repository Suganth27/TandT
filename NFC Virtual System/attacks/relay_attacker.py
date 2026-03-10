import socket
import time
from core.crypto import generate_response

HOST = "127.0.0.1"
PORT = 65432

counter = 0

while True:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    challenge = client.recv(1024).decode()
    challenge = int(challenge)

    print("\nRelay attacker forwarding challenge:", challenge)

    time.sleep(3)   # artificial relay delay

    counter += 1

    response = generate_response(counter, challenge)

    message = f"{counter},{response}"

    client.send(message.encode())

    client.close()