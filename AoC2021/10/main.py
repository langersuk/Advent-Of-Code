import functools

with open('input.txt') as f:
    lines = [row.strip() for row in f]

pairs = {'[': ']', '{':'}', '<':'>', '(':')'}
openBrackets = ['[', '{', '<', '(']

corruptedLines = list()

def part1(lines):
    scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
    }
    corrupted = list()
    opening = list()
    for index,line in enumerate(lines):
        for bracket in line:
            if bracket in openBrackets:
                opening.append(bracket)
            else:
                if pairs[opening[-1]] == bracket:
                    opening.pop()
                else:
                    corrupted.append(bracket)
                    corruptedLines.append(index)
                    opening = []
                    break
        opening = []

    corrupted = [scores[bracket] for bracket in corrupted]
    return sum(corrupted)

def part2(lines):
    scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
    }
    points = []
    opening = list()
    lines = [line for index, line in enumerate(lines) if index not in corruptedLines]
    for line in lines:
        for bracket in line:
            if bracket in openBrackets:
                opening.append(bracket)
            else:
                opening.pop()
        opening.reverse()
        closing = [pairs[bracket] for bracket in opening]
        closing = [scores[bracket] for bracket in closing]
        closing.insert(0, 0)
        points.append(functools.reduce(lambda a, b: a*5+b, closing))
        opening = []

    points.sort()
    middle = int((len(points)-1)/2)
    return points[middle]

print(part1(lines))

print(part2(lines))
# print(lines)

