import csv
import matplotlib.pyplot as plt
import os

ROOT = os.path.dirname(os.path.dirname(__file__))
log_file = os.path.join(ROOT, "logs", "latency_results.csv")

latencies = []

with open(log_file) as f:
    reader = csv.reader(f)

    for row in reader:
        if len(row) < 2:
            continue

        latency = float(row[1])
        latencies.append(latency)

print("Latencies collected:", latencies)

normal = []
relay = []

for l in latencies:
    if l < 1:
        normal.append(l)
    else:
        relay.append(l)

print("Total samples:", len(latencies))
print("Normal samples:", len(normal))
print("Relay samples:", len(relay))

if normal:
    print("Average normal latency:", sum(normal)/len(normal))

if relay:
    print("Average relay latency:", sum(relay)/len(relay))

plt.figure()

plt.scatter(range(len(normal)), normal, label="Normal Authentication")
plt.scatter(range(len(relay)), relay, label="Relay Attack")

plt.xlabel("Experiment Number")
plt.ylabel("Latency (seconds)")
plt.title("Authentication Latency Results")
plt.legend()

plt.show()