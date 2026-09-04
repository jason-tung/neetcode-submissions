class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        h = []
        ans = {}
        intervals.sort()
        i = 0
        for q in sorted(queries):
            ans[q] = -1
            while i < len(intervals) and intervals[i][0] <= q:
                s,e = intervals[i]
                heapq.heappush(h, (e - s + 1, e))
                i += 1
            while h and h[0][1] < q:
                heapq.heappop(h)
            if h:
                ans[q] = h[0][0]
        return [ans[q] for q in queries]