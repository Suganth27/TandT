import socket
import time

from core.config import HOST, PORT

while True:
    for i in range(3):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))

            client.recv(1024)

            payload = f"{i}|fakehash{i}"
            client.send(payload.encode())

            result = client.recv(1024).decode()
            print("[BRUTEFORCE]", result)

        time.sleep(1)

    time.sleep(2)