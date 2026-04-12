import subprocess
import time
import random

DURATION = 3600  # seconds (change anytime)

def run_once(mode):
    if mode == "normal":
        return subprocess.Popen(["python", "-m", "network.transmitter"])
    
    elif mode == "replay":
        return subprocess.Popen(["python", "-m", "attacks.replay_attacker"])
    
    elif mode == "relay":
        return subprocess.Popen(["python", "-m", "attacks.relay_attacker"])


def main():
    print("Starting Receiver...")
    receiver = subprocess.Popen(["python", "-m", "network.receiver"])
    time.sleep(2)

    start_time = time.time()

    print("\nRunning mixed experiments...")

    while time.time() - start_time < DURATION:
        mode = random.choice(["normal", "replay", "relay"])

        print(f"\n[RUNNING] {mode.upper()}")

        proc = run_once(mode)

        # let it run briefly
        time.sleep(3)

        proc.terminate()

    receiver.terminate()
    print("\nExperiment completed.")


if __name__ == "__main__":
    main()





# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("--mode", choices=["normal", "replay", "relay"])
# args = parser.parse_args()

# print(f"Running mode: {args.mode}")