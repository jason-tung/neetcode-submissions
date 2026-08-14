class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n+1) for _ in range(n+1)]
        for k in range(n+1):
            dp[-1][k] = 0
        def dfs(i, p):
            if dp[i][p] == -1:
                a = dfs(i+1, p)
                if p == n or nums[p] < nums[i]:
                    a = max(dfs(i+1, i) + 1, a)
                dp[i][p] = a
            return dp[i][p]

        # s = [nums[k] if k != i else f"_{nums[i]}_" for k in range(n)]
        # print(s)
        # for k in dp:
        #     print(k)
        return dfs(0,n)
