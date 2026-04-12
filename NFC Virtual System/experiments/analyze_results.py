import pandas as pd
import matplotlib.pyplot as plt

plt.close('all')

df = pd.read_csv(
    "logs/latency_results.csv",
    header=None,
    names=["latency", "attack_type", "result"]
)

df["latency"] = pd.to_numeric(df["latency"], errors="coerce")
df = df.dropna()

avg_latency = df.groupby("attack_type")["latency"].mean()
counts = df.groupby(["attack_type", "result"]).size().unstack(fill_value=0)

print("\nAverage Latency:\n", avg_latency)
print("\nDetection Summary:\n", counts)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

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

# # 🔴 CLEAR OLD FIGURES
# plt.close('all')

# # 🔴 READ CSV (no header)
# df = pd.read_csv(
#     "logs/latency_results.csv",
#     header=None,
#     names=["latency", "attack_type", "result"]
# )

# # 🔴 CLEAN VALUES
# df["latency"] = pd.to_numeric(df["latency"], errors="coerce")
# df = df.dropna()

# # 🔴 NORMALIZE LABELS (VERY IMPORTANT)
# df["attack_type"] = df["attack_type"].str.replace(" attack", "")

# # 🔴 COMPUTE
# avg_latency = df.groupby("attack_type")["latency"].mean()
# counts = df.groupby(["attack_type", "result"]).size().unstack(fill_value=0)

# print("\nAverage Latency:\n", avg_latency)
# print("\nDetection Summary:\n", counts)

# # 🔴 SINGLE FIGURE
# fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# avg_latency.plot(kind="bar", ax=axes[0])
# axes[0].set_title("Average Latency")
# axes[0].set_ylabel("Seconds")

# counts.plot(kind="bar", ax=axes[1])
# axes[1].set_title("Detection Results")
# axes[1].set_ylabel("Count")

# plt.tight_layout()
# plt.savefig("logs/final_output.png")
# plt.show()