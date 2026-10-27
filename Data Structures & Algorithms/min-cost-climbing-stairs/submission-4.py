class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = b = 0
        for i in range(len(cost) - 1, -1, -1):
            a, b = cost[i] + min(a,b), a
        return min(a,b)

