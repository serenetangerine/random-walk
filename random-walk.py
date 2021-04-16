#!/usr/bin/env python3


import random


def randomWalk(steps):
    """Returns coordinates after given number of steps in a cartesian coordinate system."""
    x, y = 0, 0
    for i in range(steps):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return x, y


def walkDistance(path):
    return abs(path[0]) + abs(path[1])

#print(walkDistance(randomWalk(100)))

for i in range(51):
    count = 0
    for j in range(100000):
        if walkDistance(randomWalk(i)) < 4:
            count += 1
    percent = float(count / 100000)
    print('Steps: %s\t Distance: %s' % (str(i), str(percent)))
