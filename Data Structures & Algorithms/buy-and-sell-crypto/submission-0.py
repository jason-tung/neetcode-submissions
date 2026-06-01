class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_stock = float('inf')
        highest_profit = 0
        for k in prices:
            highest_profit = max(highest_profit,k-lowest_stock)
            if k < lowest_stock:
                lowest_stock = k
        return highest_profit
            