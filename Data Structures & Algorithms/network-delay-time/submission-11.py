class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dists = [math.inf] * (n + 1)
        dists[0] = dists[k] = 0
        for i in range(n - 1):
            for (u,v,t) in times:
                if dists[v] > dists[u] + t:
                    dists[v] = dists[u] + t
        m = max(dists)
        return m if m != math.inf else -1