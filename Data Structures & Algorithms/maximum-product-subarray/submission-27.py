class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lo = hi = 1
        m = -math.inf
        for k in nums:
            cand = (k, lo * k, hi * k)
            hi,lo = max(cand), min(cand)
            m = max(m, hi)
        return m