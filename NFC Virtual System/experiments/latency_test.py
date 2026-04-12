import socket
import time

from core.config import HOST, PORT

samples = []

for _ in range(20):
    start = time.time()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.recv(1024)

    end = time.time()

    latency = end - start
    samples.append(latency)

    time.sleep(0.2)

print("\nLatency Samples:")
for s in samples:
    print(s)

print("\nAverage Latency:", sum(samples) / len(samples))





# import socket
# import time

# from core.config import HOST, PORT

# samples = []

# for _ in range(20):
#     start = time.time()

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
#         client.connect((HOST, PORT))
#         client.recv(1024)

#     end = time.time()

#     latency = end - start
#     samples.append(latency)

#     time.sleep(0.2)

# print("\nLatency Samples:")
# for s in samples:
#     print(s)

# print("\nAverage Latency:", sum(samples) / len(samples))