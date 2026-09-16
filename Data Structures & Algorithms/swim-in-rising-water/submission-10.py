dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def solve(w):
            reachable = [[False] * n for _ in range(n)]
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            def dfs(i,j,w):
                reachable[i][j] = grid[i][j] <= w
                if i == j == n - 1 and reachable[i][j]:
                    return True
                if reachable[i][j]:
                    for di,dj in dirs:
                        ip,jp = i+di, j+dj
                        if 0 <= ip < n and 0 <= jp < n and not visited[ip][jp]:
                            visited[ip][jp] = True
                            if dfs(ip, jp, w):
                                return True
            dfs(0,0,w)
            return reachable[-1][-1]
        lo, hi = min(min(k) for k in grid), max(max(k) for k in grid)
        i = 0
        while lo < hi:
            m = (lo + hi) // 2
            if solve(m):
                hi = m
            else:
                lo = m + 1
        return hi

        
