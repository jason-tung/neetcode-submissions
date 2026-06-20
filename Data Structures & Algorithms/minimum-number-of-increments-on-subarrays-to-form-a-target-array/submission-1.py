class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        last = 0
        for i in range(len(target)):
            if target[i] > last:
                res += target[i] - last
            last = target[i]
        return res