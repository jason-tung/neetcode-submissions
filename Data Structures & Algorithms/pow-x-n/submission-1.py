class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        res = 1
        while n >= 1:
            if n % 2:
                res *= x
            x = x * x
            n >>= 1
        return res