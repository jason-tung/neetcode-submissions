class Solution:
    def climbStairs(self, n: int) -> int:
        # sol(k) = sol(k-2) + sol(k-1)
        back2,back1 = 0, 1
        for _ in range(n):
            back1, back2 = back1 + back2, back1
        return back1