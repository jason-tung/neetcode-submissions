class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = m = 0
        pc = "@"
        d = Counter()
        for r in range(len(s)):
            c = s[r]
            d[c] += 1
            if d[c] >= d[pc]:
                pc = c
            if r - l + 1 > k + d[pc]:
                d[s[l]] -= 1
                l += 1
            m = max(m, r - l + 1)
        return m
            
        