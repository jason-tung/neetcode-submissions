class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lo = [0] * len(nums)
        hi = [0] * len(nums)
        m = lo[0] = hi[0] = nums[0]
        for i in range(1, len(nums)):
            candidates = nums[i], lo[i-1] * nums[i], hi[i-1] * nums[i]
            lo[i] = min(candidates)
            hi[i] = max(candidates)
            m = max(m, hi[i])
        return m