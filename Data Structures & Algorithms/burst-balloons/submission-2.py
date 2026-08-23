class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]
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

        def solve(i, j):
            if i > j:
                return 0
            if dp[i][j] == -1:
                for idx in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], pop(i, j, idx) + solve(i, idx - 1) + solve(idx + 1, j))
            return dp[i][j]
        return solve(0, n - 1)
