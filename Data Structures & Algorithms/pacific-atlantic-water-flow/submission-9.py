dirs = ((0,1), (0,-1), (1,0), (-1,0))
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac = {(0, i) for i in range(n)} | {(i, 0) for i in range(m)}
        atl = {(m-1, i) for i in range(n)} | {(i, n-1) for i in range(m)}
        def expand(visited):
            stack = list(visited)
            while stack:
                i,j = stack.pop()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    pair = (ni, nj)
                    if 0 <= ni < m and 0 <= nj < n and pair not in visited and heights[ni][nj] >= heights[i][j]:
                        visited.add(pair)
                        stack.append(pair)
            return visited
        return list(expand(pac) & expand(atl))