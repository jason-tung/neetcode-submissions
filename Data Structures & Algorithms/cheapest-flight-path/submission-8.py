class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k += 1
        prices = [math.inf] * n
        prices[src] = 0
        nxt = prices.copy()
        d = defaultdict(set)
        for a,b,price in flights:
            d[a].add((b, price))
        proc = set([src])
        for _ in range(k):
            nxt_proc = set()
            for a in proc:
                for b,cost in d[a]:
                    if prices[a] + cost < nxt[b]:
                        nxt[b] = prices[a] + cost
                        nxt_proc.add(b)
            prices = nxt.copy()
            proc = nxt_proc
        return prices[dst] if prices[dst] != math.inf else -1