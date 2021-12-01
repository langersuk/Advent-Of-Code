with open('input.txt') as f:
    nums = [int(x) for x in f]


def part1(nums, target=2020):
    for index, firstDate in enumerate(nums):
        for secondDate in nums[index+1:]:
            if(firstDate+secondDate == target):
                return firstDate*secondDate


def part2(nums, target=2020):
    for index, firstDate in enumerate(nums):
        for secondDate in nums[index+1:]:
            for thirdDate in nums[index+2:]:
                if(firstDate+secondDate+thirdDate == target):
                    return firstDate*secondDate*thirdDate

print(part1(nums))
print(part2(nums))
