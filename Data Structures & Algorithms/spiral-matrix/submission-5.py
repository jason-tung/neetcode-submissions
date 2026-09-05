class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        res = []
        dirs = [(0,1),(1,0), (0,-1),(-1,0)]
        def dfs(rows,cols,r,c,ri,ci):
            if rows == 0 or cols == 0:
                return res
            for i in range(cols):
                r += ri
                c += ci
                res.append(matrix[r][c])
            return dfs(cols, rows - 1, r, c, ci, -ri)

        return dfs(n,m,0,-1,0,1)