dirs = ((1,0), (-1,0), (0,1), (0,-1))
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m = len(board), len(board[0])
        visited = set()
        def dfs(r,c):
            visited.add((r,c))
            if board[r][c] == "O":
                for d in dirs:
                    nr,nc = r+d[0],c+d[1]
                    if (nr,nc) not in visited and 0 <= nr < n and 0 <= nc < m and board[nr][nc] == "O":
                        visited.add((nr,nc))
                        dfs(nr,nc)
        for r in (0,n-1):
            for c in range(m):
                dfs(r, c)
        for c in (0,m-1):
            for r in range(n):
                dfs(r, c)
        for r in range(n):
            for c in range(m):
                if (r,c) not in visited:
                    board[r][c] = "X"