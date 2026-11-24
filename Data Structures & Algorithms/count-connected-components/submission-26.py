class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(i):
            visited.add(i)
            for j in adj[i]:
                if j not in visited:
                    dfs(j)
        tot = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                tot += 1
        return tot