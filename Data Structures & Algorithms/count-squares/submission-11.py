class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x,y = point
        res = 0
        for x2,y2 in self.points:
            if x2 != x and y != y2:
                this_count = self.points[(x2,y2)]
                combos = ((x,y2), (x2, y))
                for a,b in combos:
                    if (a,b) in self.points:
                        this_count *= self.points[(a,b)]
                    else:
                        this_count = 0
                res += this_count
        return res
