class Solution:
    def checkValidString(self, s: str) -> bool:
        hi = lo = 0
        for c in s:
            if c == '(':
                hi += 1
                lo += 1
            elif c == ')':
                if hi == 0:
                    return False
                hi -= 1
                lo = max(0, lo - 1)

            else:
                lo = max(0, lo -1)
                hi += 1
        return lo <= 0 <= hi
        
