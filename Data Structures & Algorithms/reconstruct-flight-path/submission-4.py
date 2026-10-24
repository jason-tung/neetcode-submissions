class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for a,b in tickets:
            d[a].append(b)
        for c in d:
            d[c].sort(reverse=True)
        res = []
        def explore(city):
            while d[city]:
                explore(d[city].pop())
            res.append(city)
            return res[::-1]
        return explore("JFK")
                