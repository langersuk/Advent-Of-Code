with open('input.txt') as f:
    allFish = f.readline().split(',')
    allFish = [int(fish) for fish in allFish]

def func(allFish: list, target = 256):
    fishByAge = [allFish.count(x) for x in range(9)]

    for day in range(target):
        newBorn = fishByAge[0]
        fishByAge = [fishByAge[i+1] for i,fish in enumerate(fishByAge[:-1])]
        fishByAge[6] += newBorn
        fishByAge.append(newBorn)
    return sum(fishByAge)

print(func(allFish, 80))
print(func(allFish, 256))