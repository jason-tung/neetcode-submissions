class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        n = len(nums)
        def twoSum(i):
            target = -nums[i]
            l,r = i + 1, n - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    sol.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        nums.sort()
        for i in range(n):
            if i == 0 or nums[i] != nums[i-1]:
                twoSum(i)
        return list(sol)
