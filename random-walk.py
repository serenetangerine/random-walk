#!/usr/bin/env python3


import argparse
import random
import sys
from matplotlib import pyplot


class RandomWalk():
    def __init__(self, steps):
        self.steps = steps
        self.path = {'x': [0], 'y': [0]}

        for i in range(self.steps):
            (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            self.path['x'].append(self.path['x'][i] + dx)
            self.path['y'].append(self.path['y'][i] + dy)

        x = self.path['x'][len(self.path['x']) - 1]
        y = self.path['y'][len(self.path['y']) - 1]
        self.last_position = (x, y)

        self.distance = abs(x) + abs(y)
    
    def draw_graph(self):
        fig = pyplot.figure()
        pyplot.plot(self.path['x'], self.path['y'], color='green')
        pyplot.show()


def analyze(max_steps, distance, sample_size):
    for i in range(max_steps + 1):
        count = 0
        for j in range(sample_size + 1):
            walk = RandomWalk(i)
            if walk.distance <= distance:
                count += 1
        percent = float((count / sample_size) * 100) 
        print('%s steps:\t %s ' % (i, percent) + '%')


def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', '-s', help='Number of Max steps to analyze', type=int)
    parser.add_argument('--sample', '-n', help='Sample size to analyze for each step', type=int)
    parser.add_argument('--distance', '-d', help='Max distance for analysis', type=int)
    parser.add_argument('--graph', '-g', help='Flag to toggle drawing a static graph', action='store_true')
    
    args = parser.parse_args()
    return args


def main():
    args = getArguments()
    if args.graph:
        if args.sample or args.distance:
            print('Invalid arguments: --sample and --distance are not compatible with --graph.')
            sys.exit(1)
        elif not args.steps:
            print('Invalid arguments: --graph and --steps must both be specified.')
            sys.exit(1)
        else:
            walk = RandomWalk(args.steps)
            walk.draw_graph()
            sys.exit(0)
    elif args.steps and args.sample and args.distance:
        analyze(args.steps, args.distance, args.sample)
        sys.exit(0)
    else:
        print('Invalid arguments: either --steps and --graph or --steps, --distance, and --sample must be specified.')
        sys.exit(1)
        


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Script killed by user.')
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)
