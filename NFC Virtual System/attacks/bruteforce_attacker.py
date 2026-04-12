import socket
import random
import time

from core.config import HOST, PORT

def run_once():
    i = random.randint(100000, 200000)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("[BLE] Connecting (BRUTEFORCE)...")
        time.sleep(0.01)
        print("[BLE] Connected")

        client.recv(1024)

        payload = f"{i}|fakehash{i}"
        client.send(payload.encode())

        result = client.recv(1024).decode()
        print("[BRUTEFORCE]", result)
        print("[BLE] Disconnecting (BRUTEFORCE)\n")


if __name__ == "__main__":
    run_once()