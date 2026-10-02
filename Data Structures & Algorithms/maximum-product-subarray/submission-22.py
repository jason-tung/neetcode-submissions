class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        hi = lo = m = nums[0]
        for i in range(1, len(nums)):
            k = nums[i]
            cand = (k, hi * k, lo * k)
            hi = max(cand)
            lo = min(cand)
            m = max(hi, m)
        return m