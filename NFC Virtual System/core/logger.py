from datetime import datetime

def log_metrics(latency, attack_type, result):
    timestamp = datetime.now()

    # CSV
    with open("logs/latency_results.csv", "a") as f:
        f.write(f"{latency},{attack_type},{result}\n")

    # SYSTEM LOG (DETAILED)
    with open("logs/system.log", "a") as f:
        f.write(
            f"{timestamp} | TYPE={attack_type.upper()} | RESULT={result.upper()} | LATENCY={latency:.6f}\n"
        )




# def log_metrics(latency, attack_type, result):
#     with open("logs/latency_results.csv", "a") as f:
#         f.write(f"{latency},{attack_type},{result}\n")