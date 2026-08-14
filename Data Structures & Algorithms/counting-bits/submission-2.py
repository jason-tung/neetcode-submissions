class Solution:
    def countBits(self, n: int) -> List[int]:
        d = [-1] * (n+1)
        d[0] = 0
        offset = 0
        for k in range(1, n+1):
            if k == 2**offset:
                offset += 1
                d[k] = 1
            else:
                d[k] = d[k-2**(offset-1)] + 1
        return d
        
            