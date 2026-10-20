class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        for u,v,t in times:
            d[u].append((v,t))
        q = [(0, k)]
        visited = set()
        while q:
            cost, u = heapq.heappop(q)
            if u not in visited:
                visited.add(u)
                if len(visited) == n:
                    return cost
                for v,t in d[u]:
                    if v not in visited:
                        heapq.heappush(q, (cost + t, v))
        return -1
