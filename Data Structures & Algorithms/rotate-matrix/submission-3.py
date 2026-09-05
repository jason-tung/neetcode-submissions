class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        matrix.reverse()
        for i in range(n-1,-1,-1):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 0,2 -> 2,0

        # 123 789 741
        # 456 456 852
        # 789 123 963