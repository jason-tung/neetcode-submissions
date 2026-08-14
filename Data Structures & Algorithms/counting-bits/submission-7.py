class Solution:
    def countBits(self, n: int) -> List[int]:
        # sol(i) = sol(i>>1) + i & 1
        d = [-1] * (n+1)
        d[0] = 0
        def sol(i):
            if d[i] == -1:
                d[i] = sol(i >> 1) + (i & 1)
            return d[i]
        for i in range(n+1):
            sol(i)
        return d
        
            