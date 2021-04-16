#!/usr/bin/env python3


import argparse
import random


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
    
    args = parser.parse_args()
    return args


def main():
    args = getArguments()
    analyze(args.steps, args.distance, args.sample)



if __name__ == '__main__':
    main()
