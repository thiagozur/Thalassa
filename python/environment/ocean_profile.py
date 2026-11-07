import matplotlib.pyplot as plt
import numpy as np
from models.sound_speed import c_mackenzie

known_depths = np.array([0, 100, 500, 1000, 2000, 4000])
known_temp = np.array([20, 15, 8, 5, 3, 2.5])

depth = np.linspace(0, 4000, 8001)
salinity = np.full_like(depth, 35)
temperature = np.interp(depth, known_depths, known_temp)

sound_speed = np.array([c_mackenzie(d, s, t) for d, s, t in zip(depth, salinity, temperature)])

plt.figure(figsize=(6, 8))
plt.plot(sound_speed, depth)
plt.xticks([1475, 1500], [1475, 1500])
plt.xlim(1470, 1550)
plt.ylim(4000, 0)
plt.xlabel("Sound speed (m/s)")
plt.ylabel("Depth (m)")
plt.show()