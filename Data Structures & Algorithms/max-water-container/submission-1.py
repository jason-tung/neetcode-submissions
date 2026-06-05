class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0, len(heights)-1
        m = 0
        while i < j:
            v = (j - i) * min(heights[j],heights[i]) 
            m = max(v, m)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return m