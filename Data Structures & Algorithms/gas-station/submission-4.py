class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l, r = len(gas) - 1, 0
        diffs = [gas[i] - cost[i] for i in range(len(gas))]
        tank = diffs[l]
        while l != r:
            if tank >= 0:
                tank += diffs[r]
                r += 1
            else:
                l -= 1
                tank += diffs[l]
        return l if tank >= 0 else -1



        