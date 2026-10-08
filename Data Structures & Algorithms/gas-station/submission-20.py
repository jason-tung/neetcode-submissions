class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        back_station, next_station = n - 1, 0
        tank = 0
        while next_station <= back_station:
            if tank >= 0:
                tank += gas[next_station] - cost[next_station]
                next_station += 1
            else:
                tank += gas[back_station] - cost[back_station]
                back_station -= 1
        return next_station % n if tank >= 0 else -1