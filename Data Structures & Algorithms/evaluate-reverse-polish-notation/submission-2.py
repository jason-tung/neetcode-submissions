class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for k in tokens:
            print(k, s)
            if k.lstrip("-").isnumeric():
                s.append(int(k))
            else:
                b,a = s.pop(), s.pop()
                if k == "+":
                    s.append(a + b)
                elif k == "-":
                    s.append(a - b)
                elif k == '*':
                    s.append(a * b)
                else:
                    s.append(int(a/b))
        return s[0]

            