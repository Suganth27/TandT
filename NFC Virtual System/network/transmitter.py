import socket
import time
import os

from core.config import HOST, PORT, SECRET_KEY, DELAY_NORMAL
from core.crypto import generate_hmac

COUNTER_FILE = "logs/counter.txt"

def load_counter():
    if not os.path.exists(COUNTER_FILE):
        return 0
    with open(COUNTER_FILE, "r") as f:
        return int(f.read().strip())

def save_counter(value):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(value))


counter = load_counter()

while True:
    counter += 1
    save_counter(counter)  # persist counter

    try:
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

    except Exception as e:
        print("[ERROR]", e)

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