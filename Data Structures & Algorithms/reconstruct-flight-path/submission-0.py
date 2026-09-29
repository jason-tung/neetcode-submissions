class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        node = "JFK"
        for a,b in tickets:
            d[a].append(b)
        for a in d:
            d[a].sort(reverse=True)
        s = []
        res = []
        while len(res) != len(tickets) + 1:
            if not d[node]:
                res.append(node)
                node = s.pop() if s else None
            else:
                s.append(node)
                node = d[node].pop()
        return res[::-1]

        