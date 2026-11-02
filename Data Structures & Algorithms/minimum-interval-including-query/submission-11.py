class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        d = {}
        sq = sorted(set(queries))
        active = []
        i = 0
        intervals.sort()
        for q in sq:
            while i < len(intervals) and q >= intervals[i][0]:
                a,b = intervals[i]
                heapq.heappush(active, (b - a + 1, b))
                i += 1
            while active and q > active[0][1]:
                heapq.heappop(active)
            d[q] = active[0][0] if active else -1
        return [d[q] for q in queries]