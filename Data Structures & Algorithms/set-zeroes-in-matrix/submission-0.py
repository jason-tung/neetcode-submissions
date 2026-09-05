class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m = len(matrix), len(matrix[0])
        cols, rows = set(), set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        