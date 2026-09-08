class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        for k in range(1, n + 1):
            dp[k] = dp[k & (k-1)] + 1
        return dp