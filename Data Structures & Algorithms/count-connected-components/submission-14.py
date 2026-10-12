class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        d = defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        res = n
        def dfs(i):
            for j in d[i]:
                if j not in visited:
                    visited.add(j)
                    dfs(j)
            d[i] = []
            return 1
        return sum(dfs(i) if i not in visited else 0 for i in range(n))