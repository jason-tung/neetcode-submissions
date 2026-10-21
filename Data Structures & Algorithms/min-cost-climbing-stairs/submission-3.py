class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p1 = p2 = 0
        for i in range(len(cost) - 1, -1, -1):
            p1,p2 = cost[i] + min(p1, p2), p1
        return min(p1, p2)