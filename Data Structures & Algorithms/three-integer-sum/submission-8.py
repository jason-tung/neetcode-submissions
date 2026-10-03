class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        def twoSum(i):
            target = -nums[i]
            d = set()
            for j in range(i + 1, len(nums)):
                k = nums[j]
                diff = target - k
                if diff in d:
                    if (nums[i], k, diff) not in sol:
                        sol.add((nums[i], k, diff))
                d.add(k)
        nums.sort()
        for i in range(len(nums)):
            twoSum(i)
        return list(sol)
