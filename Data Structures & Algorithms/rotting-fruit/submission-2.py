dirs = ((1,0), (-1,0), (0,1), (0,-1))
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        nextq = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c, 0))
                    grid[r][c] = 1
                if grid[r][c] == 1:
                    fresh += 1
        m = 0
        while q or nextq:
            if not q:
                q, nextq = nextq, q
            (r,c, nm) = q.popleft()
            if grid[r][c] == 1:
                m = nm
                grid[r][c] = 2
                fresh -= 1
                for d in dirs:
                    nr,nc = r + d[0], c + d[1]
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        nextq.append((nr,nc, m+1))
                
        return m if fresh == 0 else -1