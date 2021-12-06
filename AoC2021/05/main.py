import numpy as np
with open('input.txt') as f:
    lines = [x.strip() for x in f]



lines = [[line.split(' -> ')] for line in lines]
lines = [[[rowCol.split(',') for rowCol in pair] for pair in line] for line in lines]
lines = [[[[int(num) for  num in rowCol] for rowCol in pair] for pair in line] for line in lines]
lines = [[{'x1': pair[0][0], 'y1': pair[0][1], 'x2': pair[1][0], 'y2': pair[1][1]} for pair in line] for line in lines]
lines = [line[0] for line in lines]

def day5(lines, part2):
    matrix = np.zeros((1000,1000))
    for line in lines:
        x1,x2,y1,y2 = line['x1'], line['x2'], line['y1'], line['y2']
        if x1==x2 and y1==y2:
            continue
        if x1 == x2:
            if y2>y1:
                y1,y2 = y1,y2+1
            else:
                y1,y2 = y2,y1+1
            for i in range(y1, y2):
                matrix[i][x1] += 1
            continue
        if y1 == y2:
            if x2>x1:
                x1,x2 = x1,x2+1
            else:
                x1,x2 = x2,x1+1
            for i in range(x1, x2):
                matrix[y1][i] += 1
            continue
        elif part2:
            steps = abs(x1-x2)
            dx = 1 if x2>x1 else -1
            dy = 1 if y2>y1 else -1           
            for i in range(steps+1):
                matrix[y1+dy*i][x1+dx*i] += 1
            continue


    overlap = 0
    for y in matrix:
        for x in y:
            if x > 1:
                overlap += 1
    return overlap

print(day5(lines, False))
print(day5(lines, True))
