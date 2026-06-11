class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        max_freq = l = m = 0
        for r, c in enumerate(s):
            d[c] += 1
            max_freq = max(max_freq, d[c])
            if r - l + 1 - max_freq > k:
                d[s[l]] -= 1
                l += 1
            m = max(m, r - l + 1)
        return m