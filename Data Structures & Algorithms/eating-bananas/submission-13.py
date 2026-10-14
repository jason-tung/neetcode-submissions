class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            m = (lo + hi) // 2
            time = sum(math.ceil(p/m) for p in piles)
            if time > h:
                lo = m + 1
            else:
                hi = m
        return hi