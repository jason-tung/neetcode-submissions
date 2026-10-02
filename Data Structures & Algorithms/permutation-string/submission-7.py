class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        num_left = len(s1)
        l = 0
        for r,c in enumerate(s2):
            if c in d:
                d[c] -= 1
                num_left -= 1
            while l <= r and (c not in d or d[c] < 0):
                if s2[l] in d:
                    d[s2[l]] += 1
                    num_left += 1
                l += 1
            if not num_left:
                return True
        return False
