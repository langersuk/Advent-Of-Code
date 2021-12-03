import re
with open('input.txt') as f:
    instructions = [x.strip() for x in f]


def part1(instructions, x = 0, y = 0):
    for instruction in instructions:
        num = int(re.search(r'\d+', instruction).group())
        if 'forward' in instruction:
            x += num
        elif 'down' in instruction:
            y += num
        elif 'up' in instruction:
            y -= num
        else:
            print('error in: ' + instruction)
    return x*y


def part2(instructions, x = 0, y = 0, z = 0):
    for instruction in instructions:
        num = int(re.search(r'\d+', instruction).group())
        if 'forward' in instruction:
            x += num
            y += (num * z)
        elif 'down' in instruction:
            z += num
        elif 'up' in instruction:
            z -= num
        else:
            print('error in: ' + instruction)
    return x*y

print(part1(instructions))
print(part2(instructions))