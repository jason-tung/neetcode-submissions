class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k += 1
        fewest_moves = [math.inf] * n
        prices = defaultdict(dict)
        for a,b,price in flights:
            prices[a][b] = price
        # cost, moves, node
        h = [(0, 0, src)]
        while h:
            cost, moves, node = heapq.heappop(h)
            if node == dst and moves <= k:
                return cost
            if moves < fewest_moves[node]:
                fewest_moves[node] = moves
            else:
                continue
            if moves < k:
                for nxt in prices[node]:
                    tot_cost = cost + prices[node][nxt]
                    tot_moves = moves + 1
                    heapq.heappush(h, (tot_cost, tot_moves, nxt))
        return -1
