import socket
import time

from core.config import HOST, PORT

def run_once():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("[BLE] Connecting (IMPERSONATION)...")
        time.sleep(0.01)
        print("[BLE] Connected")

        client.recv(1024)

        payload = "999999|invalidhmac"
        client.send(payload.encode())

        result = client.recv(1024).decode()
        print("[IMPERSONATION]", result)
        print("[BLE] Disconnecting (IMPERSONATION)\n")


if __name__ == "__main__":
    run_once()