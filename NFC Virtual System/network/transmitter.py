import socket
import time

from core.config import HOST, PORT, SECRET_KEY, DELAY_NORMAL
from core.crypto import generate_hmac

counter = 0

while True:
    counter += 1

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        challenge = client.recv(1024).decode()

        message = str(counter) + challenge
        response = generate_hmac(SECRET_KEY, message)

        payload = f"{counter}|{response}"

        time.sleep(DELAY_NORMAL)

        client.send(payload.encode())

        result = client.recv(1024).decode()
        print("[TRANSMITTER]", result)

    time.sleep(3)



# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import time
# import socket
# from core.config import HOST, PORT, SECRET_KEY
# from core.crypto import generate_hmac

# counter = 0

# while True:
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
#         client.connect((HOST, PORT))

#         challenge = client.recv(1024)

#         counter += 1

#         message = str(counter).encode() + challenge
#         response = generate_hmac(SECRET_KEY, message)

#         payload = f"{counter}|{response}"
#         client.send(payload.encode())

#         result = client.recv(1024)
#         print(result.decode())
        
#     time.sleep(3)