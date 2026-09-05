dirs = [(0,1),(1,0), (0,-1),(-1,0)]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        i = j = d = 0
        cnt = 0
        marker = (i,j)
        res = []
        while len(res) < n * m:
            res.append(matrix[i][j])
            ni,nj = i + dirs[d][0], j + dirs[d][1]
            if not (cnt <= ni < n-cnt and cnt <= nj < m-cnt) or (ni, nj) == marker:
                d += 1
                ni,nj = i + dirs[d % 4][0], j + dirs[d % 4][1]
                if d == 4:
                    marker = (ni, nj)
                    d = 0
                    cnt += 1
            i,j = ni, nj
        return res
                