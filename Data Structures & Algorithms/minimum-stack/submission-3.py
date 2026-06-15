class MinStack:

    def __init__(self):
        self.diff_stack = []
        self.min_val = 0

    def push(self, val: int) -> None:
        if self.diff_stack:
            self.diff_stack.append(val - self.min_val)
            self.min_val = min(self.min_val, val)
        else:
            self.diff_stack.append(0)
            self.min_val = val

    def pop(self) -> None:
        p = self.diff_stack.pop()
        if p < 0:
            self.min_val -= p

    def top(self) -> int:
        if self.diff_stack[-1] < 0:
            return self.min_val
        return self.min_val + self.diff_stack[-1]

    def getMin(self) -> int:
        return self.min_val
