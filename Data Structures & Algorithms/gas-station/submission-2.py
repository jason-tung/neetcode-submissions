class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        deficit = 0
        res = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                deficit += tank
                res = i + 1
                tank = 0
            # print(i, res, tank, deficit)
        return res % len(gas) if tank >= -deficit else -1