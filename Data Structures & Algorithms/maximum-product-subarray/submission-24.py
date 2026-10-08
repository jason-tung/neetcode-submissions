class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf
        lo = hi = 1
        for num in nums:
            candidates = (num, num * lo, num * hi)
            lo, hi = min(candidates), max(candidates)
            res = max(res, hi)
        return res