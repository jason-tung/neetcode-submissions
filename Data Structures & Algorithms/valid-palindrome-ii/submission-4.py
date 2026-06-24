class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s, l, r, life=1):
            while l < r:
                if s[l] != s[r]:
                    if not life:
                        return False
                    life -= 1
                    return helper(s, l+1, r, 0) or helper(s, l, r-1, 0)
                l += 1
                r -= 1
            return True
        return helper(s, 0, len(s) - 1)
