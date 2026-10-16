class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        qrs = sorted(set(queries))
        intervals.sort()
        d = {}
        active = []
        i = 0
        for q in qrs:
            while i < len(intervals) and q >= intervals[i][0]:
                a,b = intervals[i]
                heapq.heappush(active, (b - a + 1, b))
                i += 1
            while active and q > active[0][1]:
                heapq.heappop(active)
            d[q] = active[0][0] if active else -1
        return [d[k] for k in queries]