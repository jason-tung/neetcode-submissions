class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def dist(i,j):
            (x1, y1) = points[i]
            (x2, y2) = points[j]
            return abs(x1 - x2) + abs(y1 - y2)
        costs = [math.inf] * n
        costs[0] = 0
        visited = set([0])
        p1 = 0
        while len(visited) != n:
            for p2 in range(n):
                if p2 not in visited:
                    costs[p2] = min(costs[p2], (dist(p1, p2)))
            best = math.inf
            for i in range(n):
                if i not in visited:
                    if costs[i] < best:
                        best = costs[i]
                        p1 = i
            visited.add(p1)
        return sum(costs)
