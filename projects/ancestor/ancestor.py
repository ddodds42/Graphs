import sys
sys.path.insert(1, '../graph/')
from graph import Graph

test_ancestors = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (8, 9), (11, 8), (10, 1)
]

def earliest_ancestor(ancestors, starting_node):
    famtree = Graph()
    for tup in ancestors:
        for i in tup:
            if i not in famtree.vertices:
                famtree.add_vertex(i)
        famtree.add_edge(tup[1], tup[0])
    ancestry = famtree.dft(starting_node)[1:]
     streams = {}
    for a in ancestry:
        stream = famtree.bfs(starting_node, a)
        gens = len(stream)
        if gens not in streams:
            streams.update({gens: [stream]})
        else:
            streams[gens].append(stream)
    if streams:
        branch = max(streams.keys())
        candidos = []
        for b in streams[branch]:
            candidos.append(b[-1])
        return min(candidos)
    return -1

print(earliest_ancestor(test_ancestors, 6))