"""
Create some sample animation frames for testing
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)

fig, ax = plt.subplots(figsize=(4, 3))
line, = plt.plot(x, np.sin(x), '-b', lw=2)
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)

for i in range(100):
    line.set_data(x, np.cos(i * 0.02 * np.pi) * np.sin(x - i * 0.02 * np.pi))
    fig.savefig('frames/frame%.03i.png' % (i + 1))
