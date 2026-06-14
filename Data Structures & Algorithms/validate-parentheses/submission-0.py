class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in m:
                stack.append(c)
            elif not stack or c != m[stack.pop()]:
                    return False
        return not stack
        