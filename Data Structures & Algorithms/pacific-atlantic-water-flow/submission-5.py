dirs = ((0,1), (0,-1), (1,0), (-1,0))
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights), len(heights[0])
        pac = set((i, 0) for i in range(n)) | set((0, i) for i in range(m))
        atl = set((i, m-1) for i in range(n)) | set((n-1, i) for i in range(m))
        def expand(visited):
            stack = list(visited)
            while stack:
                i,j = stack.pop()
                for di,dj in dirs:
                    ni,nj = i+di,j+dj
                    if 0 <= ni < n and 0 <= nj < m and (ni,nj) not in visited and heights[ni][nj] >= heights[i][j]:
                        visited.add((ni, nj))
                        stack.append((ni, nj))
            return visited
        return list(expand(pac) & expand(atl))
