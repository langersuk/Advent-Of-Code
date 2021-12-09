with open('input.txt') as f:
    entries = [x.strip() for x in f]

    entries = [entry.split(' | ') for entry in entries]

def part1(entries):
    outputs = ' '.join([entry[1] for entry in entries]).split()
    unique = list(filter(lambda num: len(num) in [2,3,4,7], outputs))
    return len(unique)

def part2(entries):
    inputs = ([entry[0].split() for entry in entries])
    outputs = ([entry[1].split() for entry in entries])
    outputs = [[[x for x in num] for num in entry] for entry in outputs]
    patterns = list()
    for i in range(len(entries)):
        no1 = next(num for num in inputs[i] if len(num)==2)
        no1 = set([char for char in no1])
        no4 = next(num for num in inputs[i] if len(num)==4)
        no4 = set([char for char in no4])
        no7 = next(num for num in inputs[i] if len(num)==3)
        no7 = set([char for char in no7])
        no8 = next(num for num in inputs[i] if len(num)==7)
        no8 = set([char for char in no8])

        no069 = [num for num in inputs[i] if len(num)==6]
        no06 = list()
        for num in no069:
            num = set([x for x in num])
            if len(no4.intersection(num)) == 4:
                no9 = num
            else:
                no06.append(num)

        for num in no06:
            num = set([x for x in num])
            if len(no7.intersection(num)) == 3:
                no0 = num
            else:
                no6 = num
        no235 = [num for num in inputs[i] if len(num)==5]
        no25 = list()
        for num in no235:
            num = set([x for x in num])
            if len(no1.intersection(num)) == 2:
                no3 = num
            else:
                no25.append(num)

        for num in no25:
            num = set([x for x in num])
            if len(no4.intersection(num)) == 2:
                no2 = num
            else:
                no5 = num
        no0 = list(no0)
        no0.sort()
        no1 = list(no1)
        no1.sort()
        no2 = list(no2)
        no2.sort()
        no3 = list(no3)
        no3.sort()
        no4 = list(no4)
        no4.sort()
        no5 = list(no5)
        no5.sort()
        no6 = list(no6)
        no6.sort()
        no7 = list(no7)
        no7.sort()
        no8 = list(no8)
        no8.sort()
        no9 = list(no9)
        no9.sort()

        patterns.append([no0, no1, no2, no3, no4, no5, no6, no7, no8, no9])

    total = 0
    for i, output in enumerate(outputs):
        num = []
        for digit in output:
            digit.sort()
            num.append(str(patterns[i].index(digit)))
        num = int(''.join(num))
        total += num
        
    return total
print(part1(entries))
print(part2(entries))
# 0 = 6
# 1 = 2
# 2 = 5
# 3 = 5
# 4 = 4
# 5 = 5
# 6 = 6
# 7 = 3
# 8 = 7
# 9 = 6