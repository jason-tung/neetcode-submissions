dirs = ((0,1), (0,-1), (1,0), (-1,0))
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)]
        visited = set()
        while pq:
            cost, i, j = heapq.heappop(pq)
            if i == m - 1 and j == n - 1:
                return cost
            if (i, j) in visited:
                continue
            visited.add((i,j))
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    heapq.heappush(pq, (max(cost, grid[ni][nj]), ni, nj))
        return -1