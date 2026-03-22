import socket
import time
import hmac
import hashlib

HOST = "127.0.0.1"
PORT = 65432

SECRET_KEY = b"supersecretkey"

last_counter = {}  #Updated: store last counter per client

def generate_challenge():
    return b"random_challenge"

def verify_hmac(key, message, received_hmac):
    computed = hmac.new(key, message, hashlib.sha256).hexdigest()
    return computed == received_hmac

def is_fresh(client_id, counter):  #Updated: replay protection function
    if client_id not in last_counter:
        last_counter[client_id] = counter
        return True

    if counter <= last_counter[client_id]:
        return False

    last_counter[client_id] = counter
    return True

def reject(conn, reason):
    conn.send(f"REJECTED: {reason}".encode())
    conn.close()

def accept(conn):
    conn.send(b"ACCESS GRANTED")
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    print("Server listening...")

    while True:
        conn, addr = server.accept()

        with conn:
            print(f"Connected by {addr}")

            challenge = generate_challenge()  #1st step: send challenge
            conn.send(challenge)

            data = conn.recv(1024).decode()  #2nd step: receive data

            try:  #Expected format: counter|hmac
                counter_str, received_hmac = data.split("|")
                counter = int(counter_str)
            except:
                reject(conn, "INVALID FORMAT")
                continue

            client_id = addr[0]

            if not is_fresh(client_id, counter):  #Updated: replay check
                print("[ALERT] Replay attack detected")
                reject(conn, "REPLAY ATTACK")
                continue

            message = str(counter).encode() + challenge  #3rd step: verify HMAC

            if verify_hmac(SECRET_KEY, message, received_hmac):
                accept(conn)
            else:
                reject(conn, "INVALID HMAC")


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