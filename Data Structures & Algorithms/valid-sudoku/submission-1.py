class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rset = [0] * 9
        cset = [0] * 9
        sqset = [0] * 9
        for i in range(9):
            for j in range(9):
                # map to 0-8 then convert to bitshifted value
                n = board[i][j]
                if n != ".":
                    k = 1 << (int(board[i][j]) - 1)
                    if k & rset[i]:
                        return False
                    if k & cset[j]:
                        return False
                    if k & sqset[i//3+j//3*3]:
                        return False
                    rset[i] |= k
                    cset[j] |= k
                    sqset[i//3+j//3*3] |= k
        return True
                

        
