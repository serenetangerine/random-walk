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
            

def getArguments():
    parser = argparse.ArgumentParser
    parser.add_argument('--steps', '-s', help='Number of steps for a walk', type=int)

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
