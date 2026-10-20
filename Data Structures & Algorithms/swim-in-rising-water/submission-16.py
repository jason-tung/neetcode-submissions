dirs = ((0, 1), (0, -1), (1,0), (-1,0))
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq = [(grid[0][0], 0, 0)]
        visited = set((0, 0))
        n,m = len(grid), len(grid[0])
        while pq:
            cost, i, j = heapq.heappop(pq)
            if i == n - 1 and j == m - 1:
                return cost
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    heapq.heappush(pq, (max(grid[ni][nj], cost), ni, nj))
        return -1