import datetime

def log(event):
    with open("logs/system.log", "a") as f:
        f.write(f"{datetime.datetime.now()} | {event}\n")

def log_metrics(latency, attack_type, result):
    with open("logs/latency_results.csv", "a") as f:
        f.write(f"{latency},{attack_type},{result}\n")



# import datetime

# def log(event, file="logs/system.log"):
#     with open(file, "a") as f:
#         f.write(f"{datetime.datetime.now()} | {event}\n")