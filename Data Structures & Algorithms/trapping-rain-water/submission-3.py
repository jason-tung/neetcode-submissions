class Solution:
    def trap(self, height: List[int]) -> int:
        s = []
        res = 0
        for i, k in enumerate(height):
            while s and k > height[s[-1]]:
                col = s.pop()
                # need to check wall to left of current element
                if not s:
                    break
                left = s[-1]
                res += (i - left - 1) * (min(height[left], k)- height[col])
            s.append(i)
        return res

