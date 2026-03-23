import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import socket
from core.config import HOST, PORT, SECRET_KEY
from core.crypto import generate_hmac

counter = 0

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        challenge = client.recv(1024)

        counter += 1

        message = str(counter).encode() + challenge
        response = generate_hmac(SECRET_KEY, message)

        payload = f"{counter}|{response}"
        client.send(payload.encode())

        result = client.recv(1024)
        print(result.decode())
        
    time.sleep(3)


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