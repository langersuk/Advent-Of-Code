import re

with open('input.txt') as f:
    slopes = [x.strip() for x in f]


def part1(slopes, x=3, y=1):
    mod = len(slopes[0])
    slope = slopes[1:]
    trees = 0
    j = x
    for i in range(len(slope)):
        if (i+1) % y != 0:
            continue
        if slope[i][j % mod] == '#':
            trees += 1
        j += x
    return trees


def part2():
    return (part1(slopes, 1, 1)
            * part1(slopes, 3, 1)
            * part1(slopes, 5, 1)
            * part1(slopes, 7, 1)
            * part1(slopes, 1, 2))


print(part1(slopes))
print(part2())
