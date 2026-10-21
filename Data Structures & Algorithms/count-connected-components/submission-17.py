class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        visited = set()
        def dfs(u):
            if u not in visited:
                visited.add(u)
                for v in d[u]:
                    dfs(v)
                return 1
            return 0
        return sum(dfs(u) for u in range(n))