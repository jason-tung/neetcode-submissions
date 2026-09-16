dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        sol = [[math.inf] * m for _ in range(n)]
        q = [(grid[0][0], 0, 0)]
        while sol[-1][-1] == math.inf:
            cost, i, j = heapq.heappop(q)
            if sol[i][j] != math.inf:
                continue
            sol[i][j] = cost
            for di, dj in dirs:
                ip, jp = i + di, j + dj
                if 0 <= ip < n and 0 <= jp < m and sol[ip][jp] == math.inf:
                    heapq.heappush(q, (max(sol[i][j], grid[ip][jp]), ip, jp))
        return sol[-1][-1]