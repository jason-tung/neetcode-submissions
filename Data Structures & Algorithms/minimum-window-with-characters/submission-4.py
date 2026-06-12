class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        need = len(count)
        l = 0
        min_l, min_r = -1, len(s)
        for r,c in enumerate(s):
            if c in count:
                count[c] -= 1
                if count[c] == 0:
                    need -= 1
            while need == 0:
                if r - l < min_r - min_l:
                    min_l,min_r = l,r
                if s[l] in count:
                    if count[s[l]] == 0:
                        need += 1
                    count[s[l]] += 1
                l += 1
        return '' if min_l == -1 else s[min_l:min_r+1]