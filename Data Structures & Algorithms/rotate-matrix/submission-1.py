class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                k = n - 1 - j
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
        for i in range(n):
            for j in range(n-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]

            # 0,0 -> 2,2
            # 0,1 -> 1,2
            # i,j -> (n-1-j), (n-1-i)

        # 123 321 741
        # 456 654 852
        # 789 987 963