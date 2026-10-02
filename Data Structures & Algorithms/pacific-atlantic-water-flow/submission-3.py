dirs = [(1,0), (-1,0), (0,1), (0,-1)]
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights), len(heights[0])
        pac_start = [*[(0, i) for i in range(m)], *[(i, 0) for i in range(n)]]
        atl_start = [*[(n - 1, i) for i in range(m)], *[(i, m - 1) for i in range(n)]]
        pac_reachable, atl_reachable = set(pac_start), set(atl_start)
        def explore(q, visited):
            while q:
                i,j = q.pop()
                for di, dj in dirs:
                    ni,nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and \
                    heights[i][j] <= heights[ni][nj] and \
                    (ni, nj) not in visited:
                        visited.add((ni, nj))
                        q.append((ni, nj))
            return visited
        return list(explore(pac_start, pac_reachable) & explore(atl_start, atl_reachable))

