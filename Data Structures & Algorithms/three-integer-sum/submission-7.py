class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(i):
            target = -nums[i]
            d = set()
            sol = set()
            for j in range(i + 1, len(nums)):
                k = nums[j]
                diff = target - k
                if diff in d:
                    if (nums[i], k, diff) not in sol:
                        sol.add((nums[i], k, diff))
                d.add(k)
            return sol
        nums.sort()
        sol = set()
        for i in range(len(nums)):
            sol |= twoSum(i)
        return list(sol)

        
        