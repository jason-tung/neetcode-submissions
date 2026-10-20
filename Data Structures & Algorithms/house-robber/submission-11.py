class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def sol(i):
            if i >= len(nums):
                return 0
            if dp[i] == -1:
                dp[i] = max(nums[i] + sol(i + 2), sol(i+1))
            return dp[i]
        return sol(0)
