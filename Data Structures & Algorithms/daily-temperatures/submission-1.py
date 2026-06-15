class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i,k in enumerate(temperatures):
            while stack and k > stack[-1][0]:
                p = stack.pop()
                res[p[1]] = i - p[1]
            stack.append((k, i))
        return res
