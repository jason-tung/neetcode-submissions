class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            if n == 1:
                return True
            s.add(n)
            nn = 0
            while n:
                nn += (n % 10)**2
                n //= 10
            n = nn
        return False