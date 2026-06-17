class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrival_times = []
        ps = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
        for (pos, sp) in ps:
            arrival = (target-pos)/sp
            if not arrival_times or arrival > arrival_times[-1]:
                arrival_times.append(arrival)
        return len(set(arrival_times))