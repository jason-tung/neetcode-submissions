class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        l = 0
        num_zeros = 0
        for r,c in enumerate(s2):
            if c in count:
                count[c] -= 1
                if count[c] == 0:
                    num_zeros += 1
            if r - l + 1 > len(s1):
                if s2[l] in count:
                    count[s2[l]] += 1
                if count[s2[l]] == 1:
                    num_zeros -= 1 
                l += 1
            if num_zeros == len(count):
                return True
        return False