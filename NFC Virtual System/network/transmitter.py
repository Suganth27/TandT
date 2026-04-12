import socket
import time
import os

from core.config import HOST, PORT, SECRET_KEY
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


def run_once():
    counter = load_counter() + 1
    save_counter(counter)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        challenge = client.recv(1024).decode()
        print("[BLE] Connecting to receiver...")
        time.sleep(0.01)
        print("[BLE] Connected")

        message = str(counter) + challenge
        response = generate_hmac(SECRET_KEY, message)

        payload = f"{counter}|{response}"

        client.send(payload.encode())

        result = client.recv(1024).decode()
        print("[NORMAL]", result)
        print("[BLE] Disconnecting...\n")


if __name__ == "__main__":
    run_once()