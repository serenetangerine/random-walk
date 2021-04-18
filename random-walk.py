#!/usr/bin/env python3
#
## Generates walk objects and allows for either graphing a single walk or running an analysis of 
## how many walks have a distance less than a given distance for given walk lengths

## TODO
# Add animated graph argument and method


import argparse
import numpy
import random
import sys
from matplotlib import pyplot


class RandomWalk():
    def __init__(self, steps):
        self.steps = steps
        # initialize path start point
        self.path = {'x': [0], 'y': [0]}

        # generate walk
        for i in range(self.steps):
            (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            self.path['x'].append(self.path['x'][i] + dx)
            self.path['y'].append(self.path['y'][i] + dy)

        # set end coordinates
        x = self.path['x'][len(self.path['x']) - 1]
        y = self.path['y'][len(self.path['y']) - 1]
        self.last_position = (x, y)

        # calculate distance
        self.distance = abs(x) + abs(y)
    
    # draw a graph of the walk object
    def draw_graph(self):
        fig = pyplot.figure()
        pyplot.plot(self.path['x'], self.path['y'], color='green')
        pyplot.show()


def averageDistance(max_steps, distance, sample_size):
    for i in range(max_steps + 1):
        count = 0
        for j in range(sample_size + 1):
            walk = RandomWalk(i)
            if walk.distance <= distance:
                count += 1
        percent = float((count / sample_size) * 100) 
        print('%s steps:\t %s ' % (i, percent) + '%')


def distributionDistance(steps, sample_size):
    distances = []
    for i in range(sample_size + 1):
        walk = RandomWalk(steps)
        distances.append(walk.distance)
    bins = numpy.arange(min(distances), max(distances) + 1, 1)
    pyplot.hist(distances, bins=bins, density=True)
    pyplot.show()


def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', '-s', help='Number of Max steps to analyze', type=int)
    parser.add_argument('--sample', '-n', help='Sample size to analyze for each step', type=int)
    parser.add_argument('--distance', '-d', help='Max distance for analysis', type=int)

    parser.add_argument('--graph', '-g', help='Flag to toggle drawing a static graph', action='store_true')

    parser.add_argument('--averageDistance', '-aA', help='Flag to toggle average distance analysis', action='store_true')
    parser.add_argument('--distributionDistance', '-aD', help='Flag to toggle distance distribution analysis', action='store_true')
    
    args = parser.parse_args()
    return args


def main():
    args = getArguments()

    if args.graph and args.steps:
        if args.sample or args.distance:
            print('InvalidArgument: --sample or --distance are not supported with --graph')
            sys.exit(1)

        print('Generating walk with %s steps...\n' % (args.steps))
        walk = RandomWalk(args.steps)
        print('Walk sequence generated!\nDistance: %s\n\nGenerating graph...' % (walk.distance))
        walk.draw_graph()
        print('Done!')
        sys.exit(0)

    elif args.steps and args.sample and args.distance and args.averageDistance:
        if args.graph:
            print('Invalid Argument: --graph is not not supported with analysis.')
            sys.exit(1)

        averageDistance(args.steps, args.distance, args.sample)
        sys.exit(0)

    elif args.steps and args.sample and args.distributionDistance:
        if args.graph or args.distance or args.averageDistance:
            print('Invalid Arguments: <write error message later>')
            sys.exit(1)

        distributionDistance(args.steps, args.sample)
        sys.exit(0)

    else:
        print('Invalid Arguments: use -h for help.')
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
