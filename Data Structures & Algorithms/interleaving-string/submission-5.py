class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, o = len(s1), len(s2), len(s3)
        if n + m != o:
            return False
        # sol(i,j) = sol(i+1, j) or sol(i, j+1)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = 1
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i < n and s3[i+j] == s1[i]:
                    dp[i][j] += dp[i+1][j]
                if j < m and s3[i+j] == s2[j]:
                    dp[i][j] += dp[i][j+1]
        return dp[0][0] >= 1