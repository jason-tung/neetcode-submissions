class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= nums[(m - 1) % n]:
                return nums[m]
            # if nums[l] <= nums[m] <= nums[r]:
            #     return nums[l]
            if nums[l] <= nums[m]:
                if nums[m] >= nums[r]:
                    l = m + 1
                else:
                    return nums[l]
            else:
                r = m - 1
            