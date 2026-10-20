class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        tot = len(s1)
        l = 0
        for r in range(len(s2)):
            c = s2[r]
            if c in d:
                d[c] -= 1
                tot -= 1
            else:
                for i in range(l, r):
                    d[s2[i]] += 1
                    tot += 1
                l = r + 1
            while d[c] < 0:
                d[s2[l]] += 1
                tot += 1
                l += 1
            if tot == 0:
                return True
        return False
