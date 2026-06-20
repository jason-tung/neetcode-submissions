class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, len(nums) - 1
        while nums[l] > nums[r]:
            m = (l + r)//2
            if nums[m] < nums[m-1]:
                return nums[m]
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return nums[l]
        

            
            