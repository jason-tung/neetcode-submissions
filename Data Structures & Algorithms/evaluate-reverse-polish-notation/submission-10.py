class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(["+", "-", "*", "/"])
        for t in tokens:
            if t in ops:
                b, a = stack.pop(), stack.pop()
                if t == "+":
                    res = a + b
                elif t == "-":
                    res = a - b
                elif t == "*":
                    res = a * b
                else:
                    res = int(a / b)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[-1]