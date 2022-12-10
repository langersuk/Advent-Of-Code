with open('input.txt') as f:
    nums = [x for x in f.readline()]
    # print(nums)


def part1(nums):
    for i in range(len(nums)-3):
        if len(set(nums[i:i+4])) == 4:
            return i + 4
    return "not found"


def part2(nums):
    for i in range(len(nums)-13):
        if len(set(nums[i:i+14])) == 14:
            return i + 14
    return "not found"


print(part1(nums))
print(part2(nums))
