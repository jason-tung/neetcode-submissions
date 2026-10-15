class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            k = nums[i]
            if k in d:
                return [d[k], i]
            d[target-k] = i
        return []