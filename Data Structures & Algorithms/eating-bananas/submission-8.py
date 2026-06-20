class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        ret = r
        while l <= r:
            m = (l + r)//2
            s = sum([math.ceil(k / m) for k in piles])
            if s > h:
                l = m + 1
            else:
                ret = m
                r = m - 1
        return ret