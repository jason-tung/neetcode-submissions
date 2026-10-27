class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        d = {}
        qs = sorted(queries)
        intervals.sort()
        i = 0
        active = []
        for q in qs:
            while i < len(intervals) and intervals[i][0] <= q:
                a,b = intervals[i]
                heapq.heappush(active, (b - a + 1, b))
                i += 1
            while active and active[0][1] < q:
                heapq.heappop(active)
            d[q] = active[0][0] if active else -1
        return [d[q] for q in queries]