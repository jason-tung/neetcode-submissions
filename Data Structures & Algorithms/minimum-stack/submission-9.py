class MinStack:

    def __init__(self):
        self.m = 0
        self.diffs = []

    def push(self, val: int) -> None:
        if not self.diffs:
            self.m = val
            self.diffs.append(0)
        else:
            diff = val - self.m
            self.diffs.append(diff)
            if val < self.m:
                self.m = val

    def pop(self) -> None:
        diff = self.diffs.pop()
        if diff < 0:
            self.m -= diff
            return self.m
        return self.m + diff

    def top(self) -> int:
        diff = self.diffs[-1]
        if diff < 0:
            return self.m
        return self.m + diff

    def getMin(self) -> int:
        return self.m
