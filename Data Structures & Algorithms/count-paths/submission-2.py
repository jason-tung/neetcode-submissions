class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # using math
        m,n = m-1,n-1
        t = m + n
        prod = 1
        for k in range(max(m,n) + 1, t + 1):
            prod *= k
        for k in range(2,min(m,n) + 1):
            prod //= k
        return prod