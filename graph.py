#!/usr/bin/env python3


import argparse
import random
from matplotlib import pyplot


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


def walkDistance(path):
    return abs(path['x'][len(path['x']) - 1]) + abs(path['y'][len(path['y']) - 1])


def drawGraph(path):
    fig = pyplot.figure()
    pyplot.style.use('classic')
    
    pyplot.plot(path['x'], path['y'], color='green')
    pyplot.show()


def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', '-s', help='Number of steps to generate', type=int)

    args = parser.parse_args()
    return args


def main():
    args = getArguments()
    walk = randomWalk(args.steps)
    distance = walkDistance(walk)

    print('Distance: %s' % (distance))
    drawGraph(walk)



if __name__ == '__main__':
    main()
