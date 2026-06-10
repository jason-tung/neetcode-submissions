class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m, p = float('inf'), 0
        for k in prices:
            p = max(p, k-m)
            m = min(m, k)
        return p
            