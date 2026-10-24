class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pq = [(0, k + 1, src)]
        d = defaultdict(list)
        best = [-1] * n
        for u,v,c in flights:
            d[u].append((v,c))
        while pq:
            cost, steps, u = heapq.heappop(pq)
            if u == dst:
                return cost
            if steps > best[u]:
                best[u] = steps
                if steps > 0:
                    for v,c in d[u]:
                        heapq.heappush(pq, (cost + c, steps -1, v))
        return -1