class Solution:
    def climbStairs(self, n: int) -> int:
        a = {}
        a[1],a[2] = 1,2
        for i in range(3, n + 1):
            a[i] = a[i-1] + a[i-2]
        return a[n]