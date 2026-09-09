class Solution:
    def getSum(self, a: int, b: int) -> int:
        r = co = 0
        off = 0
        while (a or b or co) and off < 32:
            a1, b1 = a & 1, b & 1
            tmp = co
            co = tmp & a1 | tmp & b1 | a1 & b1
            s = a1 ^ b1 ^ tmp
            r |= s << off
            off += 1
            a >>= 1
            b >>= 1
        if r >> 31:
            r = (-1 << 32) | r
        return r