class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        d = defaultdict(list)
        for a,b,t in times:
            d[a].append((t,b))
        h = [(0, k)]
        while h:
            cost, i = heapq.heappop(h)
            if i not in visited:
                visited.add(i)
                if len(visited) == n:
                    return cost
                for c2, k in d[i]:
                    if k not in visited:
                        heapq.heappush(h, (cost + c2, k))
        return -1
        
            