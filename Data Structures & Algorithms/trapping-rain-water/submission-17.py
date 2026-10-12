class Solution:
    def trap(self, height: List[int]) -> int:
        lw = rw = l = tot = 0 
        r = len(height) - 1
        while l <= r:
            if height[l] <= height[r]:
                tot += max(lw - height[l], 0)
                lw = max(lw, height[l])
                l += 1
            else:
                tot += max(rw - height[r], 0)
                rw = max(rw, height[r])
                r -= 1
        return tot