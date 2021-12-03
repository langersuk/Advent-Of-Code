import re

with open('input.txt') as f:
    passwords = [x.strip() for x in f]


def part1(passwords):
    validPasswords = list()
    for line in passwords:
        results = re.search(
            r'(?P<min>\d*)-(?P<max>\d*) (?P<letter>[a-zA-Z]): (?P<password>\w*)', line)
        min = int(results['min'])
        max = int(results['max'])
        letter = results['letter']
        password = results['password']
        result = re.findall(letter, password)
        if min <= len(result) <= max:
            validPasswords.append(line)
    return len(validPasswords)


def part2(passwords):
    validPasswords = list()
    for line in passwords:
        results = re.search(
            r'(?P<pos1>\d*)-(?P<pos2>\d*) (?P<letter>[a-zA-Z]): (?P<password>\w*)', line)
        print(results)
        pos1 = int(results['pos1'])
        pos2 = int(results['pos2'])
        letter = results['letter']
        password = results['password']
        if password[pos1-1] == letter != password[pos2-1] or password[pos2-1] == letter != password[pos1-1]:
            validPasswords.append(line)
    return len(validPasswords)


print(part1(passwords))
print(part2(passwords))
