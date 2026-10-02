dirs = [(0,1), (1,0), (0,-1), (-1,0)]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, dep):
            if board[i][j] == word[dep]:
                if dep == len(word) - 1:
                    return True
                for (di, dj) in dirs:
                    ni, nj = i + di, j + dj
                    c = board[i][j]
                    board[i][j] = "*"
                    if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                        if dfs(ni, nj, dep + 1):
                            return True
                    board[i][j] = c
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False