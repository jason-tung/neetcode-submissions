class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        i, d, active = 0, {}, []
        qs = sorted(set(queries))
        intervals.sort()
        for q in qs:
            while i < len(intervals) and q >= intervals[i][0]:
                u,v = intervals[i]
                i += 1
                heapq.heappush(active, (v - u + 1, v))
            while active and active[0][1] < q:
                heapq.heappop(active)
            d[q] = active[0][0] if active else -1
        return [d[k] for k in queries]