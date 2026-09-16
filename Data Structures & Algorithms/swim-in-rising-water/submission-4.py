dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = [[False] * n for _ in range(n)]
        q = [(grid[0][0], 0, 0)]
        while q:
            cost, i, j = heapq.heappop(q)
            if i == j == n - 1:
                return cost
            if not seen[i][j]:
                seen[i][j] = True
                for di, dj in dirs:
                    ip, jp = i + di, j + dj
                    if 0 <= ip < n and 0 <= jp < n and not seen[ip][jp]:
                        heapq.heappush(q, (max(cost, grid[ip][jp]), ip, jp))