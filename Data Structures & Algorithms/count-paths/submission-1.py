class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # using math
        m,n = m-1,n-1
        t = m + n
        return math.factorial(t)//(math.factorial(m) * math.factorial(n))

# 2,5
# 7! / 5!2! = 

# t = (m-1) + (n-1)
# t! / (m-1)! ( n-1)! = 