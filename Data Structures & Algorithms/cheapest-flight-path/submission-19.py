class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [math.inf] * n
        cost[src] = 0
        for _ in range(k + 1):
            nxt = [*cost]
            for u,v,p in flights:
                nxt[v] = min(nxt[v], cost[u] + p)
            cost = nxt
        return cost[dst] if cost[dst] != math.inf else -1