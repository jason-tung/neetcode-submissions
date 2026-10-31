class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.myPow(x, -n)
        if n == 0:
            return 1
        mult = x if n % 2 else 1
        return mult * self.myPow(x * x, n // 2)