#!/usr/bin/env python3


import argparse
import random
import sys
from matplotlib import pyplot


class RandomWalk():
    def __init__(self, steps):
        self.steps = steps
        self.path = [0]

        for i in range(self.steps):
            dx = random.choice([1, -1])
            self.path.append(self.path[i] + dx)
        
        self.last_position = self.path[len(self.path) - 1]
        self.distance = self.last_position

    def draw_graph(self):
        pass
            

def averageDistance(max_steps, distance, sample_size):
    for i in range(max_steps + 1):
        count = 0
        for j in range(sample_size + 1):
            walk = RandomWalk(i)
            if walk.distance <= distance:
                count += 1
            percent = float((count / sample_size) * 100)
            print(%s steps:\t %s ' % (i, percent) + '%')


def getArguments():
    parser = argparse.ArgumentParser
    parser.add_argument('--steps', '-s', help='Number of steps for a walk', type=int)
    parser.add_argument('--sample', '-n', help='Sample size to analyze for each step', type=int)
    parser.add_argument('--distance', '-d', help='Max distance for analysis', type=int)

    parser.add_argument('--averageDistance', '-aA', help='Flag to toggle average distance analysis', action='store_true')
    parser.add_argument('--distributionDistance', '-aD', help='Flag to toggle distance distribution analysis', action='store_true')

    args = parser.parse_args()
    return args


def main():
    args = getArguments

    if args.steps:
        walk = RandomWalk(args.steps)
        print(walk.distance)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Script terminated by user.')
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
