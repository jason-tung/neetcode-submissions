class CountSquares:

    def __init__(self):
        self.counter = defaultdict(int)
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
            counts = 1
            for x in (xi, xj):
                for y in (yi, yj):
                    if (x,y) != (xi,yi):
                        counts *= self.counter[(x, y)]
            tot += counts
        return tot

