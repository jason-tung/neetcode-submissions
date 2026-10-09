class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        for (u,v,t) in times:
            d[u].append((t,v))
        visited = set([k])
        q = d[k]
        heapq.heapify(q)
        res = 0
        while q and len(visited) != n:
            time, v = heapq.heappop(q)
            if v not in visited:
                visited.add(v)
                res = time
                for cost, i in d[v]:
                    if i not in visited:
                        heapq.heappush(q, (cost + time, i))
        return res if len(visited) == n else -1

        