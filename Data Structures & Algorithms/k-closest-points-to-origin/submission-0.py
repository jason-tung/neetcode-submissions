class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = [(-math.sqrt(point[0]**2 + point[1] ** 2), point) for point in points]
        h = []
        for p in l:
            heapq.heappush(h, p)
            while len(h) > k:
                heapq.heappop(h)
        return [heapq.heappop(h)[1] for _ in range(len(h))]