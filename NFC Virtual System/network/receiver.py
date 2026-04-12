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

    # 🔴 RELAY ATTACK (delay based)
    if latency > LATENCY_THRESHOLD:
        conn.send(b"RELAY DETECTED")
        log_metrics(latency, "relay", "rejected")
        return

    # 🔴 REPLAY ATTACK (counter reuse)
    if counter <= last_counter:
        conn.send(b"REPLAY DETECTED")
        log_metrics(latency, "replay", "rejected")
        return

    # 🔴 VALID AUTHENTICATION
    if received_hmac == expected_hmac:
        last_counter = counter
        conn.send(b"SUCCESS")
        log_metrics(latency, "normal", "success")
        return

    # 🔴 INVALID HMAC → classify attack type
    conn.send(b"INVALID HMAC")

    # classify based on behavior
    if counter > last_counter:
        # attacker trying new counter but wrong HMAC
        log_metrics(latency, "impersonation", "rejected")
    else:
        # fallback (rare edge case)
        log_metrics(latency, "mitm", "rejected")


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



# import socket
# import time
# import random

# from core.config import HOST, PORT, SECRET_KEY, LATENCY_THRESHOLD
# from core.crypto import generate_hmac
# from core.logger import log_metrics

# last_counter = 0

# def handle_client(conn):
#     global last_counter

#     # 🔴 STEP 1: generate challenge
#     challenge = str(random.randint(1000, 9999))
#     conn.send(challenge.encode())

#     start_time = time.time()

#     data = conn.recv(1024).decode()
#     end_time = time.time()

#     latency = end_time - start_time

#     try:
#         counter, received_hmac = data.split("|")
#         counter = int(counter)
#     except:
#         conn.send(b"INVALID FORMAT")
#         return

#     message = str(counter) + challenge
#     expected_hmac = generate_hmac(SECRET_KEY, message)

#     # 🔴 RELAY DETECTION
#     if latency > LATENCY_THRESHOLD:
#         conn.send(b"RELAY DETECTED")
#         log_metrics(latency, "relay", "rejected")
#         return

#     # 🔴 REPLAY DETECTION
#     if counter <= last_counter:
#         conn.send(b"REPLAY DETECTED")
#         log_metrics(latency, "replay", "rejected")
#         return

#     # 🔴 HMAC VALIDATION
#     if received_hmac == expected_hmac:
#         last_counter = counter
#         conn.send(b"SUCCESS")
#         log_metrics(latency, "normal", "success")
#     else:
#         conn.send(b"INVALID HMAC")
#         log_metrics(latency, "normal", "rejected")


# def start_server():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
#         server.bind((HOST, PORT))
#         server.listen()
#         print("Receiver running...")

#         while True:
#             conn, addr = server.accept()
#             with conn:
#                 handle_client(conn)


# if __name__ == "__main__":
#     start_server()