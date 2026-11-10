class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n=len(s),len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m:
                    if j == n:
                        dp[i][j] = True
                    elif j + 1 < n and p[j + 1] == "*":
                        dp[i][j] = dp[i][j+2]
                elif j != n:
                    is_match = p[j] == "." or p[j] == s[i]
                    if j + 1 < n and p[j + 1] == "*":
                        if is_match:
                            dp[i][j] = dp[i][j+2] or dp[i+1][j]
                        else:
                            dp[i][j] = dp[i][j+2]
                    elif is_match:
                        dp[i][j] = dp[i+1][j+1]
                    else:
                        dp[i][j] = False
        return dp[0][0]
                