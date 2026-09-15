class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        d = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                (x1, y1) = points[i]
                (x2, y2) = points[j]
                d[i].append((abs(x1 - x2) + abs(y1 - y2), j))
                d[j].append((abs(x1 - x2) + abs(y1 - y2), i))
            heapq.heapify(d[i])
        cost = 0
        visited = set([0])
        while len(visited) != n:
            candidate = (math.inf, -1)
            for i in visited:
                while d[i] and d[i][0][1] in visited:
                    heapq.heappop(d[i])
                if d[i] and d[i][0] < candidate:
                    candidate = d[i][0]
            visited.add(candidate[1])
            cost += candidate[0]
        return cost
