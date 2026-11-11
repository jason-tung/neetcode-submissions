class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = m = 0
        d = {}
        for r,c in enumerate(s):
            if c in d:
                l = max(d[c] + 1, l)
            d[c] = r
            m = max(m, r - l + 1)
        return m