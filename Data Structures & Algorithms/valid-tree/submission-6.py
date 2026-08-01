class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = [[] for _ in range(n)]
        for (a,b) in edges:
            d[a].append(b)
            d[b].append(a)
        solved = [False for _ in range(n)]
        visited = [False for _ in range(n)]
        def dfs(n, prev):
            for k in d[n]:
                if k != prev and not solved[n]:
                    if k in visited:
                        return False 
                    visited[k] = True
                    if not dfs(k, n):
                        return False
                    visited[k] = False
            solved[n] = True
            return True
        dfs(0, -1)
        return all(solved)
            