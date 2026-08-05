class Solution:
    # opt(i) = Max(opt(i-2) + f(i), opt(i-1))
    # bottom up with 2 counter cnstant space instead of full cache
    def rob(self, nums: List[int]) -> int:
        last_houses = [0, 0]
        for n in nums:
            last_houses[0], last_houses[1] = last_houses[1], max(last_houses[0] + n, last_houses[1])
        return last_houses[1]