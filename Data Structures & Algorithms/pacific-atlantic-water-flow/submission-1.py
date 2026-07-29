dirs = ((1,0), (-1,0), (0,1), (0,-1))
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights), len(heights[0])
        pac_q = deque([(0,k) for k in range(m)] + [(k,0) for k in range(n)])
        atl_q = deque([(n - 1,k) for k in range(m)] + [(k,m - 1) for k in range(n)])
        def sol(q):
            ps = set()
            while q:
                (r,c) = q.popleft()
                ps.add((r,c))
                height = heights[r][c]
                for d in dirs:
                    nr,nc = r + d[0], c + d[1]
                    if (nr,nc) not in ps and 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and heights[nr][nc] >= height:
                        q.append((nr,nc))
            return ps
        atl_s, pac_s = sol(atl_q), sol(pac_q)
        return [list(k) for k in atl_s if k in pac_s]
