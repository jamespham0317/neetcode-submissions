"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node

        oldToCopy = {}
        visited = set()

        def dfs(node):
            if node in visited: return
            oldToCopy[node] = Node(val = node.val)
            visited.add(node)

            for n in node.neighbors:
                dfs(n)

        dfs(node)

        for old in visited:
            copy = oldToCopy[old]
            for n in old.neighbors:
                copy.neighbors.append(oldToCopy[n])

        return oldToCopy[node]