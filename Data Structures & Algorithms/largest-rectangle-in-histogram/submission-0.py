class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        last_biggest = []
        m = 0
        heights.append(0)
        for i,k in enumerate(heights):
            while last_biggest and k < last_biggest[-1][1]:
                p = last_biggest.pop()
                left = last_biggest[-1][0] if last_biggest else -1
                m = max(m, ((i-1) - left) * p[1])
            last_biggest.append((i,k))
        return m