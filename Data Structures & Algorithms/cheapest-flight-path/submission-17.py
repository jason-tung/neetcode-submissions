class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [math.inf] * n
        costs[src] = 0
        for _ in range(k+1):
            nxt = [*costs]
            for u,v,c in flights:
                nxt[v] = min(nxt[v], costs[u] + c)
            costs = nxt
        return costs[dst] if costs[dst] != math.inf else -1