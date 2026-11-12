op = {"(": ")", "{": "}", "[": "]"}
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in op:
                stk.append(op[c])
            elif not stk or c != stk.pop():
                return False
        return not stk
        