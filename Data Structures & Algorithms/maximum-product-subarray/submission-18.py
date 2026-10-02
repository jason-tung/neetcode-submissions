class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_pos = -math.inf
        prev_neg = math.inf
        m = nums[0]
        if m >= 0:
            prev_pos = m
        if m <= 0:
            prev_neg = m
        for i in range(1, len(nums)):
            k = nums[i]
            if k > 0:
                pos = max(prev_pos * k, k)
                neg = prev_neg * k
                m = max(pos, m)
            elif k < 0:
                neg = min(prev_pos * k, k)
                pos = prev_neg * k
                m = max(pos, k, m)
            else:
                neg = pos = 0
                m = max(m, 0)
            prev_pos, prev_neg = pos, neg
        return m