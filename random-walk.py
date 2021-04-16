#!/usr/bin/env python3


import random
from matplotlib import pyplot


def randomWalk(steps):
    """Returns coordinates after given number of steps in a cartesian coordinate system."""
    pyplot.title('Random Walk')
    path = {'x': [], 'y': []}
    x, y = 0, 0
    for i in range(steps):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
        path['x'].append(x)
        path['y'].append(y)
    pyplot.plot(path['x'], path['y'])    
    pyplot.show()
    return (x, y)




def walkDistance(x, y):
    return abs(x) + abs(y)    


def main():
    (x, y) = randomWalk(10000)
    distance = walkDistance(x, y)
    print('(%s, %s), %s' % (str(x), str(y), str(distance)))



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
