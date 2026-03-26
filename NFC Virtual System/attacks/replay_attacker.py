import socket
import time

HOST = "127.0.0.1"
PORT = 65432

# simulate replay with same counter
payload = "1|fakehmac"

while True:  #for _ in range(10): for exact 10 samples
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        client.recv(1024)  # receive challenge

        client.send(payload.encode())

        result = client.recv(1024)
        print("[REPLAY]", result.decode())

    time.sleep(3)  # delay to avoid spam



# import socket
# import time

# HOST = "127.0.0.1"
# PORT = 65432

# saved_message = None

# while True:

#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect((HOST, PORT))

#     challenge = client.recv(1024).decode()
#     challenge = int(challenge)

#     print("\nAttacker received challenge:", challenge)

#     if saved_message is None:

#         print("Recording first valid authentication...")

#         counter = 1
#         fake_response = "replay_attack"

#         saved_message = f"{counter},{fake_response}"

#         client.send(saved_message.encode())

#     else:

#         print("Replaying old authentication message!")

#         client.send(saved_message.encode())

#     client.close()

#     time.sleep(5)