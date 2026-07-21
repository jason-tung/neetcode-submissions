class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island_count = 0
        q = deque([(0, 0)])
        while q:
            popped = q.popleft()
            if popped in visited:
                continue
            visited.add(popped)
            land_squares = deque()
            if grid[popped[0]][popped[1]] == "1":
                island_count += 1
                land_squares.append(popped)
            else:
                for di, dj in [(1, 0), (0, 1)]:
                    r, c = popped[0] + di, popped[1] + dj
                    if (r, c) not in visited and 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        q.append((r, c))
            while land_squares:
                popped = land_squares.popleft()
                visited.add(popped)
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    r, c = popped[0] + di, popped[1] + dj
                    if (r, c) not in visited and 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        if grid[r][c] == "1":
                            land_squares.append((r, c))
                        else:
                            q.append((r, c))
        return island_count
