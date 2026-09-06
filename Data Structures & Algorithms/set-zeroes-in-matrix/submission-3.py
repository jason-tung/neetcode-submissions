class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m = len(matrix), len(matrix[0])
        zc = [False, False]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        zc[0] = True
                    if j == 0:
                        zc[1] = True
                    matrix[i][0] = 0 
                    matrix[0][j] = 0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if zc[0]:
            for j in range(m):
                matrix[0][j] = 0
        if zc[1]:
            for i in range(n):
                matrix[i][0] = 0
            
        


        