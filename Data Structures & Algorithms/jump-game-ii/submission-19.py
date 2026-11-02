class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = max_reach = steps = 0
        while max_reach < len(nums) - 1:
            nxt_reach = max_reach
            for i in range(r, max_reach + 1):
                nxt_reach = max(nxt_reach, nums[i] + i)
            max_reach = nxt_reach
            steps += 1
        return steps
