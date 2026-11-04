class CountSquares:

    def __init__(self):
        self.counter = Counter()
        self.keys = []

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point not in self.counter:
            self.keys.append(point)
        self.counter[point] += 1

    def count(self, point: List[int]) -> int:
        tot = 0
        xi, yi = point
        for xj, yj in self.keys:
            if (xj, yj) == (xi, yi) or abs(xi - xj) != abs(yi - yj):
                continue
            counts = self.counter[(xj, yj)]
            counts *= self.counter[(xi, yj)] * self.counter[(xj, yi)]
            tot += counts
        return tot

