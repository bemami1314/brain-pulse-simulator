import numpy as np
import matplotlib.pyplot as plt


n = 100

pulses = [np.random.uniform(0.3, 0.7)]

for _ in range(n - 1):
    prev = pulses[-1]
    change = np.random.uniform(-0.08, 0.08)
    new_pulse = np.clip(prev + change, 0, 1)
    pulses.append(new_pulse)


time = np.linspace(0, 1, n)
plt.plot(time, pulses)
plt.title("Natural-Like Brain Pulses")
plt.xlabel("Time (s)")
plt.ylabel("Pulse Value")
plt.grid(True)
plt.savefig("pulse_plot.png")


with open("simulated_brain_pulses.json", "w") as f:
    for pulse in pulses:
        f.write(f"{pulse:.4f}\n")

