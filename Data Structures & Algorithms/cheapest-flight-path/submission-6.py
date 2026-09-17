class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k += 1
        prices = [math.inf] * n
        prices[src] = 0
        nxt = [k for k in prices]
        for _ in range(k):
            for a,b,cost in flights:
                if prices[a] + cost < nxt[b]:
                    nxt[b] = prices[a] + cost
            prices = [k for k in nxt]
        return prices[dst] if prices[dst] != math.inf else -1