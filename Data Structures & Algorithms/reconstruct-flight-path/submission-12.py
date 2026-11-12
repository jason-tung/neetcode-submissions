class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for a,b in tickets:
            adj[a].append(b)
        for a in adj:
            adj[a].sort(reverse=True)
        res = []
        def dfs(i):
            while adj[i]:
                dfs(adj[i].pop())
            res.append(i)
            return res
        return dfs('JFK')[::-1]