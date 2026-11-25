class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        d = {}
        pq = []
        intervals.sort()
        sq = sorted(set(queries))
        i = 0
        for q in sq:
            while i < len(intervals) and intervals[i][0] <= q:
                u,v = intervals[i]
                heapq.heappush(pq, (v - u + 1, v))
                i += 1
            while pq and pq[0][1] < q:
                heapq.heappop(pq)
            d[q] = -1 if not pq else pq[0][0]
        return [d[q] for q in queries]
