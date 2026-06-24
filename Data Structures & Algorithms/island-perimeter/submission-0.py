class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        def eval(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or not grid[r][c]:
                return 0
            return 1
        def dfs(r, c):
            if (r,c) in seen:
                return 0
            seen.add((r,c))
            if not eval(r,c):
                return 0
            neighbors = [(r+ri, c+ci) for (ri, ci) in [(0,1), (0,-1), (1,0), (-1,0)]]
            self_score = 4 - sum(eval(r,c) for r,c in neighbors)
            neighbors_scores = sum([dfs(r,c) for r,c in neighbors])
            return neighbors_scores + self_score
        i = 0
        while not grid[i // rows][i % cols]:
            i += 1
        return dfs(i // rows, i % cols)