op = {"(": ")", "{": "}", "[": "]"}
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in op:
                stk.append(op[c])
            elif not stk or stk.pop() != c:
                return False
        return not len(stk)
        