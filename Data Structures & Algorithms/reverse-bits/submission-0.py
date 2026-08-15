class Solution:
    def reverseBits(self, n: int) -> int:
        s = 0
        offset = 0
        while n:
            if n & 1:
                s += (n & 1) << (31-offset)
            n >>= 1
            offset += 1
        return s