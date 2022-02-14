import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
line, = ax.plot(np.arange(10))  # <-- ax.boxplot(np.arange(10))
ax.set_ylim(0, 20)


def update(data):
    line.set_ydata(data)  # < -- line = ax.boxplot(data)? 
    return line,


def data_gen():
    i = 0
    while True:
        yield np.arange(10) + i
        i += .1
        i %= 10

ani = animation.FuncAnimation(fig, update, data_gen, interval=100)
plt.show()
