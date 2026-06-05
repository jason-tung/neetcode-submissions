class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = -1, len(s)
        while i < j:
            i += 1
            j -= 1
            while i < len(s) and not(s[i].isalnum()):
                i += 1
            while j >= 0 and not(s[j].isalnum()):
                j -= 1
            if i < len(s) and j > 0 and s[i].lower() != s[j].lower():
                return False
        return True