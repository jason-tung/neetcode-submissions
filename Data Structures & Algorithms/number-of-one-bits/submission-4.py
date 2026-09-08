class Solution:
    def hammingWeight(self, n: int) -> int:
        r = 0
        while n:
            r += 1
            n = n & (n - 1)
        return r