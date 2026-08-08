class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # constant space
        m = lo = hi = nums[0]
        for i in range(1, len(nums)):
            candidates = nums[i], lo * nums[i], hi * nums[i]
            lo = min(candidates)
            hi = max(candidates)
            m = max(m, hi)
        return m