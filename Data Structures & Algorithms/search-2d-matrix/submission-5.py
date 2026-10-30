class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        l,r = 0, m * n - 1
        while l <= r:
            med = (l + r)//2
            i,j = med // n, med % n
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                r = med - 1
            else:
                l = med + 1 
        return False