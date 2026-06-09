class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        max_l = max_r = tot = 0
        while l < r:
            if height[l] < height[r]:
                tot += max(max_l - height[l], 0)
                max_l = max(max_l, height[l])
                l += 1
            else:
                tot += max(max_r - height[r], 0)
                max_r = max(max_r, height[r])
                r -= 1
        return tot