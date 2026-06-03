class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = sum([1 if not num else 0 for num in nums])
        if num_zeros > 1:
            return [0 for k in nums]
        prod = 1
        for k in nums:
            prod *= k if k != 0 else 1
        if num_zeros == 0:
            return [prod//k for k in nums]
        return [0 if k != 0 else prod for k in nums]