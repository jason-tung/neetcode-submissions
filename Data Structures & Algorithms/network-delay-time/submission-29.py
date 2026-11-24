class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        pq = [(0,k)]
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v,t))
        while pq:
            cost, node = heapq.heappop(pq)
            if node not in visited:
                visited.add(node)
                if len(visited) == n:
                    return cost
                for v, t in adj[node]:
                    if v not in visited:
                        heapq.heappush(pq, (cost + t, v))
        return -1