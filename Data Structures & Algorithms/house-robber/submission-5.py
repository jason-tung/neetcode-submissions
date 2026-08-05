class Solution:
    # opt(i) = Max(opt(i-2) + f(i), opt(i-1))
    # top down
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n
        def dfs(i):
            if cache[i] == -1:
                if i == 0:
                    cache[i] = nums[0]
                elif i == 1:
                    cache[i] = max(nums[0], nums[1])
                else:
                    cache[i] = max(dfs(i - 2) + nums[i], dfs(i-1))
            return cache[i]
        return dfs(n - 1)
                
            
