class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        running = 0
        pref = [0] * 1000
        l,r = float('inf'), 0
        for trip in trips:
            pref[trip[1]] += trip[0]
            pref[trip[2]] -= trip[0]
            l = min(l, trip[1])
            r = max(r, trip[2])
        for i in range(l, r+1):
            running += pref[i]
            if running > capacity:
                return False
        return True
            