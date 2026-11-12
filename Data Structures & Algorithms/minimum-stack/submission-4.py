class MinStack:

    def __init__(self):
        self.stack, self.mins = [], [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> None:
        top = self.stack.pop()
        if self.mins[-1] == top:
            self.mins.pop()
        return top

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
