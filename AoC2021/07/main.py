import math

with open('input.txt') as f:
    allCrabs = f.readline().split(',')
    allCrabs = [int(crab) for crab in allCrabs]


def part1(allCrabs):
    # bestposition = 0
    fuel = 9999999999
    for position in range(1000):
        if sum([abs(crab-position) for crab in allCrabs]) < fuel:
            fuel = sum([abs(crab-position) for crab in allCrabs])
            # bestposition = position
    return(fuel)

def part2(allCrabs):
    def summing(n):
        return (n*(n+1))/2

    # bestposition = 0
    fuel = 9999999999
    for position in range(1000):
        if sum([summing(abs(crab-position)) for crab in allCrabs]) < fuel:
            fuel = sum([summing(abs(crab-position)) for crab in allCrabs])
            bestposition = position
    # print(bestposition)
    return(int(fuel))

print(part1(allCrabs))
print(part2(allCrabs))