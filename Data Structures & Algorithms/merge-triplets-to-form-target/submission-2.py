class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        sub = [-math.inf] * 3
        for k in range(3):
            for trip in triplets:
                if trip[k] == target[k] and trip[0] <= target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                    sub = [max(trip[i], sub[i]) for i in range(3)]
                    break
        return sub == target
        
