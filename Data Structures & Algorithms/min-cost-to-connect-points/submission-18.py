class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def dist(i,j):
            (x1, y1) = points[i]
            (x2, y2) = points[j]
            return abs(x1 - x2) + abs(y1 - y2)
        costs = [math.inf] * n
        costs[0] = 0
        visited = [0] * n
        visited[0] = 1
        edges = 1
        p1 = 0
        while edges != n:
            best, nxt = math.inf, -1
            for p2 in range(n):
                if not visited[p2]:
                    costs[p2] = min(costs[p2], (dist(p1, p2)))
                    if costs[p2] < best:
                        best, nxt = costs[p2], p2
            visited[nxt] = 1
            p1 = nxt
            edges += 1
        return sum(costs)
