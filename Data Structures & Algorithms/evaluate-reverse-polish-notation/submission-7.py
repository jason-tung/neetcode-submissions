class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        args = []
        ops = {'+', '-', '*', '/'}
        for c in tokens:
            if c in ops:
                arg1, arg2 = args.pop(), args.pop()
                match c:
                    case '+':
                        res = arg2 + arg1
                    case '-':
                        res = arg2 - arg1
                    case '*':
                        res = arg2 * arg1
                    case '/':
                        res = int(arg2/arg1)
                args.append(res)
            else:
                args.append(int(c))
        return args[0]
