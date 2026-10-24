class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        tickets.sort(reverse=True)
        for a,b in tickets:
            d[a].append(b)
        res = []
        def explore(city):
            while d[city]:
                explore(d[city].pop())
            res.append(city)
            return res
        return explore("JFK")[::-1]
                