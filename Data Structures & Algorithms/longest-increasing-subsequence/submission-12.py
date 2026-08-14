class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            m = 0
            for p in range(n+1):
                a = dp[i+1][p]
                if p == n or nums[i] > nums[p]:
                    a = max(a, dp[i+1][i] + 1)
                dp[i][p] = a

        # s = [nums[k] if k != i else f"_{nums[i]}_" for k in range(n)]
        # print(s)
        # for k in dp:
        #     print(k)
        return dp[0][-1]
