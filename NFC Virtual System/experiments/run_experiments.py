import subprocess
import time
import random

DURATION = 3600  # total experiment time in seconds

ATTACKS = {
    "normal": ["python", "-m", "network.transmitter"],
    "replay": ["python", "-m", "attacks.replay_attacker"],
    "relay": ["python", "-m", "attacks.relay_attacker"],
    "impersonation": ["python", "-m", "attacks.impersonation_attacker"],
    "bruteforce": ["python", "-m", "attacks.bruteforce_attacker"],
    "mitm": ["python", "-m", "attacks.mitm_attacker"],
}


def run_once(mode):
    proc = subprocess.Popen(ATTACKS[mode])
    proc.wait()  # wait for exactly one execution


def main():
    print("Starting Receiver...")
    receiver = subprocess.Popen(["python", "-m", "network.receiver"])
    time.sleep(2)

    print("\nRunning random time-based experiment...\n")

    start_time = time.time()

    modes = list(ATTACKS.keys())

    while time.time() - start_time < DURATION:
        mode = random.choice(modes)

        print(f"[RUNNING] {mode.upper()}")

        run_once(mode)

        # random gap between requests (controls distribution)
        time.sleep(random.uniform(0.5, 1.5))

    receiver.terminate()
    print("\nExperiment completed.")


if __name__ == "__main__":
    main()