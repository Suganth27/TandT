import socket
import time

from core.config import HOST, PORT

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        client.recv(1024)

        payload = "999|invalidhmac"
        client.send(payload.encode())

        result = client.recv(1024).decode()
        print("[IMPERSONATION]", result)

    time.sleep(3)