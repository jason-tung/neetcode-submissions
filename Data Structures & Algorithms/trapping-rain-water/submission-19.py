class Solution:
    def trap(self, height: List[int]) -> int:
        l = lw = rw = tot =0
        r = len(height) - 1
        while l <= r:
            if height[l] >= height[r]:
                tot += max(0, rw - height[r])
                rw = max(height[r], rw)
                r -= 1
            else:
                tot += max(0, lw - height[l])
                lw = max(lw, height[l])
                l += 1
        return tot