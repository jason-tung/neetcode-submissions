class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(32):
            r |= (n & 1) << (31-i)
            n >>= 1
        return r