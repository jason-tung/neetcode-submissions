inf = 2147483647

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c, 0))
        while q:
            p = q.popleft()
            (r,c,val) = p
            if (r,c) not in visited and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != -1:
                visited.add((r,c))
                grid[r][c] = val
                for dir in ((1,0), (-1,0), (0,1), (0,-1)):
                    q.append((r + dir[0], c + dir[1], val + 1))
