dirs = ((0,1), (0,-1), (1,0), (-1,0))
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        def search(i,j,idx):
            if board[i][j] == word[idx]:
                if idx == len(word) - 1:
                    return True
                c, board[i][j] = board[i][j], "*"
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0<=ni<m and 0<=nj<n:
                        if search(ni, nj, idx+1):
                            return True
                board[i][j] = c
            return False
        for i in range(m):
            for j in range(n):
                if search(i,j,0):
                    return True
        return False