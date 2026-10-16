class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost = [math.inf] * (n + 1)
        cost[0] = cost[k] = 0
        for _ in range(n - 1):
            nxt_cost = [*cost]
            for a,b,t in times:
                nxt_cost[b] = min(nxt_cost[b], cost[a] + t)
            cost = nxt_cost
        m = max(cost)
        return m if m != math.inf else -1
