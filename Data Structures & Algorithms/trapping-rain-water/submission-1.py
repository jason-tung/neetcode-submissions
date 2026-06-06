class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l_r_maxes = [0] * len(height)
        for i in range(1, len(height)-1):
            l_r_maxes[i] = max(l_r_maxes[i-1], height[i-1])
        r_l_max = 0
        for i in range(len(height)-2, 0, -1):
            r_l_max = max(height[i + 1], r_l_max)
            res += max(min(l_r_maxes[i], r_l_max) - height[i], 0)
        return res

