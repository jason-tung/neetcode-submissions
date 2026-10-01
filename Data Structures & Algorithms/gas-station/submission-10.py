class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        back_station = n - 1
        cur_station = 0
        while back_station >= cur_station:
            if tank >= 0:
                tank += gas[cur_station]
                tank -= cost[cur_station]
                cur_station += 1
            else:
                tank += gas[back_station]
                tank -= cost[back_station]
                back_station -= 1
        return (cur_station % n) if tank >= 0 else -1
    
                