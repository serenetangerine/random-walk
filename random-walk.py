#!/usr/bin/env python3


import random


def randomWalk(steps):
    """Returns coordinates after given number of steps in a cartesian coordinate system."""
    x, y = 0, 0
    for i in range(steps):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)


def walkDistance(x, y):
    return abs(x) + abs(y)    


def main():
    (x, y) = randomWalk(25)
    distance = walkDistance(x, y)
    print('(%s, %s), %s' % (str(x), str(y), str(distance)))



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
