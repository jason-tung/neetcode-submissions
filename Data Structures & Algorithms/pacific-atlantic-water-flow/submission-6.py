dirs = ((0,1), (0,-1), (1,0), (-1,0))
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r,c = len(heights), len(heights[0])
        pac = set((i, 0) for i in range(r)) | set((0, i) for i in range(c))
        atl = set((i, c - 1) for i in range(r)) | set((r - 1, i) for i in range(c))
        def expand(s):
            stack = list(s)
            while stack:
                i,j = stack.pop()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0<=ni<r and 0<=nj<c and heights[ni][nj] >= heights[i][j] and (ni,nj) not in s:
                        stack.append((ni, nj))
                        s.add((ni,nj))
            return s
        return list(expand(pac) & expand(atl))
