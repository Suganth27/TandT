import socket
import time
import random

from core.config import HOST, PORT, SECRET_KEY, LATENCY_THRESHOLD
from core.crypto import generate_hmac
from core.logger import log_metrics

last_counter = 0

def handle_client(conn):
    global last_counter

    # 🔴 STEP 1: generate challenge
    challenge = str(random.randint(1000, 9999))
    conn.send(challenge.encode())

    start_time = time.time()

    data = conn.recv(1024).decode()
    end_time = time.time()

    latency = end_time - start_time

    try:
        counter, received_hmac = data.split("|")
        counter = int(counter)
    except:
        conn.send(b"INVALID FORMAT")
        return

    message = str(counter) + challenge
    expected_hmac = generate_hmac(SECRET_KEY, message)

    # 🔴 RELAY DETECTION
    if latency > LATENCY_THRESHOLD:
        conn.send(b"RELAY DETECTED")
        log_metrics(latency, "relay", "rejected")
        return

    # 🔴 REPLAY DETECTION
    if counter <= last_counter:
        conn.send(b"REPLAY DETECTED")
        log_metrics(latency, "replay", "rejected")
        return

    # 🔴 HMAC VALIDATION
    if received_hmac == expected_hmac:
        last_counter = counter
        conn.send(b"SUCCESS")
        log_metrics(latency, "normal", "success")
    else:
        conn.send(b"INVALID HMAC")
        log_metrics(latency, "normal", "rejected")


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print("Receiver running...")

        while True:
            conn, addr = server.accept()
            with conn:
                handle_client(conn)


if __name__ == "__main__":
    start_server()



# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import socket
# import time
# from core.config import HOST, PORT, SECRET_KEY, RELAY_THRESHOLD
# from core.crypto import verify_hmac
# from core.protocol import generate_challenge
# from core.logger import log, log_metrics

# last_counter = {}

# def is_fresh(client_id, counter):
#     if client_id not in last_counter:
#         last_counter[client_id] = counter
#         return True
#     if counter <= last_counter[client_id]:
#         return False
#     last_counter[client_id] = counter
#     return True

# def reject(conn, reason, latency=0):
#     conn.send(f"REJECTED: {reason}".encode())
#     log(f"REJECTED {reason} latency={latency}")
#     log_metrics(latency, reason.lower(), "rejected")
#     conn.close()

# def accept(conn, latency):
#     conn.send(b"ACCESS GRANTED")
#     log(f"SUCCESS latency={latency}")
#     log_metrics(latency, "normal", "success")
#     conn.close()

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
#     server.bind((HOST, PORT))
#     server.listen()
#     print("Receiver running...")

#     while True:
#         conn, addr = server.accept()

#         with conn:
#             print(f"Connected: {addr}")

#             challenge = generate_challenge()

#             start_time = time.time()
#             conn.send(challenge)

#             data = conn.recv(1024).decode()
#             end_time = time.time()

#             latency = end_time - start_time
#             print(f"Latency: {latency*1000:.2f} ms")

#             if latency > RELAY_THRESHOLD:
#                 reject(conn, "RELAY ATTACK", latency)
#                 continue

#             try:
#                 counter_str, received_hmac = data.split("|")
#                 counter = int(counter_str)
#             except:
#                 reject(conn, "FORMAT ERROR", latency)
#                 continue

#             client_id = addr[0]

#             if not is_fresh(client_id, counter):
#                 reject(conn, "REPLAY ATTACK", latency)
#                 continue

#             message = str(counter).encode() + challenge

#             if verify_hmac(SECRET_KEY, message, received_hmac):
#                 accept(conn, latency)
#             else:
#                 reject(conn, "INVALID HMAC", latency)
            
#             time.sleep(3)