class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        d = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                (x1, y1) = points[i]
                (x2, y2) = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                d[i][j] = dist
                d[j][i] = dist
        cost = 0
        visited = set()
        q = [(0, 0)]
        while len(visited) != n:
            while q[0][1] in visited:
                heapq.heappop(q)
            c, p = heapq.heappop(q)
            visited.add(p)
            cost += c
            for i in range(n):
                if i not in visited:
                    heapq.heappush(q, (d[p][i], i))
        return cost
