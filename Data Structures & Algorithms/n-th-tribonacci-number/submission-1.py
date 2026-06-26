class Solution:
    def tribonacci(self, n: int) -> int:
        d = {}
        d[0], d[1], d[2] = 0, 1, 1
        def helper(n):
            if n in d:
                return d[n]
            d[n] = sum(helper(n-k) for k in range(1,4))
            return d[n]
        return helper(n)