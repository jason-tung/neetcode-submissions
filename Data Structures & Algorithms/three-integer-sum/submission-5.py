class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                r.extend(self.twoSum(nums, i + 1, len(nums) - 1, -nums[i]))
        return r

    def twoSum(self, nums,i, j, k):
        start_i, start_j = i,j
        results = []
        while i < j:
            s = nums[i] + nums[j]
            if s < k:
                i += 1
            elif s > k:
                j -= 1
            else:
                results.append((nums[i],nums[j],-k))
                i += 1
                while nums[i] == nums[i-1] and i < j:
                    i += 1
        return results