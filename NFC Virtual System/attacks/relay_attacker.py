import socket
import time

from core.config import HOST, PORT, DELAY_RELAY

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        challenge = client.recv(1024).decode()

        time.sleep(DELAY_RELAY)

        payload = "1|fakehmac"
        client.send(payload.encode())

        result = client.recv(1024).decode()
        print("[RELAY]", result)

    time.sleep(3)






# import socket
# import time

# HOST = "127.0.0.1"
# PORT = 65432

# while True:  #for _ in range(10): for exact 10 samples
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
#         client.connect((HOST, PORT))

#         challenge = client.recv(1024)

#         time.sleep(3)  #simulate relay delay

#         payload = "1|fakehmac"
#         client.send(payload.encode())

#         result = client.recv(1024)
#         print("[RELAY]", result.decode())

#     time.sleep(3)