class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        def eval(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or not grid[r][c]:
                return 0
            return 1
        for i in range(rows * cols):
            r,c = i // cols, i % cols
            if eval(r,c):
                neighbors = [eval(r+ri, c+ci) for (ri, ci) in [(0,1), (0,-1), (1,0), (-1,0)]]
                res += 4 - sum(neighbors)
        return res