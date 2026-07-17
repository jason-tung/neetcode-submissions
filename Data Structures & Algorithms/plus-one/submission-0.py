class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        co = 0
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            s = digits[i] + co
            digits[i] = s % 10
            co = s // 10
        if co:
            digits.insert(0, co)
        return digits