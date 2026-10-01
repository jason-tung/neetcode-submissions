class Solution:
    def trap(self, height: List[int]) -> int:
        left_wall = [0] * len(height)
        right_wall = [0] * len(height)
        for i in range(1, len(height)):
            j = len(height) - 1 - i
            left_wall[i] = max(height[i-1], left_wall[i - 1])
            right_wall[j] = max(height[j+1], right_wall[j + 1])
        res = 0
        for i in range(len(height)):
            h = height[i]
            res += max(min(left_wall[i], right_wall[i]) - height[i], 0)
        return res