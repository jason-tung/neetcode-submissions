class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # no need to do nums <= 1 case per constraints
        p = 1
        l_to_r = [0 for k in nums]
        for i in range(len(nums)):
            l_to_r[i] = p
            p *= nums[i]
        p = 1
        r_to_l = [0 for k in nums]
        for i in range(len(nums)):
            i = len(nums) - 1 - i
            r_to_l[i] = p
            p *= nums[i]
        r = [0 for k in nums]
        for k in range(0,len(nums)):
            r[k] = l_to_r[k] * r_to_l[k]
        return r

            