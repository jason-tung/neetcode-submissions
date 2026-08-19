class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        dp[0] = 1
        for k in nums:
            new_dp = defaultdict(int)
            for tot in dp:
                new_dp[tot - k] += dp[tot]
                new_dp[tot + k] += dp[tot]
            dp = new_dp
        return dp[target]
        
