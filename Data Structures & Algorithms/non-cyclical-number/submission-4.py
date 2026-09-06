class Solution:
    def isHappy(self, n: int) -> bool:
        def incr(n):
            nn = 0
            while n:
                nn += (n % 10)**2
                n //= 10
            return nn
        slow = n
        fast = incr(n)
        while slow != fast:
            slow = incr(slow)
            fast=incr(incr(fast))
        return slow == 1