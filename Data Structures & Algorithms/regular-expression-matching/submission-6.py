class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp=[[False] * (m+1) for _ in range(n + 1)]
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if j == m:
                    dp[i][j] = i == n
                    continue
                cur_match = i < n and (s[i] == p[j] or p[j] == ".")
                if j + 1 < m and p[j + 1] == "*":
                    if cur_match:
                        dp[i][j] = dp[i+1][j] or dp[i][j+2]
                    else:
                        dp[i][j] = dp[i][j+2]
                elif cur_match:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = False 
        return dp[0][0]