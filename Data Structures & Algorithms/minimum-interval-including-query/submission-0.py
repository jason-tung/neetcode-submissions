from enum import IntEnum
from heapq import heappush, heappop
class Event(IntEnum):
    START = 0
    END = 2
    QUERY = 1

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = [-1] * len(queries)
        timeline = []
        for i, it in enumerate(intervals):
            s,e = it
            timeline.append((s, Event.START, e-s+1, i))
            timeline.append((e, Event.END, i))
        for i, q in enumerate(queries):
            timeline.append((q, Event.QUERY, i))
        timeline.sort()
        active = [False] * len(intervals)
        short = []
        for t, ty, *rest in timeline:
            match ty:
                case Event.START:
                    l, i = rest
                    active[i] = True
                    heappush(short, (l, i))
                case Event.END:
                    i = rest[0]
                    active[i] = False
                case Event.QUERY:
                    while short and not active[short[0][1]]:
                        heappop(short)
                    if short:
                        i = rest[0]
                        ans[i] = short[0][0]
        return ans

            

