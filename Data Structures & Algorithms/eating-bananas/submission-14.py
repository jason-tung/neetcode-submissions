class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo,hi = 1,max(piles)
        while lo != hi:
            m = (hi + lo) // 2
            s = sum(math.ceil(pile/m) for pile in piles)
            if s > h:
                lo = m + 1
            else:
                hi = m
        return lo
            