class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        tickets.sort(reverse=True)
        d = defaultdict(list)
        for a,b in tickets:
            d[a].append(b)
        def dfs(u):
            while d[u]:
                dfs(d[u].pop())
            res.append(u)
        dfs("JFK")
        return res[::-1]