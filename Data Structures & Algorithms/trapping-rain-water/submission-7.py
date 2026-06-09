class Solution:
    def trap(self, height: List[int]) -> int:
        tot = 0
        s = []
        for i in range(len(height)):
            while s and height[i] > height[s[-1]]:
                bot = s.pop()
                # need another left wall
                if not s:
                    break
                left = s[-1]
                tot += (i - left - 1) * (min(height[left], height[i]) - height[bot])
            s.append(i)
        return tot
