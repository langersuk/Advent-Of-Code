with open('input.txt') as f:
    forms = f.read().split('\n\n')


def part1(forms):
    forms = [group.replace('\n', '') for group in forms]
    forms = [set([letter for letter in group]) for group in forms]
    return sum([len(group) for group in forms])

def part2(forms: list):
    forms = [group.split('\n') for group in forms]
    forms = [[set([letter for letter in person])
              for person in group] for group in forms]
    forms = [group[0].intersection(*group[1:]) for group in forms]
    return sum([len(group) for group in forms])

print(part1(forms))
print(part2(forms))
