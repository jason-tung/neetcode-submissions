class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        lw,rw = 0, 0
        tot = 0
        while l <= r:
            if height[l] >= height[r]:
                tot += max(rw - height[r], 0)
                rw = max(rw, height[r])
                r -= 1
            else:
                pass
                tot += max(lw - height[l], 0)
                lw = max(lw, height[l])
                l += 1
        return tot
