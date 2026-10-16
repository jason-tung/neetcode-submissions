class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def twoSum(i):
            target = -nums[i]
            l,r = i + 1, len(nums) - 1
            while l < r:
                tot = nums[l] + nums[r]
                if tot > target:
                    r -= 1
                elif tot < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                twoSum(i)
        return res