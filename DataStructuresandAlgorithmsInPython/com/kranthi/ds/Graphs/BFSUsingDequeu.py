

from collections import deque

def BFSUsingDeque(graph):

    result = []
    if not graph:
        return result

    queue = deque(list(graph.keys())[0])
    visited = set()

    while queue:
        node = queue.popleft()
        if node not in visited:
            result.append(node)
            visited.add(node)
            queue.extend(graph[node])
    return result


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

print(BFSUsingDeque(graph))
