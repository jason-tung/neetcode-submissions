class Solution:
    def jump(self, nums: List[int]) -> int:
        reachable = 0
        next_reachable = 0
        num_jumps = 0
        i = 0
        while i <= len(nums):
            if reachable >= len(nums) - 1:
                return num_jumps
            reach = i + nums[i]
            next_reachable = max(next_reachable, reach)
            if i == reachable:
                reachable = next_reachable
                num_jumps += 1
            i += 1