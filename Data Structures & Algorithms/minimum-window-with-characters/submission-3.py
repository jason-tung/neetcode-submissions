class Solution:
    def minWindow(self, s: str, t: str) -> str:
        num_zero = l = 0
        counter = Counter(t)
        while l < len(s) and s[l] not in counter:
            l += 1 
        min_l,min_r = l,len(s)
        for r, c in enumerate(s):
            if r >= l:
                if c in counter:
                    counter[c] -= 1
                    if counter[c] == 0:
                        num_zero += 1
                if num_zero == len(counter):
                    if r - l < min_r - min_l:
                        min_l = l
                        min_r = r
                    if s[l] in counter:
                        counter[s[l]] += 1
                        if counter[s[l]] > 0:
                            num_zero -= 1
                    l += 1
                    while l < r and (s[l] not in counter or counter[s[l]] < 0):
                        if s[l] in counter:
                            counter[s[l]] += 1
                            if counter[s[l]] > 0:
                                num_zero -= 1
                        l += 1
                    if num_zero == len(counter):
                        if r - l < min_r - min_l:
                            min_l = l
                            min_r = r
        if min_r == len(s):
            return ""
        min_str = s[min_l:min_r+1]
        return min_str