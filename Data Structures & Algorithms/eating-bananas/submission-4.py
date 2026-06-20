class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        while l < r:
            m = (l + r)//2
            s = sum([math.ceil(k / m) for k in piles])
            if s <= h:
                r = m
            else:
                l = m + 1
        return l