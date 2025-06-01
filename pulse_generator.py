import numpy as np
import json

n = 100

pulses = [round(np.random.uniform(0.3, 0.7), 6)]

for _ in range(n - 1):
    prev = pulses[-1]
    change = np.random.uniform(-0.08, 0.08)
    new_pulse = round(np.clip(prev + change, 0, 1), 6)
    pulses.append(new_pulse)


with open("simulated_brain_pulses.json", "w") as f:
    json.dump(pulses, f, indent=2)

