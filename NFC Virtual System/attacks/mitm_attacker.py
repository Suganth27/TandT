import socket
import time

from core.config import HOST, PORT

def run_once():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("[BLE] Connecting (MITM)...")
        time.sleep(0.01)
        print("[BLE] Connected")

        challenge = client.recv(1024).decode()

        fake_counter = 999999
        fake_hmac = "tamperedhmac"

        payload = f"{fake_counter}|{fake_hmac}"
        client.send(payload.encode())

        result = client.recv(1024).decode()
        print("[MITM]", result)
        print("[BLE] Disconnecting (MITM)\n")


if __name__ == "__main__":
    run_once()