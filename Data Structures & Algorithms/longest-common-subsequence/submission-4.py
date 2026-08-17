class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        dp = [[-1] * n for _ in range(m)]
        def solve(i,j):
            if i == m or j == n:
                return 0
            if dp[i][j] == -1:
                take = 0
                if text1[i] == text2[j]:
                    take = solve(i+1, j+1) + 1 
                dp[i][j] = max(take, solve(i+1, j), solve(i, j+1))
            return dp[i][j]
        return solve(0, 0)