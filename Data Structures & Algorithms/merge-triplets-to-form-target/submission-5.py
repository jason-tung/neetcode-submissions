class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [-math.inf] * 3
        for triplet in triplets:
            if all(triplet[i] <= target[i] for i in range(3)):
                for i in range(3):
                    cur[i] = max(cur[i], triplet[i])
        return all(cur[i] == target[i] for i in range(3))
                