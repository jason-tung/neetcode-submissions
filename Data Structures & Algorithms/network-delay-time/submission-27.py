class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = [(0, k)]
        visited = set()
        d = defaultdict(list)
        for u,v,t in times:
            d[u].append((v,t))
        while pq:
            cost, node = heapq.heappop(pq)
            if node not in visited:
                visited.add(node)
                if len(visited) == n:
                    return cost
                for v,t in d[node]:
                    if v not in visited:
                        heapq.heappush(pq, (cost + t, v))
        return -1
                