class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        d = defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        def dfs(i):
            for v in d[i]:
                if v not in visited:
                    visited.add(v)
                    dfs(v)
            d[i] = []
        tot = 0
        for i in range(n):
            if i not in visited:
                tot += 1
                visited.add(i)
                dfs(i)
        return tot
            