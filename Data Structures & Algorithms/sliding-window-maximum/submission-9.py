class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lrmax, rlmax = [0] * len(nums), [0] * len(nums)
        res = []
        for i in range(len(nums)):
            if not i % k:
                lrmax[i] = nums[i]
            else:
                lrmax[i] = max(lrmax[i - 1], nums[i])
            j = len(nums) - 1 - i
            if not j % k or i == 0:
                rlmax[j] = nums[j]
            else:
                rlmax[j] = max(rlmax[j + 1], nums[j])
        for r in range(k - 1, len(nums)):
            lr, rl = rlmax[r - k + 1], lrmax[r]
            res.append(max(lr, rl))
        return res
