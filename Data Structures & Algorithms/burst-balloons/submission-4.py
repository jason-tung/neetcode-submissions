class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        def pop(i, j, idx):
            if i - 1 < 0:
                left = 1
            else:
                left = nums[i - 1]
            if j + 1 >= n:
                right = 1
            else:
                right = nums[j + 1]
            return left * right * nums[idx]

        for l in range(1,n+1):
            for i in range(n - l + 1):
                j = i + l - 1
                for idx in range(i,j + 1):
                    left = dp[i][idx-1] if idx-1 >= i else 0
                    right = dp[idx+1][j] if idx + 1 <= j else 0
                    dp[i][j] = max(dp[i][j], pop(i, j, idx) + left + right)
        return dp[0][n-1]
