import pandas as pd
import matplotlib.pyplot as plt

clean_rows = []

with open("logs/latency_results.csv", "r") as f:
    for line in f:
        parts = line.strip().split(",")

        # keep only valid rows
        if len(parts) == 3:
            try:
                latency = float(parts[0])
                attack = parts[1]
                result = parts[2]
                clean_rows.append([latency, attack, result])
            except:
                continue

# convert to dataframe
df = pd.DataFrame(clean_rows, columns=["latency", "attack_type", "result"])

# 🔴 HANDLE EMPTY CASE
if df.empty:
    print("❌ No valid data found in CSV. File is corrupted.")
    exit()

print("Cleaned Data:")
print(df.head())

# average latency
avg_latency = df.groupby("attack_type")["latency"].mean()

# detection counts
counts = df.groupby(["attack_type", "result"]).size().unstack(fill_value=0)

print("\nAverage Latency:\n", avg_latency)
print("\nDetection Summary:\n", counts)

# plot latency
avg_latency.plot(kind="bar")
plt.title("Average Latency by Attack Type")
plt.ylabel("Latency (seconds)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# plot detection
counts.plot(kind="bar")
plt.title("Attack Detection Results")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



# import csv
# import matplotlib.pyplot as plt
# import os

# ROOT = os.path.dirname(os.path.dirname(__file__))
# log_file = os.path.join(ROOT, "logs", "latency_results.csv")

# latencies = []

# with open(log_file) as f:
#     reader = csv.reader(f)

#     for row in reader:
#         if len(row) < 2:
#             continue

#         latency = float(row[1])
#         latencies.append(latency)

# print("Latencies collected:", latencies)

# normal = []
# relay = []

# for l in latencies:
#     if l < 1:
#         normal.append(l)
#     else:
#         relay.append(l)

# print("Total samples:", len(latencies))
# print("Normal samples:", len(normal))
# print("Relay samples:", len(relay))

# if normal:
#     print("Average normal latency:", sum(normal)/len(normal))

# if relay:
#     print("Average relay latency:", sum(relay)/len(relay))

# plt.figure()

# plt.scatter(range(len(normal)), normal, label="Normal Authentication")
# plt.scatter(range(len(relay)), relay, label="Relay Attack")

# plt.xlabel("Experiment Number")
# plt.ylabel("Latency (seconds)")
# plt.title("Authentication Latency Results")
# plt.legend()

# plt.show()