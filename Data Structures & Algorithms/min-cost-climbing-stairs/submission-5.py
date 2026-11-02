class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a,b = 0, 0
        for i in range(len(cost)):
            a, b = b, min(a,b) + cost[i]
        return min(a,b)
