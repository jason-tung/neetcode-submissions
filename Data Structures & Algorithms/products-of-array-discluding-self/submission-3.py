class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # no need to do nums <= 1 case per constraints
        p = 1
        pref = [0 for k in nums]
        for i in range(len(nums)):
            pref[i] = p
            p *= nums[i]
        p = 1
        for i in range(len(nums)):
            i = len(nums)-1-i
            pref[i] *= p
            p *= nums[i]
        return pref

            