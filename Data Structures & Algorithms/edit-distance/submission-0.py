class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        n,m = len(word1), len(word2)
        dp = [[-1] * (m+1) for _ in range(n + 1)]
        dp[-1][-1] = 0
        def sol(i,j):
            if dp[i][j] == -1:
                ans = 0
                if i == n:
                    ans = 1 + sol(i, j+1)
                elif j == m:
                    ans = 1 + sol(i + 1, j)
                elif word1[i] == word2[j]:
                    ans = sol(i+1,j+1)
                else:
                    ans = 1 + min(sol(i+1, j), sol(i+1, j+1))
                dp[i][j] = ans
            return dp[i][j]
        a = sol(0,0)
        return a