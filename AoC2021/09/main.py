with open('input.txt') as f:
    caves = [[int(digit) for digit in row.strip()] for row in f]

def part1(caves):
    riskLevels = list()
    for i in range(len(caves)):
        for j in range(len(caves[0])):
            tube = caves[i][j]
            surroundingTubes = [
                caves[i-1][j] if i>0 else 9, #up
                caves[i+1][j] if i<len(caves)-1 else 9, #down
                caves[i][j-1] if j>0 else 9, #left
                caves[i][j+1] if j<len(caves[0])-1 else 9 #right
                ]
            if all(x > tube for x in surroundingTubes):
                riskLevels.append(tube+1)
    return sum(riskLevels)   


def part2(caves):
    basins = []
    sinks = []
    for i in range(len(caves)):
        for j in range(len(caves[0])):
            tube = caves[i][j]
            surroundingTubes = [
                caves[i-1][j] if i>0 else 9, #up
                caves[i+1][j] if i<len(caves)-1 else 9, #down
                caves[i][j-1] if j>0 else 9, #left
                caves[i][j+1] if j<len(caves[0])-1 else 9 #right
                ]
            if all(x > tube for x in surroundingTubes):
                basins.append([i,j])

    def basinSearch(basin):
        i, j = basin[0], basin[1]
        tube = caves[i][j]
        up = caves[i-1][j] if i>0 else 9
        down = caves[i+1][j] if i<len(caves)-1 else 9
        left = caves[i][j-1] if j>0 else 9
        right = caves[i][j+1] if j<len(caves[0])-1 else 9     
        if tube < up and up != 9:
            sink.append([i-1, j])
            basinSearch([i-1, j])
        if tube < down and down != 9:
            sink.append([i+1, j])
            basinSearch([i+1, j])
        if tube < left and left != 9:
            sink.append([i, j-1])
            basinSearch([i, j-1])
        if tube < right and right != 9:
            sink.append([i, j+1])
            basinSearch([i, j+1])
        caves[i][j] = 9

    for basin in basins:
        sink = []
        basinSearch(basin)
        sink.append(basin)
        sink = [list(i) for i in set(tuple(i) for i in sink)] #remove duplicates
        sinks.append(sink)

    sinks = [len(sink) for sink in sinks]
    sinks.sort()

    return sinks[-1]*sinks[-2]*sinks[-3]

print(part1(caves))
print(part2(caves))