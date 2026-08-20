d = [(0,1), (1,0), (0,-1), (-1,0)]

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix), len(matrix[0])
        dp=[[-1]*m for _ in range(n)]
        def dfs(i,j):
            if dp[i][j] == -1:
                tot = 1
                for (r,c) in d:
                    ni, nj = i + r, j + c
                    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                        tot = max(tot, dfs(ni, nj) + 1)
                dp[i][j] = tot
            return dp[i][j]
        for i in range(n):
            for j in range(m):
                dfs(i,j)
        return max(max(k) for k in dp)