import socket
import time

from core.config import HOST, PORT

def run_once():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("[BLE] Connecting (REPLAY)...")
        time.sleep(0.01)
        print("[BLE] Connected")

        client.recv(1024)

        payload = "1|fakehmac"
        client.send(payload.encode())

        result = client.recv(1024).decode()
        print("[REPLAY]", result)
        print("[BLE] Disconnecting (REPLAY)\n")


if __name__ == "__main__":
    run_once()