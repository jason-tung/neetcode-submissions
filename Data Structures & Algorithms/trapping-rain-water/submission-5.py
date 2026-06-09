class Solution:
    def trap(self, height: List[int]) -> int:
        tot = 0
        l, r = 0, len(height) - 1
        pre_max, post_max = height[l], height[r]
        while l < r:
            if pre_max > post_max:
                r -= 1
                tot += max(0, post_max - height[r])
                post_max = max(post_max, height[r])
            else:
                l += 1 
                tot += max(0, pre_max - height[l])
                pre_max = max(pre_max, height[l])
        return tot
