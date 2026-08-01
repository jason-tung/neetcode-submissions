class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = [[] for _ in range(n)]
        for (a,b) in edges:
            d[a].append(b)
            d[b].append(a)
        visited = [False for _ in range(n)]
        def dfs(n, prev):
            visited[n] = True
            for k in d[n]:
                if k != prev:
                    if visited[k]:
                        return False 
                    if not dfs(k, n):
                        return False
            return True
        # dfs for acyclic check
        if not dfs(0, -1):
            return False
        # connectedness check
        return all(visited)
            