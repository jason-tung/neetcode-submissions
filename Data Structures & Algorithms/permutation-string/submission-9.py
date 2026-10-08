class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        letters_left = len(s1)
        l = 0
        for r in range(len(s2)):
            c = s2[r]
            if c in d:
                d[c] -= 1
                letters_left -= 1
            while l <= r and (c not in d or d[c] < 0):
                lc = s2[l]
                if lc in d:
                    d[lc] += 1
                    letters_left += 1
                l += 1
            if letters_left == 0:
                return True
        return False