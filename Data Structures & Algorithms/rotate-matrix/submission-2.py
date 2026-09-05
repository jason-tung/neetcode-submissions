class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            k = n - 1 - i
            matrix[i], matrix[k] = matrix[k], matrix[i]
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 0,2 -> 2,0

        # 123 789 741
        # 456 456 852
        # 789 123 963