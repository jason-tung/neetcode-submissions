dirs = ((0,1), (0,-1), (1,0), (-1, 0))
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r,c = len(heights), len(heights[0])
        pac = {(ri, 0) for ri in range(r)} | {(0,ci) for ci in range(c)}
        atl = {(ri, c-1) for ri in range(r)} | {(r-1,ci) for ci in range(c)}
        def expand(visited):
            stack = list(visited)
            while stack:
                i,j = stack.pop()
                for di, dj in dirs:
                    ni,nj = i +di,j+dj
                    if 0<= ni < r and 0<=nj<c and (ni,nj) not in visited and heights[ni][nj] >= heights[i][j]:
                        visited.add((ni, nj))
                        stack.append((ni,nj))
            return visited 
        return list(expand(pac) & expand(atl))

