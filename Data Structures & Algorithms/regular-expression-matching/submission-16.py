class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s), len(p)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        def sol(i, j):
            if i == n:
                if j == m:
                    return 1
                elif p[j] == "*" or j + 1 < m and p[j + 1] == "*":
                    return sol(i, j + 1)
                else:
                    return 0
            if dp[i][j] == -1:
                if j >= m:
                    dp[i][j] = 0
                elif p[j] == "*":
                    if (p[j-1] == s[i] or p[j-1] == "."):
                        dp[i][j] = sol(i + 1, j) or sol(i, j + 1)
                    else:
                        dp[i][j] = sol(i, j + 1)
                elif j + 1 < m and p[j + 1] == '*':
                    dp[i][j] = sol(i, j + 1)
                elif s[i] == p[j] or p[j] == '.':
                    dp[i][j] = sol(i + 1, j + 1)
                else: 
                    dp[i][j] = 0
            return dp[i][j]
                
        return sol(0,0) == 1