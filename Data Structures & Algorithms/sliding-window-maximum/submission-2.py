class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        ans = [0] * (len(nums) - k + 1)
        for r,n in enumerate(nums):
            l = r - k + 1
            while d and d[-1][0] < n:
                d.pop()
            d.append((n, r))
            while d and d[0][1] < l:
                d.popleft()
            if l >= 0:
                ans[l] = d[0][0]
        return ans
            
        