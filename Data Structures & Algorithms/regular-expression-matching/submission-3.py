class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp=[[-1] * m for _ in range(n + 1)]
        def sol(i,j):
            if j >= m:
                return i >= n
            if dp[i][j] == -1:
                if i >= n:
                    return j + 1 < m and p[j+1] == "*" and sol(i, j+2)
                cur_match = s[i] == p[j] or p[j] == "."
                if j + 1 < m and p[j+1] == "*":
                    if cur_match:
                        dp[i][j] = sol(i + 1, j) or sol(i, j + 2)
                    else:
                        dp[i][j] = sol(i, j + 2)
                elif cur_match:
                    dp[i][j] = sol(i+1, j+1)
                else:
                    dp[i][j] = False
            return dp[i][j]
        return sol(0,0)

        