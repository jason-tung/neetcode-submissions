class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [math.inf] * n
        cost[src] = 0
        for _ in range(k + 1):
            nxt_cost = [*cost]
            for u,v,c in flights:
                nxt_cost[v] = min(nxt_cost[v], cost[u] + c)
            cost = nxt_cost
        return cost[dst] if cost[dst] != math.inf else -1