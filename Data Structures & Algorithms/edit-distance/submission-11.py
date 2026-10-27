class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        def solve(i,j):
            if i == m:
                return n - j
            elif j == n:
                return m - i
            if dp[i][j] == -1:
                if word1[i] == word2[j]:
                    dp[i][j] = solve(i + 1, j + 1)
                else:
                    dp[i][j] = 1 + min(solve(i+1, j), solve(i,j+1), solve(i+1, j+1))
            return dp[i][j]
        return solve(0,0)