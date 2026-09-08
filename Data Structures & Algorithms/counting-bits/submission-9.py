class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        if n == 0:
            return dp
        dp[1] = 1
        for k in range(2, n + 1):
            dp[k] = dp[k & (k-1)] + 1
        return dp