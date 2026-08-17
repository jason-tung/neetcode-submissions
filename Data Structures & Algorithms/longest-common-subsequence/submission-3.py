class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        dp = [0] * (n+1)
        for i in range(m - 1, -1, -1):
            prev = 0
            for j in range(n - 1, -1, -1):
                take = dp[j+1] + (1 if text1[i] == text2[j] else 0) 
                skip = max(prev, dp[j])
                dp[j+1] = prev
                prev = max(take, skip)
                if j == 0:
                    dp[j] = prev
        return dp[0]