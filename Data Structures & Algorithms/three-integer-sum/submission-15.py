class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def twoSum(i):
            target = -nums[i]
            l,r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    sol.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            twoSum(i)
        return sol