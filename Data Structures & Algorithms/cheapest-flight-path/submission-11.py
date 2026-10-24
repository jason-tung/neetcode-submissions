class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pq = [(0, k + 1, src)]
        d = defaultdict(list)
        visited = set()
        best = [(math.inf, k + 1) for _ in range(n)]
        best[src] = (0, k + 1)
        for u,v,c in flights:
            d[u].append((v,c))
        while pq:
            cost, steps, u = heapq.heappop(pq)
            if u == dst:
                return cost
            if steps > 0:
                for v,c in d[u]:
                    nc, ns = cost + c, steps - 1
                    if nc <= best[v][0] or ns >= best[v][1]:
                        best[v] = (nc, ns)
                        heapq.heappush(pq, (cost + c, steps - 1, v))
        return -1