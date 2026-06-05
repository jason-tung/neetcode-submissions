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
            while i < j and (nums[i] + nums[j] < k or i!=start_i and nums[i] == nums[i-1]):
                i += 1
            while i < j and nums[i] + nums[j] > k:
                j -= 1
            if i < j and nums[i] + nums[j] == k:
                results.append((nums[i],nums[j],-k))
                i += 1
        return results