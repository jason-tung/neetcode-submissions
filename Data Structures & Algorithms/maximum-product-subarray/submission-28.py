class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        hi = lo = 1
        m = -math.inf
        for k in nums:
            candidates = (k, hi * k, lo * k)
            hi, lo = max(candidates), min(candidates)
            m = max(m, hi)
        return m