class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, start, stop):
            if stop <= start:
                return nums[0]
            last_houses = [0, 0]
            for i in range(start,stop):
                n = nums[i]
                last_houses[0], last_houses[1] = last_houses[1], max(last_houses[0] + n, last_houses[1])
            return last_houses[1]
        n = len(nums)
        return max(helper(nums, 0, n - 1),helper(nums, 1, n))