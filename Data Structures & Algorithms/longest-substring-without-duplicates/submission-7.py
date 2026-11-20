class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        m = 0
        for r in range(len(s)):
            if s[r] in window:
                l = r - len(window)
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
            window.add(s[r])
            m = max(m, len(window))
        return m
