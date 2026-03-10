import csv
import time
import os

def log_latency(latency):

    log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(log_dir, exist_ok=True)

    file_path = os.path.join(log_dir, "latency_results.csv")

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([time.time(), latency])