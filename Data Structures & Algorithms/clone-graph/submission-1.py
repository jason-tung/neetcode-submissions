"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node):
            if node not in visited:
                visited[node] = Node(node.val)
                visited[node].neighbors = [dfs(n) for n in node.neighbors]
                return visited[node]
            return visited[node]
        return dfs(node) if node else None