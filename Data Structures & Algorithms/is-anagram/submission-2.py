class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = Counter(s)
        for c in t:
            d[c] -= 1
            if d[c] < 0:
                return False

        return True
