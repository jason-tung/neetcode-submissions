class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        def dfs(i):
            for j in d[i]:
                if j not in visited:
                    visited.add(j)
                    dfs(j)
            return 1
        return sum(dfs(i) if i not in visited else 0 for i in range(n))