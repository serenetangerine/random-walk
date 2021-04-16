#!/usr/bin/env python3


import random
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation


def randomWalk(steps):
    """Returns coordinates after given number of steps in a cartesian coordinate system."""
    path = {'x': [], 'y': []}
    x, y = 0, 0
    for i in range(steps):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
        path['x'].append(x)
        path['y'].append(y)
    return path


def walkDistance(x, y):
    return abs(x) + abs(y)


fig = pyplot.figure()
pyplot.style.use('classic')
path = randomWalk(1000)

x, y = [], []

def animate(i):
    x.append(path['x'][i])
    y.append(path['y'][i])
    print('(%s, %s)' % (str(x[i]), str(y[i])))
    pyplot.plot(x, y, color='green')

ani = FuncAnimation(fig, animate, interval=10)
pyplot.show()


