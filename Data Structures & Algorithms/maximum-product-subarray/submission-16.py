class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best_pos_prods = [-math.inf] * len(nums)
        best_neg_prods = [math.inf] * len(nums)
        m = nums[0]
        if nums[0] >= 0:
            best_pos_prods[0] = nums[0]
        if nums[0] <= 0:
            best_neg_prods[0] = nums[0]
        for i in range(1, len(nums)):
            k = nums[i]
            prev_pos, prev_neg = best_pos_prods[i-1], best_neg_prods[i-1]
            if k > 0:
                best_pos_prods[i] = max(prev_pos * k, k)
                best_neg_prods[i] = prev_neg * k
                m = max(best_pos_prods[i], m)
            elif k < 0:
                best_neg_prods[i] = min(prev_pos * k, k)
                best_pos_prods[i] = prev_neg * k
                m = max(best_pos_prods[i], k, m)
            else:
                best_pos_prods[i] = best_neg_prods[i] = 0
                m = max(m, 0)
        return m