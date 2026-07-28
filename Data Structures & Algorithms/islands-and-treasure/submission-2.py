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
            if (r,c) not in visited:
                visited.add((r,c))
                grid[r][c] = val
                for dir in ((1,0), (-1,0), (0,1), (0,-1)):
                    rn = r + dir[0]
                    cn = c + dir[1]
                    if (rn,cn) not in visited and 0 <= rn < len(grid) and 0 <= cn < len(grid[0]) and grid[rn][cn] != -1:
                        q.append((rn, cn, val + 1))
