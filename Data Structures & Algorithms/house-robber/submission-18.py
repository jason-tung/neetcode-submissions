class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def sol(i):
            if i < 0:
                return 0
            if dp[i] == -1:
                dp[i] = max(sol(i-2) + nums[i], sol(i-1))
            return dp[i]
        return sol(len(nums) - 1)
