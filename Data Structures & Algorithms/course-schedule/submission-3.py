class Node:
    def __init__(self, val):
        self.val = val
        self.prereqs = set()

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {}
        solved = set()
        for k in range(numCourses):
            d[k] = Node(k)
        for (a,b) in prerequisites:
            d[a].prereqs.add(d[b])
        def dfs(node):
            for k in node.prereqs:
                if k.val not in solved:
                    if k.val in visited:
                        return False
                    visited.add(k.val)
                    if not dfs(k):
                        return False
            solved.add(node.val)
            return True
        for n in range(numCourses):
            visited = set([n])
            if not dfs(d[n]):
                return False
        return True