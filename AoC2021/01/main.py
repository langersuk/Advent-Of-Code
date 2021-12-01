with open('input.txt') as f:
    nums = [int(x) for x in f]

def part1(nums):
    i = 0
    for ind, num in enumerate(nums):
        if num > nums[ind-1]:
            i += 1
    return i

def part2(nums):
    sums = list()
    for index in range(len(nums)):
        if index+2 > len(nums)-1:
            continue
        sums.append(nums[index]+nums[index+1]+nums[index+2])

    i = 0
    for index, number in enumerate(sums):
        if number > sums[index-1]:
            i += 1
    return i

print(part1(nums))
print(part2(nums))