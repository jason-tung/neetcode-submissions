class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        next_station, back_station = 0, n - 1
        while next_station != back_station + 1:
            if tank >= 0:
                tank += gas[next_station] - cost[next_station]
                next_station += 1
            else:
                tank += gas[back_station] - cost[back_station]
                back_station -= 1
        return next_station % n if tank >= 0 else -1
                