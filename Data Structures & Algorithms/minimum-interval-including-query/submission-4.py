class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        d = {}

        srt_queries = sorted(list(set(queries)))
        timeline = []
        smallest_active = []
        active = [False] * n
        for i,(a,b) in enumerate(intervals):
            timeline.append((a, "0START", i))
            timeline.append((b, "1END", i))
        heapq.heapify(timeline)
        for q in srt_queries:
            while timeline and (q > timeline[0][0] or q == timeline[0][0] and timeline[0][1] == "0START"):
                t, evt, i = heapq.heappop(timeline)
                if evt == "0START":
                    # size, i
                    heapq.heappush(smallest_active, (intervals[i][1] - intervals[i][0] + 1, i))
                    active[i] = True
                else:
                    active[i] = False
            while smallest_active and not active[smallest_active[0][1]]:
                heapq.heappop(smallest_active)
            d[q] = -1 if not smallest_active else smallest_active[0][0]
        return [d[k] for k in queries]