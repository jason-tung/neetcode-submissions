class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost = [math.inf] * (n + 1)
        cost[0] = cost[k] = 0
        for i in range(n - 1):
            for u,v,t in times:
                if cost[v] > cost[u] + t:
                    cost[v] = cost[u] + t 
        m = max(cost)
        return m if m != math.inf else -1