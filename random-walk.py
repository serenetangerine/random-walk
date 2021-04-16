#!/usr/bin/env python3


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


mywalk = RandomWalk(1000)
print('Last Position: %s\t Distance: %s' % (mywalk.last_position, mywalk.distance))

#for i in range(51):
#    count = 0
#    for j in range(100000):
#        if walkDistance(randomWalk(i)) < 4:
#            count += 1
#    percent = float(count / 100000)
#    print('Steps: %s\t Distance: %s' % (str(i), str(percent)))

def analyze(max_steps, distance, sample_size):
    for i in range(max_steps):
        count = 0
        for j in range(sample_size):
            walk = RandomWalk(i)
            if walk.distance <= distance:
                count += 1
        percent = float((count / sample_size) * 100) 
        print('%s steps:\t %s' % (i, percent))


def main():
    analyze(51, 5, 10000)



if __name__ == '__main__':
    main()
