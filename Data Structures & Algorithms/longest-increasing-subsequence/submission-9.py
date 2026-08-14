class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # sol(n) = max(sol(m) + 1 for m > n if num[m] > num[n] else sol(m))
        dp = [-1] * n
        def sol(i):
            if dp[i] == -1:
                a = 1
                for j in range(i,n):
                    if nums[i] < nums[j]:
                        a = max(a, sol(j) + 1)
                dp[i] = a
            return dp[i]
        return max(sol(i) for i in range(n))
                    
        
