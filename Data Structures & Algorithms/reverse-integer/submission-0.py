class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        n = (x >> 31) & 1
        if n:
            x *= -1
        while x:
            r *= 10
            r += x % 10
            x //= 10
        if n:
            r *= -1
        return r if -2**31 <= r <= 2**31 - 1 else 0