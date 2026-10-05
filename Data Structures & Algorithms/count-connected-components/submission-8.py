class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        def dfs(i):
            if i not in visited:
                visited.add(i)
                for k in d[i]:
                    if k not in visited:
                        dfs(k)
                return 1
            return 0
        return sum(dfs(i) for i in range(n))
