class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost = [math.inf] * (n + 1)
        cost[0] = cost[k] = 0
        for _ in range(n - 1):
            for a,b,t in times:
                cost[b] = min(cost[b], cost[a] + t)
        m = max(cost)
        return m if m != math.inf else -1
