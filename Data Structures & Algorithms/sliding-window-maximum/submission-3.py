class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        leftmax, rightmax = [0] * len(nums), [0] * len(nums)
        for l in range(len(nums)):
            r = len(nums) - 1 - l
            if l % k == 0:
                leftmax[l] = nums[l]
            else:
                leftmax[l] = max(leftmax[l-1], nums[l])
            if r % k == 0 or r == len(nums) - 1:
                rightmax[r] = nums[r]
            else:
                rightmax[r] = max(rightmax[r+1], nums[r])
        ans = []
        for l in range(len(nums) - k + 1):
            ans.append(max(leftmax[l + k - 1], rightmax[l]))
        return ans

            
        

            
        