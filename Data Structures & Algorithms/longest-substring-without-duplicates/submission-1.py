class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        se = set()
        res = 0
        l = r = 0
        for r in range(len(s)):
            while s[r] in se and l < r:
                se.remove(d[l])
                l += 1
            se.add(s[r])
            d[r] = s[r]
            res = max(res, len(se))
        return res
            