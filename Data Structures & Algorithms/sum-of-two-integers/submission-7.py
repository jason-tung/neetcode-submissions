class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b:
            a,b = a ^ b, (a & b & mask) << 1
        a &= mask
        if a >> 31:
            a = (-1 << 32) | a
        return a