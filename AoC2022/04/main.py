with open('input.txt') as f:
    nums = [[list(range(int(y.split("-")[0]), int(y.split("-")[1])+1))
             for y in x.strip().split(",")] for x in f]


def part1(nums):
    total = 0
    for num in nums:
        if len(set(num[0]).intersection(set(num[1]))) == len(num[0]) or len(set(num[0]).intersection(set(num[1]))) == len(num[1]):
            total += 1
    return total


def part2(nums):
    total = 0
    for num in nums:
        if len(set(num[0]).intersection(set(num[1]))) > 0:
            total += 1
    return total


print(part1(nums))
print(part2(nums))
