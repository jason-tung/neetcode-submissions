import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s = Counter(s)
        set_t = Counter(t)
        for k in set_s:
            if set_s[k] != set_t[k]:
                return False
        return True