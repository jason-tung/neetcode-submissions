dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parents = [[(i,j) for j in range(n)] for i in range(n)]
        size = [[1 for j in range(n)] for i in range(n)]
        def find(i,j):
            while parents[i][j] != (i,j):
                ip,jp = parents[i][j]
                parents[i][j] = parents[ip][jp]
                i,j = ip,jp
            return i,j
        def dsu(i1,j1,i2,j2):
            p1,p2 = find(i1,j1), find(i2,j2)
            if p1 != p2:
                if size[p1[0]][p1[1]] < size[p2[0]][p2[1]]:
                    p1,p2 = p2, p1
                parents[p2[0]][p2[1]] = p1
                size[p1[0]][p1[1]] += size[p2[0]][p2[1]]
            return size[p1[0]][p1[1]]
        w = 0
        edges = []
        for i in range(n):
            for j in range(n):
                for di,dj in dirs:
                    ip,jp = i + di, j + dj
                    if 0 <= ip < n and 0 <= jp < n:
                        edges.append((max(grid[i][j], grid[ip][jp]), i , j , ip , jp))
        heapq.heapify(edges)
        while find(n-1, n-1) != find(0,0):
            w, i1, j1, i2, j2 = heapq.heappop(edges)
            dsu(i1,j1,i2,j2)
        return w
            
            
