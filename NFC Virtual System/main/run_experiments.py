import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--mode", choices=["normal", "replay", "relay"])
args = parser.parse_args()

print(f"Running mode: {args.mode}")




# import subprocess
# import time
# import os

# ROOT = os.path.dirname(os.path.dirname(__file__))

# reader_path = os.path.join(ROOT, "devices", "reader_server.py")
# phone_path = os.path.join(ROOT, "devices", "phone_client.py")

# print("Starting reader server...")

# reader = subprocess.Popen(["python", reader_path])

# time.sleep(3)  # give server time to start

# print("Running authentication experiments...")

# for i in range(20):

#     print("Authentication run:", i + 1)

#     try:
#         subprocess.run(["python", phone_path], check=True)
#     except subprocess.CalledProcessError:
#         print("Phone connection failed, retrying...")
#         time.sleep(2)
#         continue

#     time.sleep(1)

# print("Experiments completed.")

# reader.terminate()