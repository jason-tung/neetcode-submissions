class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        lw = rw = 0
        tot = 0
        while l <= r:
            if height[l] <= height[r]:
                tot += max(0, lw - height[l])
                lw = max(lw, height[l])
                l += 1
            else:
                tot += max(0, rw - height[r]) 
                rw = max(rw, height[r])
                r -= 1
        return tot