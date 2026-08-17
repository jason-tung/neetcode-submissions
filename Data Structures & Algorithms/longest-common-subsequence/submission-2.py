class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        dp_prev = [0] * (n+1)
        for i in range(m - 1, -1, -1):
            dp = [0] * (n+1)
            for j in range(n - 1, -1, -1):
                take = dp_prev[j+1] + (1 if text1[i] == text2[j] else 0) 
                skip = max(dp[j + 1], dp_prev[j])
                dp[j] = max(take, skip)
            dp_prev = dp
        return dp[0]