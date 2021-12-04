import numpy as np

with open('input.txt') as f:
    bingoBoards = [x.strip() for x in f]
    drawnNumbers = [int(x) for x in bingoBoards[0].split(',')]
    bingoBoards = bingoBoards[1:]

boards = []
board = None
for row in bingoBoards:
    row = [int(x) for x in row.split()]
    if not row:
        if(board):
            board = np.asarray(board)
            boards.append(board)
        board = list()
    else:
        board.append(row)
board = np.asarray(board)
boards.append(board)

def part1(boards: list):

    def findWinningBoard():
        for i in range(len(drawnNumbers)-1):
            drawnSoFar = set(drawnNumbers[:i+1])
            for board in boards:
                for j in range(5):
                    if set(board[j]).issubset(drawnSoFar):
                        return board, drawnSoFar, i
                    if set(board[:,j]).issubset(drawnSoFar):
                        return board, drawnSoFar, i
    
    winningBoard, drawnSet, i = findWinningBoard()
    winningSet = set([num for row in winningBoard for num in row])
    return sum(winningSet.difference(drawnSet))*drawnNumbers[i]

def part2(boards: list):

    def findWinningBoard():
        for i in range(len(drawnNumbers)-1):
            drawnSoFar = set(drawnNumbers[:i+1])
            for index,board in enumerate(boards):
                for j in range(5):
                    if set(board[j]).issubset(drawnSoFar):
                        if len(boards) == 1:
                            return board, drawnSoFar, i
                        boards.pop(index)
                        return findWinningBoard()
                    if set(board[:,j]).issubset(drawnSoFar):
                        if len(boards) == 1:
                            return board, drawnSoFar, i
                        boards.pop(index)
                        return findWinningBoard()
    winningBoard, drawnSet, i = findWinningBoard()
    winningSet = set([num for row in winningBoard for num in row])
    return sum(winningSet.difference(drawnSet))*drawnNumbers[i]


print(part1(boards))

print(part2(boards))