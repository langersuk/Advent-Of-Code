import numpy as np

with open('input.txt') as f:
    data = [row.strip() for row in f]

folds = data[data.index('')+1:]
folds = [fold.split('=') for fold in folds]
folds = [{fold[0].replace('fold along ',''): int(fold[1])} for fold in folds]


dots = data[:data.index('')]
dots = [{'x':int(num[0]), 'y':int(num[1])} for num  in [dot.split(',') for dot in dots]]

width = max({dot['x'] for dot in dots})+1
height = max({dot['y'] for dot in dots})+1

arr = np.zeros((height, width))

for dot in dots:
    arr[dot['y'], dot['x']] = 1

def folding(arr, limit = None):
    for fold in folds[:limit]:
        if list(fold.keys())[0] == 'y':
            arr = np.delete(arr, fold['y'], 0)
            old, new = np.vsplit(arr, 2)
            new = np.flip(new, 0)
            arr = np.add(new, old)
        if list(fold.keys())[0] == 'x':
            arr = np.delete(arr, fold['x'], 1)
            old, new = np.hsplit(arr, 2)
            new = np.flip(new, 1)
            arr = np.add(new, old)
    print(arr)
    return np.count_nonzero(arr)
    
print(folding(arr, 1))
print(folding(arr))

# RLBCJGLU
# [[ 6.  2.  9.  0.  0.  6.  0.  0.  0.  0.  8. 22. 10.  0.  0.  0.  6.  3.   0.  0.  0.  0.  2.  9.  0.  0. 16. 28.  0.  0. 13.  0.  0.  0.  0.  4.   0.  0.  8.  0.]
#  [ 6.  0.  0. 16.  0.  7.  0.  0.  0.  0.  3.  0.  0.  4.  0.  3.  0.  0.   1.  0.  0.  0.  0. 13.  0.  7.  0.  0.  6.  0. 18.  0.  0.  0.  0. 13.   0.  0. 10.  0.]
#  [ 8.  0.  0. 10.  0. 18.  0.  0.  0.  0.  9.  7.  3.  0.  0.  5.  0.  0.   0.  0.  0.  0.  0.  9.  0. 30.  0.  0.  0.  0.  8.  0.  0.  0.  0. 20.   0.  0.  2.  0.]
#  [ 4. 10.  8.  0.  0.  3.  0.  0.  0.  0.  5.  0.  0.  8.  0. 36.  0.  0.   0.  0.  0.  0.  0. 16.  0.  5.  0.  3. 14.  0. 11.  0.  0.  0.  0.  9.   0.  0.  8.  0.]
#  [ 3.  0.  4.  0.  0.  1.  0.  0.  0.  0.  8.  0.  0.  6.  0. 10.  0.  0.  12.  0.  6.  0.  0.  8.  0.  4.  0.  0. 15.  0.  7.  0.  0.  0.  0.  8.   0.  0. 25.  0.]
#  [ 7.  0.  0.  5.  0.  6.  4.  6.  2.  0. 13.  3.  3.  0.  0.  0. 18. 22.   0.  0.  0.  8.  3.  0.  0.  0.  3.  7.  4.  0.  1.  6. 10.  6.  0.  0.  29. 12.  0.  0.]]