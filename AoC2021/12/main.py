import networkx as nx

with open('input.txt') as f:
    paths = [tuple(path.strip().split('-')) for path in f]

G = nx.Graph()
G.add_edges_from(paths)

def part1(node='start', seenPaths = set()):
    total = 0
    if node == 'end':
        return 1
    if node in seenPaths:
        return 0
    path = seenPaths.copy()
    if node.islower():
        path.add(node)
    for point in G[node]:
        total += part1(point, path)
    return total
    
def part2(node='start', seenPaths = set(), seenOnce = False):
    total = 0
    if node == 'end':
        return 1
    if node in seenPaths:
        if seenOnce:
            return 0
        else:
            if node == 'start':
                return 0
            seenOnce = True
    path = seenPaths.copy()
    if node.islower():
        path.add(node)
    for point in G[node]:
        total += part1(point, path, seenOnce)
    return total

print(part1())
print(part2())