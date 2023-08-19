import json
from math import pi
import matplotlib.pyplot as plt

data = []

with open("./data.json", "r") as f:
    data = json.load(f)

data = data[:100000]

ratios = [entry["num_balls_circle"] / entry["num_balls_square"] if entry["num_balls_square"]!=0 else 0  for entry in data]

iterations = [entry["iteration"] for entry in data]

plt.figure(figsize=(10, 6))
plt.axhline(y=pi, color='r')
plt.plot(iterations, ratios, linestyle='-', color='b')
plt.title("Ratio vs. Iteration")
plt.xlabel("Iteration")
plt.ylabel("Ratio")
plt.grid(True)
plt.show()