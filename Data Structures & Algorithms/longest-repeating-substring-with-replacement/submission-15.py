class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = Counter()
        l = m = 0
        most_freq = 0
        for r, c in enumerate(s):
            d[c] += 1
            most_freq = max(d[c], most_freq)
            if r - l + 1 > most_freq + k:
                d[s[l]] -= 1
                l += 1
            m = max(m, r - l + 1)
        return m