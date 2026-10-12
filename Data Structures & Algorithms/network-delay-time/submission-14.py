class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        for u,v,t in times:
            d[u].append((v,t))
        visited = set()
        pq = [(0,k)]
        while pq:
            cost, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            if len(visited) == n:
                return cost
            for v,t in d[u]:
                if v not in visited:
                    heapq.heappush(pq, (cost + t, v))
        return -1