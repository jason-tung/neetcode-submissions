class Solution:
    def jump(self, nums: List[int]) -> int:
        cost = 0
        l = r = 0
        while r < len(nums) - 1:
            nxt_r = r
            while l <= r:
                nxt_r = max(nxt_r, l + nums[l])
                l += 1
            r = nxt_r
            cost += 1
        return cost

