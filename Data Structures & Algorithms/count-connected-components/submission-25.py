class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(i):
            if i not in visited:
                visited.add(i)
                for j in adj[i]:
                    if j not in visited:
                        dfs(j)
                return 1
            return 0
        return sum(dfs(i) for i in range(n))