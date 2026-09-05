dirs = [(0,1),(1,0), (0,-1),(-1,0)]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        res = []
        for k in range(math.ceil(min(m,n)/2)):
            d = 0
            i = j = k
            ni,nj = -1,-1
            while (k <= i <= n-1-k and k <= j <= m-1-k) and (ni, nj) != (k,k):
                res.append(matrix[i][j])
                ni,nj=i+dirs[d][0],j+dirs[d][1]
                if not(k <= ni <= n-1-k and k <= nj <= m-1-k):
                    d += 1
                    ni,nj=i+dirs[d][0],j+dirs[d][1]
                i,j = ni,nj

        return res
            



            