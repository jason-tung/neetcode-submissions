class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lo = hi = 1
        m = -math.inf
        for k in nums:
            cands = (k, k * lo, k * hi)
            lo,hi = min(cands), max(cands)
            m = max(hi, m)
        return m
