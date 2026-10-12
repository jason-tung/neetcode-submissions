class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        d = defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        res = n
        def dfs(i):
            if i not in visited:
                visited.add(i)
                for j in d[i]:
                    if j not in visited:
                        dfs(j)
                d[i] = []
                return 1
            return 0
        return sum(dfs(i) for i in range(n))