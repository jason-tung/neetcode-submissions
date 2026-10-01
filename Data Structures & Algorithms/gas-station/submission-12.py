class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        res = tank = deficit = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                deficit += tank
                tank = 0
                res = i + 1
        return res % n if tank >= -deficit else -1