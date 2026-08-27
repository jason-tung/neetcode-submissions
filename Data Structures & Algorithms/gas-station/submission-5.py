class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l, r = len(gas) - 1, 0
        tank = gas[l] - cost[l]
        while l != r:
            if tank >= 0:
                tank += gas[r] - cost[r]
                r += 1
            else:
                l -= 1
                tank += gas[l] - cost[l]
        return l if tank >= 0 else -1



        