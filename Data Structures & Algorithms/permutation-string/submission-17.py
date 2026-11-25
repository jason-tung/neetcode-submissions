class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        remain = len(s1)
        l = 0
        for r in range(len(s2)):
            if s2[r] in d:
                d[s2[r]] -= 1
                remain -= 1
            while l <= r and (s2[r] not in d or d[s2[r]] < 0):
                c = s2[l]
                if c in d:
                    d[c] += 1
                    remain += 1
                l += 1
            if not remain:
                return True
        return False