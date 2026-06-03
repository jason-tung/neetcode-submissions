class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # no need to do nums <= 1 case per constraints
        p = 1
        l_to_r = [0 for k in nums]
        for i in range(len(nums)):
            p *= nums[i]
            l_to_r[i] = p
        p = 1
        r_to_l = [0 for k in nums]
        for i in range(len(nums)):
            i = len(nums) - 1 - i
            p *= nums[i]
            r_to_l[i] = p
        r = [0 for k in nums]
        r[0] = r_to_l[1]
        r[-1] = l_to_r[-2]
        for k in range(1,len(nums) -1):
            r[k] = l_to_r[k-1] * r_to_l[k+1]
        return r

            