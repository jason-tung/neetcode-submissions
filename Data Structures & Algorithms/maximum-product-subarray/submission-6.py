class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [-math.inf] * len(nums)
        dpn = [0] * len(nums)
        dp[0] = nums[0]
        if nums[0] < 0:
            dpn[0] = nums[0] 
        m = dp[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                dpn[i] = nums[i] * dpn[i-1]
                dp[i] = max(nums[i] * dp[i-1], nums[i])
            else:
                dpn[i] = min(nums[i], dp[i-1] * nums[i])
                dp[i] = max(nums[i], dpn[i-1] * nums[i])
            m = max(m, dp[i])
        return m