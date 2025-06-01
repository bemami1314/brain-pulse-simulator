import numpy as np
import json
import matplotlib.pyplot as plt

n = 100

pulses = [round(np.random.uniform(0.3, 0.7), 6)]

for _ in range(n - 1):
    prev = pulses[-1]
    change = np.random.uniform(-0.08, 0.08)
    new_pulse = round(np.clip(prev + change, 0, 1), 6)
    pulses.append(new_pulse)

# ذخیره پالس‌ها در فایل JSON
with open("simulated_brain_pulses.json", "w") as f:
    json.dump(pulses, f, indent=2)

# رسم نمودار
time = np.linspace(0, 1, n)
plt.plot(time, pulses, color='royalblue')
plt.title("Simulated Brain Pulses")
plt.xlabel("Time (s)")
plt.ylabel("Pulse Value")
plt.grid(True)

# ذخیره نمودار
plt.savefig("pulse_plot.png")
plt.close()

