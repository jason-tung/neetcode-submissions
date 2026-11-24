class MinStack:

    def __init__(self):
        self.stack = []
        self.m = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.m = val
        else:
            self.stack.append(val - self.m)
            self.m = min(val, self.m)

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            self.m -= diff
            

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.m
        return self.stack[-1] + self.m

    def getMin(self) -> int:
        return self.m

# a: 1 2  0 3
# s: 1 1 -1 3
# m: 1 1  0 0
