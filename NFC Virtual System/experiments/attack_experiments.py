import subprocess
import time
import os

ROOT = os.path.dirname(os.path.dirname(__file__))

reader = os.path.join(ROOT, "devices", "reader_server.py")
phone = os.path.join(ROOT, "devices", "phone_client.py")
relay = os.path.join(ROOT, "attacks", "relay_attacker.py")
replay = os.path.join(ROOT, "attacks", "replay_attacker.py")

print("Starting reader...")

reader_process = subprocess.Popen(["python", reader])

time.sleep(3)

print("\n--- NORMAL AUTHENTICATION TEST ---")

for i in range(10):
    print("Normal auth:", i+1)
    subprocess.run(["python", phone])
    time.sleep(1)

print("\n--- REPLAY ATTACK TEST ---")

for i in range(5):
    print("Replay attack:", i+1)
    subprocess.run(["python", replay])
    time.sleep(1)

print("\n--- RELAY ATTACK TEST ---")

for i in range(5):
    print("Relay attack:", i+1)
    subprocess.run(["python", relay])
    time.sleep(1)

print("\nExperiments finished")

reader_process.terminate()