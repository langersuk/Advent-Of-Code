with open('input.txt') as f:
    nums = [[int(y) for y in x.split("\n")] for x in f.read().split("\n\n")]

def part1(nums):
    list = [sum(num) for num in nums]
    return max(list)

def part2(nums):
    list = [sum(num) for num in nums]
    list.sort(reverse=True)
    return sum(list[:3])

print(part1(nums))
print(part2(nums))