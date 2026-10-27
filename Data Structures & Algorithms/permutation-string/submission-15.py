class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        n = len(s1)
        l = 0
        for r in range(len(s2)):
            c = s2[r]
            if c in d:
                d[c] -= 1
                n -=1 
            while l <= r and (c not in d or d[c] < 0):
                c2 = s2[l]
                if c2 in d:
                    d[c2] += 1
                    n += 1
                l += 1
            if n == 0:
                return True
        return False