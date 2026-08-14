class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in nums]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-2, -1, -1):
            best = 0
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    best = dp[i][j] = max(dp[j][-1] + 1, best)
                else:
                    dp[i][j] = max(dp[i][j-1], best)
        # s = [nums[k] if k != i else f"_{nums[i]}_" for k in range(n)]
        return max(max(dp[i]) for i in range(n))
