class Solution:
    def countBits(self, n: int) -> List[int]:
        # sol(i) = sol(i>>1) + i & 1
        d = [0] * (n+1)
        for k in range(1, n+1):
            d[k] = d[k>>1] + (k&1)
        return d
        
            