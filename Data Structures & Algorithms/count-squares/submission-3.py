class CountSquares:

    # pick another point as vertex

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, pt: List[int]) -> int:
        r = 0
        for p, count in self.points.items():
            x1,y1 = p
            x2,y2 = pt
            if x1-x2 and y1-y2:
                c1,c2 = self.points[(x1,y2)] if (x1,y2) in self.points else 0, self.points[(x2,y1)] if (x2,y1) in self.points else 0 
                if c1 and c2:
                    r += count * c1 * c2
        return r
            


