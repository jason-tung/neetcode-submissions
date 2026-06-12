class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        l = 0
        need = len(count)
        for r,c in enumerate(s2):
            if c in count:
                count[c] -= 1
                if count[c] == 0:
                    need -= 1
            if r - l + 1 > len(s1):
                if s2[l] in count:
                    if count[s2[l]] == 0:
                        need += 1 
                    count[s2[l]] += 1
                l += 1
            if need == 0:
                return True
        return False