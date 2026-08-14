class Solution:
    def countBits(self, n: int) -> List[int]:
        d = [-1] * (n+1)
        d[0] = 0
        for k in range(1, n+1):
            l = k.bit_length()
            j = k ^ (1 << (l - 1))
            d[k] = d[j] + 1
        return d
        
            