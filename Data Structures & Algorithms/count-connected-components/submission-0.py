class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        d = [[] for _ in range(n)]
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        def dfs(n):
            if n in visited:
                return 0
            visited.add(n)
            for k in d[n]:
                dfs(k)
            return 1
        total = 0
        for k in range(n):
            if k not in visited:
                total += dfs(k)
        return total