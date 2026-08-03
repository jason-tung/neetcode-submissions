class Solution:
    # opt(i) = Max(opt(i-2) + f(i), opt(i-1))
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [0] * n
        for i in range(n):
            if i == 0:
                cache[i] = nums[i]
            elif i == 1:
                cache[i] = max(nums[0], nums[1])
            else:
                cache[i] = max(cache[i-2] + nums[i], cache[i-1])
        return cache[-1]
                
            
