class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1
            while temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = len(temperatures)
                    break
                j += 1
            res[i] = j - i if j < len(temperatures) else 0
        return res
