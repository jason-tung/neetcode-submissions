class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        d = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                (x1, y1) = points[i]
                (x2, y2) = points[j]
                d[i].append((abs(x1 - x2) + abs(y1 - y2), i, j))
                d[j].append((abs(x1 - x2) + abs(y1 - y2), j, i))
        cost = 0
        visited = set([0])
        q = d[0]
        heapq.heapify(q)
        while len(visited) != n:
            while q[0][1] in visited and q[0][2] in visited:
                heapq.heappop(q)
            (price, p1, p2) = heapq.heappop(q)
            cost += price
            if p1 in visited:
                p1, p2 = p2, p1
            visited.add(p1)
            for path in d[p1]:
                heapq.heappush(q, path)
        return cost
