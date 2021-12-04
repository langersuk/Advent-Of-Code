with open('input.txt') as f:
    bordingPasses = [x.strip() for x in f]


allIds = []


def part1(boardingPasses):
    for seat in boardingPasses:
        row = seat[:7]
        column = seat[7:]

        row = ''.join(['0' if x == 'F' else '1' for x in row])
        row = int(row, 2)

        column = ''.join(['0' if x == 'L' else '1' for x in column])
        column = int(column, 2)

        # print(row, column)
        id = (row*8)+column
        allIds.append(id)

    allIds.sort()
    return allIds[-1]


def part2(allIds: list):
    allIds.reverse()
    for i, id in enumerate(allIds):
        if allIds[i+1] == id-2:
            return(id-1)


print(part1(bordingPasses))
print(part2(allIds))
