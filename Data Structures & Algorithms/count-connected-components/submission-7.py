class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(u):
            if not visited[u]:
                visited[u] = True
                for v in adj[u]:
                    dfs(v)
                return 1
            return 0
        return sum(dfs(i) for i in range(n))
        