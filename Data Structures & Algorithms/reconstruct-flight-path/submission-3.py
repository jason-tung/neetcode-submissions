class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for a,b in tickets:
            d[a].append(b)
        for a in d:
            d[a].sort(reverse=True)
        res = []
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            while d[node]:
                dfs(d[node].pop())
            res.append(node)
        dfs("JFK")
        return res[::-1]

    