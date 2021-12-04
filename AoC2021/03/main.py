with open('input.txt') as f:
    diagReport = [x.strip() for x in f]
    diagReport = [[int(num) for num in line] for line in diagReport]

def part1(diagReport):
    average = len(diagReport)/2
    totals = [sum(num) for num in zip(*diagReport)]
    gamma = ''.join((['1' if num>average else '0' for num in totals ]))
    epsilon = ''.join(['1' if num<average else '0' for num in totals ])
    return int(gamma, 2)*int(epsilon, 2)

def part2(diagReport):
    oxy = diagReport
    co2 = diagReport

    for x in range(len(oxy[0])):
        average = len(oxy)/2
        total = sum(line[x] for line in oxy)
        oxy = list(filter(lambda line: line[x] == (total >= average), oxy))
        if len(oxy) == 1:
            break
    oxy = [str(num)for num in oxy[0]]
    oxy = ''.join(oxy)
    oxy = int(oxy, 2)

    for x in range(len(co2[0])):
        average = len(co2)/2
        total = sum(line[x] for line in co2)
        co2 = list(filter(lambda line: line[x] == (total < average), co2))
        if len(co2) == 1:
            break
    co2 = [str(num)for num in co2[0]]
    co2 = ''.join(co2)
    co2 = int(co2, 2)

    return oxy*co2

print(part1(diagReport))
print(part2(diagReport))
