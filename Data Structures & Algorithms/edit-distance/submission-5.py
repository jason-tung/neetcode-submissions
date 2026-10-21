class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1), len(word2)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        def solve(i,j):
            if j == m:
                return n - i
            if i == n:
                return m - j
            if dp[i][j] == -1:
                # cases: same letter, different letter
                if word1[i] == word2[j]:
                    dp[i][j] = solve(i+1, j+1)
                else:
                    # can inserst, delete, replace
                    ins = solve(i, j+1)
                    delete = solve(i + 1, j)
                    repl = solve(i + 1, j + 1)
                    dp[i][j] = 1 + min(ins, delete, repl)
            return dp[i][j]
        return solve(0,0)
