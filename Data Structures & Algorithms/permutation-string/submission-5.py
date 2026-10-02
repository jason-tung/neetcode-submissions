class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # counterize s1
        # correct letters var
        # slide window across s2 and update correct letters var
        d = Counter(s1)
        num_left = len(s1)
        l, r = 0, -1
        while r < len(s2) - 1:
            r += 1
            c = s2[r]
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
        return not num_left
