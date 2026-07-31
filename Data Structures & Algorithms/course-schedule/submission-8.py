class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {}
        solved = set()
        for k in range(numCourses):
            d[k] = set()
        for (a,b) in prerequisites:
            d[b].add(a)
        def dfs(n):
            for k in d[n]:
                if k not in solved:
                    if k in visited:
                        return False
                    visited.add(k)
                    if not dfs(k):
                        return False
            solved.add(n)
            return True
        for n in range(numCourses):
            if n not in solved:
                visited = set([n])
                if not dfs(n):
                    return False
        return True