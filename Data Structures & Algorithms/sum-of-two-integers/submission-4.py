class Solution:
    def getSum(self, a: int, b: int) -> int:
        r = co = 0
        off = 0
        while (a or b or co) and off < 32:
            a1, b1 = a & 1, b & 1
            tmp = co
            co = tmp & a1 | tmp & b1 | a1 & b1
            s = a1 ^ b1 ^ tmp
            # print(f'a,b are {a:08b}, {b:08b}')
            # print(f"sum is {s:08b}, co is {co:08b}")
            r |= s << off
            # print(f"r is {r:08b}")
            off += 1
            a >>= 1
            b >>= 1
        if r >> 31:
            r = (-1 << 32) | r
        return r