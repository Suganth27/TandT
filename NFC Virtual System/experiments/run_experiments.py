import subprocess
import time
import random

DURATION = 30  # total run time

ATTACKS = {
    "normal": ["python", "-m", "network.transmitter"],
    "replay": ["python", "-m", "attacks.replay_attacker"],
    "relay": ["python", "-m", "attacks.relay_attacker"],
    "impersonation": ["python", "-m", "attacks.impersonation_attacker"],
    "bruteforce": ["python", "-m", "attacks.bruteforce_attacker"],
    "mitm": ["python", "-m", "attacks.mitm_attacker"],
}


def run_phase(mode, duration=5):
    print(f"\n[RUNNING] {mode.upper()}")

    proc = subprocess.Popen(ATTACKS[mode])

    time.sleep(duration)

    proc.terminate()


def main():
    print("Starting Receiver...")
    receiver = subprocess.Popen(["python", "-m", "network.receiver"])
    time.sleep(2)

    start = time.time()

    modes = list(ATTACKS.keys())

    # 🔴 FORCE EACH ATTACK AT LEAST ONCE
    random.shuffle(modes)
    for mode in modes:
        run_phase(mode, 5)

    # 🔴 THEN RANDOM EXECUTION
    while time.time() - start < DURATION:
        mode = random.choice(modes)
        run_phase(mode, 5)

    receiver.terminate()
    print("\nExperiment completed.")


if __name__ == "__main__":
    main()





# import subprocess
# import time
# import random

# DURATION = 3600  # seconds (change anytime)

# def run_once(mode):
#     if mode == "normal":
#         return subprocess.Popen(["python", "-m", "network.transmitter"])
    
#     elif mode == "replay":
#         return subprocess.Popen(["python", "-m", "attacks.replay_attacker"])
    
#     elif mode == "relay":
#         return subprocess.Popen(["python", "-m", "attacks.relay_attacker"])


# def main():
#     print("Starting Receiver...")
#     receiver = subprocess.Popen(["python", "-m", "network.receiver"])
#     time.sleep(2)

#     start_time = time.time()

#     print("\nRunning mixed experiments...")

#     while time.time() - start_time < DURATION:
#         mode = random.choice(["normal", "replay", "relay"])

#         print(f"\n[RUNNING] {mode.upper()}")

#         proc = run_once(mode)

#         # let it run briefly
#         time.sleep(3)

#         proc.terminate()

#     receiver.terminate()
#     print("\nExperiment completed.")


# if __name__ == "__main__":
#     main()