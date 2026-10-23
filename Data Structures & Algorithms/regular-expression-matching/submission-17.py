class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[-1] * n for _ in range(m)]
        def sol(i,j):
            if i == m:
                if j == n:
                    return 1
                if j + 1 < n and p[j+1] == "*":
                    return sol(i, j + 2)
                else:
                    return 0
            elif j == n:
                return 0
            elif dp[i][j] == -1:
                is_match = p[j] == '.' or p[j] == s[i]
                if j + 1 < n and p[j+1] == "*":
                    if is_match:
                        dp[i][j] = sol(i + 1, j) or sol(i, j + 2)
                    else:
                        dp[i][j] = sol(i, j + 2)
                elif is_match:
                    dp[i][j] = sol(i + 1, j + 1)
                else:
                    dp[i][j] = 0
            print(i,j,dp[i][j])
            return dp[i][j]
        return sol(0,0) == 1