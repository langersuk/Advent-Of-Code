from os import path
import re

with open('input.txt') as f:
    rules = [x.strip() for x in f]

bags = {}
for l in rules:
    bag, contains = l.split('contain')
    bag = bag.replace(' bags', '')
    bags[bag] = contains
answer = set()                      # Bags containing 'shiny gold'
q = ['shiny gold']                  # Work queue for traversing bags
while len(q) != 0:
    current = q.pop(0)
    for bag in bags:
        if bag in answer:             # Skip if already counted.
            continue
        if current in bags[bag]:      # If bag contains current-bag,
            q.append(bag)             # add to queue and answer
            answer.add(bag)
print ("Answer part 1: %d" % len(answer))


def part1(rules, myBag):
    rules = [rule.split(' contain ') for rule in rules]
    mainBags = [rule[0].strip('s') for rule in rules]
    contents = [rule[1].split(', ') for rule in rules]

    def modifyBag(bag):
        if not re.match(r'(?P<num>\d) (?P<bag>.+?bag)', bag):
            return None
        else:
            return re.search(r'(?P<num>\d) (?P<bag>.+?bag)', bag).group('bag')

    contents = [set([modifyBag(bag) for bag in bags]) for bags in contents]

    dictionary = dict(zip(mainBags, contents))

    bagsWhichContainMyBag = set()

    for (bag, contents) in dictionary.items():
        if myBag in contents:
            bagsWhichContainMyBag.add(bag)

    for (bag, contents) in dictionary.items():
        if len(bagsWhichContainMyBag.intersection(contents)) > 0:
            bagsWhichContainMyBag.add(bag)

    for (bag, contents) in dictionary.items():
        if len(bagsWhichContainMyBag.intersection(contents)) > 0:
            bagsWhichContainMyBag.add(bag)
    for (bag, contents) in dictionary.items():
        if len(bagsWhichContainMyBag.intersection(contents)) > 0:
            bagsWhichContainMyBag.add(bag)
    for (bag, contents) in dictionary.items():
        if len(bagsWhichContainMyBag.intersection(contents)) > 0:
            bagsWhichContainMyBag.add(bag)

    return len(bagsWhichContainMyBag)


print(part1(rules, 'shiny gold bag'))
