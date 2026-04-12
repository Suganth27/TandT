import socket
import time

from core.config import HOST, PORT

payload = "1|fakehmac"

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        client.recv(1024)

        client.send(payload.encode())

        result = client.recv(1024).decode()
        print("[REPLAY]", result)

    time.sleep(1)



# import socket
# import time

# HOST = "127.0.0.1"
# PORT = 65432

# #simulate replay with same counter
# payload = "1|fakehmac"

# while True:  #for _ in range(10): for exact 10 samples
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
#         client.connect((HOST, PORT))

#         client.recv(1024)  #receive challenge

#         client.send(payload.encode())

#         result = client.recv(1024)
#         print("[REPLAY]", result.decode())

#     time.sleep(3)  #delay to avoid spam