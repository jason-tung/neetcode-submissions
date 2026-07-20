class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            if n in s:
               return False
            s.add(n)
            tmp = 0
            while n:
                tmp += (n % 10) ** 2
                n //= 10
            n = tmp
        return True