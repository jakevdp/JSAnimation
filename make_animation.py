import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from JSAnimation import HTMLWriter


fig = plt.figure(figsize=(4, 3))
ax = plt.axes(xlim=(0, 10), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 10, 1000)
    y = np.cos(i * 0.02 * np.pi) * np.sin(x - i * 0.02 * np.pi)
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)

# set embed_frames=True to embed base64-encoded frames directly in the HTML
anim.save('animation.html', writer=HTMLWriter(embed_frames=True))
