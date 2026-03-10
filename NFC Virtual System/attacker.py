import socket
import time

HOST = "127.0.0.1"
PORT = 65432

saved_message = None

while True:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    challenge = client.recv(1024).decode()
    challenge = int(challenge)

    print("\nAttacker intercepted challenge:", challenge)

    if saved_message is None:

        print("Waiting for legitimate phone message...")

        legit_counter = 1
        legit_response = "dummy"

        saved_message = f"{legit_counter},{legit_response}"

        client.send(saved_message.encode())

    else:

        print("Replaying old message!")

        client.send(saved_message.encode())

    client.close()

    time.sleep(5)