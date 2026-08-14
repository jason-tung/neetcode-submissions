class Solution:
    def countBits(self, n: int) -> List[int]:
        d = [0] * (n+1)
        offset = 1
        for k in range(1, n+1):
            if k == offset:
                offset <<= 1
                d[k] = 1
            else:
                d[k] = d[k-(offset//2)] + 1
        return d
        
            