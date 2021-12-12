import numpy as np

with open('input.txt') as f:
    cavern = np.array([[int(octopus) for octopus in row.strip()] for row in f])

blooms = 0
def part1(cavern, steps=100):
    def bloom(i,j):
        global blooms 
        if cavern[i][j] >= 10:
            cavern[i][j] = 0
            blooms +=1
            if i > 0:
                if cavern[i-1][j] != 0:
                    cavern[i-1][j] += 1 #up
                    bloom(i-1, j)
                if j > 0:
                    if cavern[i-1][j-1] != 0:
                        cavern[i-1][j-1] += 1 #up-left
                        bloom(i-1,j-1)
                if j < len(cavern[0])-1:
                    if cavern[i-1][j+1] != 0:
                        cavern[i-1][j+1] += 1 #up-right
                        bloom(i-1, j+1)                        
            if i < len(cavern)-1:
                if cavern[i+1][j] != 0:
                    cavern[i+1][j] += 1 #down
                    bloom(i+1, j)
                if j > 0:
                    if cavern[i+1][j-1] != 0:
                        cavern[i+1][j-1] += 1 #down-left
                        bloom(i+1, j-1)
                if j < len(cavern[0])-1:
                    if cavern[i+1][j+1] != 0:
                        cavern[i+1][j+1] += 1 #down-right
                        bloom(i+1, j+1)
            if j > 0:
                if cavern[i][j-1] != 0:
                    cavern[i][j-1] += 1 #left
                    bloom(i, j-1)
            if j < len(cavern[0])-1:
                if cavern[i][j+1] != 0:
                    cavern[i][j+1] += 1 #right
                    bloom(i, j+1)


    for n in range(steps):
        cavern = np.array([[octopus +1 for octopus in row] for row in cavern])
        for i in range(len(cavern)):
            for j in range(len(cavern[0])):
                bloom(i,j)
    return blooms

def part2(cavern):
    def bloom(i,j):
        global blooms 
        if cavern[i][j] >= 10:
            cavern[i][j] = 0
            blooms +=1
            if i > 0:
                if cavern[i-1][j] != 0:
                    cavern[i-1][j] += 1 #up
                    bloom(i-1, j)
                if j > 0:
                    if cavern[i-1][j-1] != 0:
                        cavern[i-1][j-1] += 1 #up-left
                        bloom(i-1,j-1)
                if j < len(cavern[0])-1:
                    if cavern[i-1][j+1] != 0:
                        cavern[i-1][j+1] += 1 #up-right
                        bloom(i-1, j+1)                        
            if i < len(cavern)-1:
                if cavern[i+1][j] != 0:
                    cavern[i+1][j] += 1 #down
                    bloom(i+1, j)
                if j > 0:
                    if cavern[i+1][j-1] != 0:
                        cavern[i+1][j-1] += 1 #down-left
                        bloom(i+1, j-1)
                if j < len(cavern[0])-1:
                    if cavern[i+1][j+1] != 0:
                        cavern[i+1][j+1] += 1 #down-right
                        bloom(i+1, j+1)
            if j > 0:
                if cavern[i][j-1] != 0:
                    cavern[i][j-1] += 1 #left
                    bloom(i, j-1)
            if j < len(cavern[0])-1:
                if cavern[i][j+1] != 0:
                    cavern[i][j+1] += 1 #right
                    bloom(i, j+1)

    step=0
    while not np.all((cavern == 0)):
        step += 1
        cavern = np.array([[octopus +1 for octopus in row] for row in cavern])
        for i in range(len(cavern)):
            for j in range(len(cavern[0])):
                bloom(i,j)
    return step

print(part1(cavern))
print(part2(cavern))