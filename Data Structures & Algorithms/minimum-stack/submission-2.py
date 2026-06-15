class MinStack:

    def __init__(self):
        self.diff_stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.diff_stack.append((val - self.min_val) if self.diff_stack else 0)
        self.min_val = min(self.min_val, val)

    def pop(self) -> None:
        p = self.diff_stack.pop()
        m = self.min_val
        if not self.diff_stack:
            self.min_val = float('inf')
        elif p < 0:
            self.min_val -= p
        return p + m

    def top(self) -> int:
        if self.diff_stack[-1] < 0:
            return self.min_val
        return self.min_val + self.diff_stack[-1]

    def getMin(self) -> int:
        return self.min_val
