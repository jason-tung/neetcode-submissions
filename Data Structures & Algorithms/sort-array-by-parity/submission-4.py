class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j = 0, len(nums)
        while i < j:
            if nums[i] % 2:
                j -= 1
                nums[j],nums[i] = nums[i],nums[j]
            else:
                i += 1
        return nums