class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        letters_remaining = len(s1)
        l = 0
        for r in range(len(s2)):
            if s2[r] in d:
                d[s2[r]] -= 1
                letters_remaining -= 1
            if s2[r] not in d:
                for i in range(l,r):
                    d[s2[i]] += 1
                    letters_remaining += 1
                l = r + 1
            while l<=r and d[s2[r]] < 0:
                d[s2[l]] += 1
                letters_remaining += 1
                l += 1
            if letters_remaining == 0:
                return True
        return False
