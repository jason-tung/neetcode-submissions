class CountSquares:

    def __init__(self):
        self.counts = Counter()


    def add(self, point: List[int]) -> None:
        x,y = point
        self.counts[(x,y)]+=1

    def count(self, point: List[int]) -> int:
        x,y = point
        point = tuple(point)
        tot = 0
        for x2,y2 in self.counts:
            if (x,y) == (x2,y2) or abs(x2-x) != abs(y2-y):
                continue
            tot += self.counts[(x2,y2)] * self.counts[(x,y2)] * self.counts[(x2,y)]
        return tot


