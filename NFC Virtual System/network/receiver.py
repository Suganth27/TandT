import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import socket
import time
from core.config import HOST, PORT, SECRET_KEY, RELAY_THRESHOLD
from core.crypto import verify_hmac
from core.protocol import generate_challenge
from core.logger import log, log_metrics

last_counter = {}

def is_fresh(client_id, counter):
    if client_id not in last_counter:
        last_counter[client_id] = counter
        return True
    if counter <= last_counter[client_id]:
        return False
    last_counter[client_id] = counter
    return True

def reject(conn, reason, latency=0):
    conn.send(f"REJECTED: {reason}".encode())
    log(f"REJECTED {reason} latency={latency}")
    log_metrics(latency, reason.lower(), "rejected")
    conn.close()

def accept(conn, latency):
    conn.send(b"ACCESS GRANTED")
    log(f"SUCCESS latency={latency}")
    log_metrics(latency, "normal", "success")
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("Receiver running...")

    while True:
        conn, addr = server.accept()

        with conn:
            print(f"Connected: {addr}")

            challenge = generate_challenge()

            start_time = time.time()
            conn.send(challenge)

            data = conn.recv(1024).decode()
            end_time = time.time()

            latency = end_time - start_time
            print(f"Latency: {latency*1000:.2f} ms")

            if latency > RELAY_THRESHOLD:
                reject(conn, "RELAY ATTACK", latency)
                continue

            try:
                counter_str, received_hmac = data.split("|")
                counter = int(counter_str)
            except:
                reject(conn, "FORMAT ERROR", latency)
                continue

            client_id = addr[0]

            if not is_fresh(client_id, counter):
                reject(conn, "REPLAY ATTACK", latency)
                continue

            message = str(counter).encode() + challenge

            if verify_hmac(SECRET_KEY, message, received_hmac):
                accept(conn, latency)
            else:
                reject(conn, "INVALID HMAC", latency)
            
            time.sleep(3)


# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import socket
# import random
# import time
# from core.crypto import verify_response
# from experiments.latency_test import log_latency

# HOST = "127.0.0.1"
# PORT = 65432

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST, PORT))
# server.listen()

# print("Reader waiting for NFC tap...")

# while True:

#     conn, addr = server.accept()
#     print("\nDevice connected:", addr)

#     challenge = random.randint(100000,999999)

#     start_time = time.time()

#     conn.send(str(challenge).encode())

#     data = conn.recv(1024).decode()

#     end_time = time.time()

#     latency = end_time - start_time

#     counter, response = data.split(",")

#     counter = int(counter)

#     print("Challenge:", challenge)
#     print("Latency:", latency, "seconds")

#     if verify_response(counter, challenge, response):
#         print("Authentication SUCCESS")
#     else:
#         print("Authentication FAILED")

#     if latency > 2:
#         print("⚠ Possible relay attack detected!")

#     log_latency(latency)

#     conn.close()