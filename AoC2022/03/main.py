with open('input.txt') as f:
    nums = [x.strip() for x in f]

def part1(nums):
    total = 0
    nums = [[[y for y in x[:len(x)//2]], [y for y in x[len(x)//2:]]] for x in nums]
    for num in nums:
        letter = [x for x in num[0] if x in num[1]][0]
        value = ord(letter)-96
        if value < 1:
            value += 32 + 26
        total += value
    return total

def part2(nums):
    total = 0
    nums = [[x for x in y] for y in nums]
    nums = [nums[i * 3:(i + 1) * 3] for i in range((len(nums) + 3 - 1) // 3 )]
    for num in nums:
            letter = [x for x in num[0] if x in num[1] and x in num[2]][0]
            value = ord(letter)-96
            if value < 1:
                value += 32 + 26
            total += value
    return total

print(part1(nums))
print(part2(nums))