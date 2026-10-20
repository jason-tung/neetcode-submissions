class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        costs = [math.inf] * (n + 1)
        costs[0] = costs[k] = 0
        for _ in range(n-1):
            for a,b,t in times:
                costs[b] = min(costs[b], costs[a] + t)
        m = max(costs)
        return m if m != math.inf else -1