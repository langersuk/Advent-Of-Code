import re

with open('input.txt') as f:
    data = f.read().split('\n\n')

newData = list()
for entry in data:
    newData.append(entry.replace('\n', ' '))


def part1(data, *mandatory, **optional):
    totalValid = 0
    regex = ''
    for field in mandatory:
        regex += f'(?=.*({field}))'
    optional = optional['optional'].split()
    for field in optional:
        regex += f'(?=.*({field}))?'
    for entry in data:
        valid = re.search(regex, entry)
        if valid:
            totalValid += 1
    return totalValid


def part2(data, *mandatory, **optional):
    totalValid = 0
    regex = ''
    for field in mandatory:
        regex += f'(?=.*({field}:(?P<{field}>\S*)))'
    optional = optional['optional'].split()
    for field in optional:
        regex += f'(?=.*({field}:(?P<{field}>\S*)))?'
    for entry in data:
        result = re.search(regex, entry)
        if not result:
            continue
        valid = [

            (1920 <= int(result['byr']) <= 2002),

            (2010 <= int(result['iyr']) <= 2020),

            (2020 <= int(result['eyr']) <= 2030),

            re.match(r'\d+[a-zA-Z]+', result['hgt']),

            re.search(r'[a-zA-Z]+', result['hgt']) and ((re.search(r'[a-zA-Z]+', result['hgt']).group() == 'cm' and 150 <= int(re.search(r'\d+', result['hgt']).group()) <= 193) or

                                                        (re.search(r'[a-zA-Z]+', result['hgt']).group() == 'in' and 59 <= int(re.search(r'\d+', result['hgt']).group()) <= 76)),

            re.match(r'#[0-9a-f]{6}', result['hcl']),

            result['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],

            re.match(r'^[0-9]{9}$', result['pid'])

        ]
        if all(valid):
            totalValid += 1

        # if not (1920 <= int(result['byr']) <= 2002):
        #     continue
        # if not (2010 <= int(result['iyr']) <= 2020):
        #     continue
        # if not (2020 <= int(result['eyr']) <= 2030):
        #     continue
        # if not re.search(r'\d+[a-zA-Z]+', result['hgt']):
        #     continue
        # if re.search(r'[a-zA-Z]+', result['hgt']).group() != 'cm' and re.search(r'[a-zA-Z]+', result['hgt']).group() != 'in':
        #     continue
        # if re.search(r'[a-zA-Z]+', result['hgt']).group() == 'cm' and not 150 <= int(re.search(r'\d+', result['hgt']).group()) <= 193:
        #     continue
        # if re.search(r'[a-zA-Z]+', result['hgt']).group() == 'in' and not 59 <= int(re.search(r'\d+', result['hgt']).group()) <= 76:
        #     continue
        # if not re.search(r'#[0-9a-f]{6}', result['hcl']):
        #     continue
        # if not result['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        #     continue
        # if not re.search(r'^[0-9]{9}$', result['pid']):
        #     continue
        # totalValid +=1

    return totalValid


print(part1(newData, 'byr', 'iyr', 'eyr', 'hgt',
            'hcl', 'ecl', 'pid', optional='cid'))
print(part2(newData, 'byr', 'iyr', 'eyr', 'hgt',
            'hcl', 'ecl', 'pid', optional='cid'))


# data = [[kv.split(':') for kv in entry.split()] for entry in data]


# data = [{key: value for key, value in entry} for entry in data]


# def part1():
#     mandatory = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
#     return [entry for entry in data if entry.keys() >= mandatory]


# def part2():

#     def validation(entry):
#         hgt = entry['hgt']
#         validation = [
#             1920 <= int(entry['byr']) <= 2002,
#             2010 <= int(entry['iyr']) <= 2020,
#             2020 <= int(entry['eyr']) <= 2030,
#             150 <= int(hgt.strip('cm')) <= 193 if hgt.endswith('cm')
#             else 59 <= int(hgt.strip('in')) <= 76 if hgt.endswith('in')
#             else False,
#             re.match(r'#[0-9a-f]{6}', entry['hcl']),
#             entry['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
#             re.match(r'^[0-9]{9}$', entry['pid'])
#         ]
#         return all(validation)

#     return len([entry for entry in part1() if validation(entry)])

# print(len(part1()))
# print(part2())
