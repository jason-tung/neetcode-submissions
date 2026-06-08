class Solution:
    def trap(self, height: List[int]) -> int:
        pref_max_heights = [0] * len(height)
        res = 0
        for i in range(1, len(height)):
            pref_max_heights[i]=max(pref_max_heights[i-1], height[i-1])
        post_max_height = 0
        for i in range(len(height) - 2, -1, -1):
            post_max_height = max(post_max_height, height[i+1])
            res += max(min(pref_max_heights[i], post_max_height) - height[i], 0)
        return res

