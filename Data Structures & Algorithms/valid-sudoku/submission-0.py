class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        for row in board:
            s.clear()
            for k in row:
                if k in s:
                    return False
                self.add_if_num(s,k)
        for col_i in range(len(board)):
            s.clear()
            for row_i in range(len(board[0])):
                k = board[row_i][col_i]
                if k in s:
                    return False
                self.add_if_num(s,k)
        for box_row_num in range(len(board)//3):
            box_row_index = box_row_num * 3
            for box_col_num in range(len(board[0])//3):
                box_col_index = box_col_num * 3
                if not self.helper(board, (box_row_index, box_col_index), (box_row_index + 2, box_col_index + 2)):
                    return False
        return True

    def add_if_num(self, s, k):
        if k.isalnum():
            s.add(k)

    def helper(self, board, top_left, bottom_right):
        (start_row,start_col) = top_left
        (end_row,end_col) = bottom_right
        s = set()
        for ri in range(start_row, end_row + 1):
            for ci in range(start_col, end_col + 1):
                k = board[ri][ci]
                if k in s:
                    return False
                self.add_if_num(s,k)
        return True
