import pandas as pd
import matplotlib.pyplot as plt

# 🔴 CLEAR OLD FIGURES
plt.close('all')

# 🔴 READ CSV (no header)
df = pd.read_csv(
    "logs/latency_results.csv",
    header=None,
    names=["latency", "attack_type", "result"]
)

# 🔴 CLEAN VALUES
df["latency"] = pd.to_numeric(df["latency"], errors="coerce")
df = df.dropna()

# 🔴 NORMALIZE LABELS (VERY IMPORTANT)
df["attack_type"] = df["attack_type"].str.replace(" attack", "")

# 🔴 COMPUTE
avg_latency = df.groupby("attack_type")["latency"].mean()
counts = df.groupby(["attack_type", "result"]).size().unstack(fill_value=0)

print("\nAverage Latency:\n", avg_latency)
print("\nDetection Summary:\n", counts)

# 🔴 SINGLE FIGURE
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

avg_latency.plot(kind="bar", ax=axes[0])
axes[0].set_title("Average Latency")
axes[0].set_ylabel("Seconds")

counts.plot(kind="bar", ax=axes[1])
axes[1].set_title("Detection Results")
axes[1].set_ylabel("Count")

plt.tight_layout()
plt.savefig("logs/final_output.png")
plt.show()





# import pandas as pd
# import matplotlib.pyplot as plt

# #VERY IMPORTANT: CLEAR OLD FIGURES
# plt.close('all')

# #MANUAL CLEANING (handles corrupted CSV)
# clean_rows = []

# with open("logs/latency_results.csv", "r") as f:
#     for line in f:
#         parts = line.strip().split(",")

#         if len(parts) == 3:
#             try:
#                 latency = float(parts[0])
#                 attack = parts[1]
#                 result = parts[2]
#                 clean_rows.append([latency, attack, result])
#             except:
#                 continue

# #create dataframe
# df = pd.DataFrame(clean_rows, columns=["latency", "attack_type", "result"])

# #HANDLE EMPTY DATA
# if df.empty:
#     print("❌ No valid data found in CSV. File is corrupted.")
#     exit()

# print("Cleaned Data:")
# print(df.head())

# #COMPUTATIONS
# avg_latency = df.groupby("attack_type")["latency"].mean()
# counts = df.groupby(["attack_type", "result"]).size().unstack(fill_value=0)

# print("\nAverage Latency:\n", avg_latency)
# print("\nDetection Summary:\n", counts)

# #CREATE NEW FIGURE (ENSURES FRESH WINDOW)
# plt.figure(figsize=(10, 4))

# #LATENCY GRAPH
# plt.subplot(1, 2, 1)
# avg_latency.plot(kind="bar")
# plt.title("Average Latency by Attack Type")
# plt.ylabel("Latency (seconds)")
# plt.xticks(rotation=0)

# #DETECTION GRAPH
# plt.subplot(1, 2, 2)
# counts.plot(kind="bar")
# plt.title("Attack Detection Results")
# plt.ylabel("Count")
# plt.xticks(rotation=0)

# plt.tight_layout()

# #SAVE IMAGE
# plt.savefig("logs/final_output.png")

# #SHOW ONLY THIS GRAPH
# plt.show()