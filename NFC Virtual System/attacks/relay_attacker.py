import socket
import time

from core.config import HOST, PORT, DELAY_RELAY

def run_once():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("[BLE] Connecting (RELAY)...")
        time.sleep(0.01)
        print("[BLE] Connected")

        client.recv(1024)

        time.sleep(DELAY_RELAY)

        payload = "999999|fakehmac"
        client.send(payload.encode())

        result = client.recv(1024).decode()
        print("[RELAY]", result)
        print("[BLE] Disconnecting (RELAY)\n")


if __name__ == "__main__":
    run_once()