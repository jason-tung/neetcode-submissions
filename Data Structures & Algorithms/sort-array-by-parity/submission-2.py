class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l,r = -1, len(nums)
        while True:
            l += 1
            r -= 1
            while l <= r and not nums[l] % 2:
                l += 1
            while l <= r and nums[r] % 2:
                r -= 1
            if l > r:
                return nums
            nums[l], nums[r] = nums[r],nums[l]