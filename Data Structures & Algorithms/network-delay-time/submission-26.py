class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        visited = set()
        for u,v,t in times:
            d[u].append((v,t))
        pq = [(0, k)]
        while pq:
            cost, i = heapq.heappop(pq)
            if i not in visited:
                visited.add(i)
                if len(visited) == n:
                    return cost
                for v,t in d[i]:
                    heapq.heappush(pq, (cost + t, v))
        return -1

