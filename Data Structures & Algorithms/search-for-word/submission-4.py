dirs = ((0,1), (0,-1), (1,0), (-1,0))
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board), len(board[0])
        def dfs(i,j,d):
            if d < len(word) and word[d] == board[i][j]:
                d += 1
                if d == len(word):
                    return True 
                c, board[i][j] = board[i][j], "*"
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if dfs(ni, nj, d):
                            return True
                board[i][j] = c
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i,j, 0):
                    return True
        return False
                    