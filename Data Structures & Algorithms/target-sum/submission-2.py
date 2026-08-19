class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def solve(i, total):
            if (i, total) not in dp:
                r = 0
                if i == n - 1:
                    r = 1 if total == target else 0
                else:
                    r = solve(i + 1, total + nums[i + 1]) + solve(i + 1, total - nums[i + 1])
                dp[(i, total)] = r
            return dp[(i, total)]
        return solve(0, nums[0]) + solve(0, -nums[0])
        
