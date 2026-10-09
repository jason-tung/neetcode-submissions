dirs = ((1,0), (-1,0), (0,1), (0,-1))
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights), len(heights[0])
        pac_border = {(0,i) for i in range(m)} | {(i, 0) for i in range(n)}
        atl_border = {(n - 1,i) for i in range(m)} | {(i, m-1) for i in range(n)}
        def genReachableSet(border):
            stack = list(border)
            while stack:
                i,j = stack.pop()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in border and heights[i][j] <= heights[ni][nj]:
                        border.add((ni, nj))
                        stack.append((ni, nj))
            return border
        return list(genReachableSet(pac_border) & genReachableSet(atl_border))
