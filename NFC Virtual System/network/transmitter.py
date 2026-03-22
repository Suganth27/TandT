import socket
import hmac
import hashlib

HOST = "127.0.0.1"
PORT = 65432

SECRET_KEY = b"supersecretkey"

counter = 0

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        challenge = client.recv(1024)  #1st step: receive challenge

        counter += 1 #Updated: increment counter

        message = str(counter).encode() + challenge  #2nd step: create message

        response = hmac.new(SECRET_KEY, message, hashlib.sha256).hexdigest()

        payload = f"{counter}|{response}"  #3rd step: send counter + response
        client.send(payload.encode())

        result = client.recv(1024)  #4th step: receive result
        print(result.decode())


# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import socket
# from core.crypto import generate_response

# HOST = "127.0.0.1"
# PORT = 65432

# counter = 0

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((HOST, PORT))

# challenge = client.recv(1024).decode()
# challenge = int(challenge)

# print("Phone received challenge:", challenge)

# counter += 1

# response = generate_response(counter, challenge)

# message = f"{counter},{response}"

# client.send(message.encode())

# print("Phone sent response")

# client.close()