class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        return s[:len(s)//2] == s[len(s)//2 + (len(s) & 1):][::-1]

