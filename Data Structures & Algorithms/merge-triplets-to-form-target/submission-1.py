class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target_indicies = [k for k,v in sorted(enumerate(target), key=lambda k: -k[1])]
        sub = [-math.inf] * 3
        for k in target_indicies:
            candidate = [math.inf] * 3
            for trip in triplets:
                if trip[k] == target[k] and trip[0] <= target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                    candidate = trip
            sub = [max(candidate[i], sub[i]) for i in range(len(candidate))]
        return sub == target
        
