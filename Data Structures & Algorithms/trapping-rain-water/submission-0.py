class Solution:
    def trap(self, height: List[int]) -> int:
        l_r_maxes = [0] * len(height)
        # can prob remove this and do this bit in place with second
        # pass -> keep running max and do math like that
        r_l_maxes = [0] * len(height)
        for i in range(1, len(height)-1):
            # MAX(max_height_up_to(i-1), height(i-1))
            l_r_maxes[i] = max(l_r_maxes[i-1], height[i-1])
            j = len(height) - 1 - i
            r_l_maxes[j]= max(r_l_maxes[j+1], height[j+1])
        res = 0
        for i in range(1, len(height)-1):
            res += max(min(l_r_maxes[i], r_l_maxes[i]) - height[i], 0)
        return res

