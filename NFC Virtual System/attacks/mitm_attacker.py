import socket
import time

from core.config import HOST, PORT

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        challenge = client.recv(1024).decode()

        # simulate intercept + modify
        fake_counter = 10
        fake_hmac = "tamperedhmac"

        payload = f"{fake_counter}|{fake_hmac}"
        client.send(payload.encode())

        result = client.recv(1024).decode()
        print("[MITM]", result)

    time.sleep(2)