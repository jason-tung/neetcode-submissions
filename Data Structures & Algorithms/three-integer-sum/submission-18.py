class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        def twoSum(i):
            target = -nums[i]
            l, r = i + 1, n - 1
            while l < r:
                sm = nums[l] + nums[r]
                if sm > target:
                    r -= 1
                elif sm < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            twoSum(i)
        return res