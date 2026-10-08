class Solution:
    def climbStairs(self, n: int) -> int:
        # sol(i) = sol(i - 1) + sol (i - 2)
        # basecase: n = 1 -> 1, n = 2 -> 2
        a,b = 0, 1
        for i in range(n):
            a,b = b, a+b
        return b