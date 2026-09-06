class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        co = 0
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            s = co + digits[i]
            digits[i] = s % 10
            co = s // 10
            if not co:
                return digits
        return [1] + digits if co else digits