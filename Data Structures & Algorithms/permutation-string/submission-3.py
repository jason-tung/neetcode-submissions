class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # counterize s1
        # correct letters var
        # slide window across s2 and update correct letters var
        d = Counter(s1)
        num_left = len(s1)
        l = r = 0
        while r < len(s2):
            c = s2[r]
            if c not in d:
                while l != r:
                    d[s2[l]] += 1
                    num_left += 1
                    l += 1
                l = r + 1
            else:
                d[c] -= 1
                num_left -= 1
                if d[c] < 0:
                    while d[c] < 0:
                        d[s2[l]] += 1
                        num_left += 1
                        l += 1
            if not num_left:
                break 
            r += 1
        return not num_left
