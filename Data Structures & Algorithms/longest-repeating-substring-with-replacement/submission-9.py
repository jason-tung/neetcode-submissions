class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = m = 0
        pc = 0
        d = Counter()
        for r in range(len(s)):
            c = s[r]
            d[c] += 1
            pc = max(pc, d[c])
            if r - l + 1 > k + pc:
                d[s[l]] -= 1
                l += 1
            m = max(m, r - l + 1)
        return m
            
        