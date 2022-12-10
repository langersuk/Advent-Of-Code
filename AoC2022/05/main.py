with open('input.txt') as f:
    nums = [[y for y in next(f)[slice(1,34,4)]] for x in range(8)]
    stacks = [list(x) for x in zip(*nums)]
    lines = f.readlines()
    instructions = [x.strip().split()[slice(1,6,2)] for x in lines[2:]]
    # print(stacks)
    # print(instructions)


def part1(stacks: list[list[str]], instructions: list[list[str]]):
    for stack in stacks:
        while " " in stack:
            stack.remove(" ")
        stack.reverse()
    for instruction in instructions:
        num = int(instruction[0])
        frm = int(instruction[1])-1
        to = int(instruction[2])-1
        for x in range(num):
            stacks[to].append(stacks[frm].pop())
    return "".join([x[-1] for x in stacks])


def part2(stacks: list[list[str]], instructions: list[list[str]]):
    for stack in stacks:
        while " " in stack:
            stack.remove(" ")
        stack.reverse()
    for instruction in instructions:
        num = int(instruction[0])
        frm = int(instruction[1])-1
        to = int(instruction[2])-1
        move = stacks[frm][-num:]
        del stacks[frm][-num:]
        stacks[to] = stacks[to] + move
    return "".join([x[-1] for x in stacks])


# print(part1(stacks, instructions))
print(part2(stacks, instructions))
