"""
Given the root of a binary tree, the value of a target node target, and an integer k,
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
"""
from collections import deque, defaultdict

class Solution(object):
    def __init__(self):
        self.parent_Map = {}

    def buildParent(self, node, parent):
        if not node:
            return

        self.parent_map[node] = parent
        self.buildParent(node.left, node)
        self.buildParent(node.right, node)

    def findKDistanceNodes(self, root, target, k):
        self.buildParent(root, None)

        visited = set()
        queue = deque()
        queue.append((target, 0)) # (node, distance)
        visited.add(target)

        result = []

        while queue:
            node, distance = queue.popleft()
            if distance == k:
                result.append(node)

            elif distance < k:
                for nb in [node.left, node.right, self.parent_Map[node]]:
                    if nb and nb not in visited:
                        queue.append((nb, distance + 1))
                        visited.add(nb)

        return result
