class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sol = []
        board = [['.'] * n for _ in range(n)]
        cols_occupied, diags_occupied, other_diags_occupied = set(), set(), set()
        def dfs(i):
            if i >= n:
                return sol.append([''.join(k) for k in board])
            for j in range(n):
                if j not in cols_occupied and i + j not in diags_occupied and i - j not in other_diags_occupied:
                    board[i][j] = "Q"
                    cols_occupied.add(j)
                    diags_occupied.add(i + j)
                    other_diags_occupied.add(i - j)
                    dfs(i + 1)
                    cols_occupied.remove(j)
                    diags_occupied.remove(i + j)
                    other_diags_occupied.remove(i - j)
                    board[i][j] = "."
        dfs(0)                
        return sol