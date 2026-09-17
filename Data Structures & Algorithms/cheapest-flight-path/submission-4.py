class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k += 1
        best = [(math.inf, math.inf)] * n
        best[src] = (0,0)
        prices = defaultdict(dict)
        for a,b,price in flights:
            prices[a][b] = price
        # cost, moves, node
        h = [(0, 0, src)]
        while h:
            cost, moves, node = heapq.heappop(h)
            if node == dst and moves <= k:
                return cost
            for nxt in range(n):
                if nxt in prices[node] and moves < k:
                    tot_cost = cost + prices[node][nxt]
                    tot_moves = moves + 1
                    if tot_cost < best[nxt][0] or tot_moves < best[nxt][1]:
                        best[nxt] = (tot_cost, tot_moves)
                        heapq.heappush(h, (tot_cost, tot_moves, nxt))
        return -1
