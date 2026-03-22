import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import socket
import random
import time
from core.crypto import verify_response
from experiments.latency_test import log_latency

HOST = "127.0.0.1"
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Reader waiting for NFC tap...")

while True:

    conn, addr = server.accept()
    print("\nDevice connected:", addr)

    challenge = random.randint(100000,999999)

    start_time = time.time()

    conn.send(str(challenge).encode())

    data = conn.recv(1024).decode()

    end_time = time.time()

    latency = end_time - start_time

    counter, response = data.split(",")

    counter = int(counter)

    print("Challenge:", challenge)
    print("Latency:", latency, "seconds")

    if verify_response(counter, challenge, response):
        print("Authentication SUCCESS")
    else:
        print("Authentication FAILED")

    if latency > 2:
        print("⚠ Possible relay attack detected!")

    log_latency(latency)

    conn.close()