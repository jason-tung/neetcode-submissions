class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                (x1,y1) = points[i]
                (x2, y2) = points[j]
                edges.append((abs(x1-x2) + abs(y1-y2), i, j))
        edges.sort()
        s = set()
        parent = list(range(n))
        size = [1] * n
        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        def union(i,j):
            ri, rj = find(i), find(j)
            if ri == rj:
                return -1
            if size[ri] < size[rj]:
                ri, rj = rj, ri
            parent[rj] = ri
            size[ri] += size[rj]
            return size[ri]
        for (cost, i , j) in edges:
            partition_size = union(i, j)
            if partition_size != -1:
                res += cost
            if partition_size == n:
                break
        return res