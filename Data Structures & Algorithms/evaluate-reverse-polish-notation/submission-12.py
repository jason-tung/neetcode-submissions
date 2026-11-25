ops = {'+', '-', '*', '/'}
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ops:
                b, a = int(stack.pop()), int(stack.pop())
                if token == "+":
                    c = a + b
                elif token == "-":
                    c = a - b
                elif token == "*":
                    c = a * b
                elif token == "/":
                    c = int(a / b)
                else:
                    raise Error("123")
                stack.append(c)
            else:
                stack.append(token)
        return int(stack[0])