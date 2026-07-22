class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m_area = 0
        q = deque([(0, 0)])
        visited = set()
        while q:
            p = q.popleft()
            if p in visited:
                continue
            if grid[p[0]][p[1]] == 0:
                for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r,c = p[0] + d[0], p[1] + d[1]
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        q.append((r, c))
            else:
                a = 0
                island = [p]
                while island:
                    p = island.pop()
                    if p in visited:
                        continue
                    if grid[p[0]][p[1]] == 0:
                        q.append(p)
                    else:
                        visited.add(p)
                        a += 1
                        m_area = max(a, m_area)
                        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            r,c = p[0] + d[0], p[1] + d[1]
                            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                                island.append((r, c))
            visited.add(p)
        return m_area
