class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cura = curb = curc = 0
        a, b, c = target
        for x, y, z in triplets:
            if x <= a and y <= b and z <= c:
                cura, curb, curc = max(cura, x), max(curb, y), max(curc, z)
        return (cura, curb, curc) == (a, b, c)