class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[(m-1)%len(nums)]:
                return nums[m]
            if nums[l] <= m <= nums[r]:
                return nums[l]
            if nums[r] >= nums[m]:
                r = m - 1
            else:
                l = m + 1
        return nums[l]