class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lo = hi = 1
        m = -math.inf
        for k in nums:
            candidates = (k, lo * k, hi * k)
            lo,hi = min(candidates), max(candidates)
            m = max(hi, m)
        return m