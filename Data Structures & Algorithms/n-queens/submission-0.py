class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sol = []
        board = [['.'] * n for _ in range(n)]
        rows_occupied, cols_occupied, diags_occupied, other_diags_occupied = set(), set(), set(), set()
        def dfs(i,j):
            if 0 <= i < n and 0 <= j < n:
                if i not in rows_occupied and j not in cols_occupied and i + j not in diags_occupied and i + (n - j) not in other_diags_occupied:
                    board[i][j] = "Q"
                    rows_occupied.add(i)
                    cols_occupied.add(j)
                    diags_occupied.add(i + j)
                    other_diags_occupied.add(i + (n-j))
                    if len(rows_occupied) == n and len(cols_occupied) == n:
                        sol.append([''.join(k) for k in board])
                    else:
                        for new_j in range(n):
                            dfs(i + 1, new_j)
                    rows_occupied.remove(i)
                    cols_occupied.remove(j)
                    diags_occupied.remove(i + j)
                    other_diags_occupied.remove(i + (n-j))
                    board[i][j] = "."
        for k in range(n):
            dfs(0, k)                
        return sol