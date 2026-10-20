class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s), len(p)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        dp[-1][-1] = 1
        def solve(i,j):
            if dp[i][j] == -1:
                if i == n:
                    if p[j] == "*":
                        dp[i][j] = solve(i, j+1)
                    elif j + 1 < len(p) and p[j + 1] == "*":
                        dp[i][j] = solve(i, j + 1)
                    else:
                        dp[i][j] = 0
                elif j == m:
                    dp[i][j] = 0
                else:
                    if p[j] == "*":
                        if p[j-1] == s[i] or p[j-1] == ".":
                            dp[i][j] = solve(i+1,j) or solve(i, j+1)
                        else:
                            dp[i][j] = solve(i, j+1)
                    elif j + 1 < len(p) and p[j + 1] == "*":
                        dp[i][j] = solve(i, j + 1)
                    elif s[i] == p[j] or p[j] == ".":
                        dp[i][j] = solve(i + 1, j + 1)
                    else:
                        dp[i][j] = 0
            return dp[i][j]
        return solve(0,0) == 1