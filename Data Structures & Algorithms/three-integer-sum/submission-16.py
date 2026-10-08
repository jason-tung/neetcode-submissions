class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        def twoSum(i):
            target = -nums[i]
            l,r = i + 1, len(nums) - 1
            while l < r:
                subtotal = nums[l] + nums[r]
                if subtotal > target:
                    r -= 1
                elif subtotal < target:
                    l += 1
                else:
                    sol.append((nums[i], nums[l], nums[r]))
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            twoSum(i)
        return sol