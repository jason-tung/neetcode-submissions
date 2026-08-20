class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, o = len(s1), len(s2), len(s3)
        if n + m != o:
            return False
        # sol(i,j) = sol(i+1, j) or sol(i, j+1)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = 1
        def sol(i,j):
            if dp[i][j] == -1:
                ans = False
                if i < n and s1[i] == s3[i + j]:
                    ans = sol(i+1,j) > 0
                if j < m and s2[j] == s3[i + j]:
                    ans = ans or sol(i,j+1) > 0
                dp[i][j] = 1 if ans else 0
            return dp[i][j]
        return sol(0,0) == 1