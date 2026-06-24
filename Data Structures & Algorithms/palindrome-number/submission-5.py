class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        ln = math.floor(math.log10(x)) + 1
        for i in range(ln // 2):
            l = ln - i - 1
            if (x // 10**i)%10 != (x // 10**l)%10:
                return False
        return True
