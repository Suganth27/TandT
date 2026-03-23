import time
import socket

HOST = "127.0.0.1"
PORT = 65432

for _ in range(10):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        start = time.time()
        client.connect((HOST, PORT))
        client.recv(1024)
        client.send(b"1|test")
        client.recv(1024)
        end = time.time()

        print("Latency:", end - start)




# import csv
# import time
# import os

# def log_latency(latency):

#     log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
#     os.makedirs(log_dir, exist_ok=True)

#     file_path = os.path.join(log_dir, "latency_results.csv")

#     with open(file_path, "a", newline="") as f:
#         writer = csv.writer(f)
#         writer.writerow([time.time(), latency])