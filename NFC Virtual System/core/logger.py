import datetime

def log(event, file="logs/system.log"):
    with open(file, "a") as f:
        f.write(f"{datetime.datetime.now()} | {event}\n")